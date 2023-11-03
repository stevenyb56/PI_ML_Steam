from fastapi import FastAPI
import pandas as pd
import numpy as np
import pickle


app = FastAPI()

@app.get('/inicio')
async def hola_mundo():
    return {'message': 'Hola Mundo!'}

@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero: str):
    genero = genero.strip().capitalize()
    df_end1 = pd.read_csv('end1.csv')
    
    # Filtrar el DataFrame para obtener las filas que coinciden con el género
    df_genero = df_end1[df_end1['Genres'] == genero]

    if df_genero.empty:
        return {"message": f"No se encontraron datos para el género {genero}"}

    # Encontrar el juego con más horas jugadas en el DataFrame filtrado
    juego_max_horas = df_genero.loc[df_genero['Hours'].idxmax()]

    # Obtener el año de lanzamiento del juego con más horas jugadas
    año_max_horas = juego_max_horas['Release_year']

    return {"message": f"Año de lanzamiento con más horas jugadas para {genero}: {año_max_horas}"}
    


@app.get('/UserForGenre/{genero}')
def UserForGenre( genero: str):

    df_end2 = pd.read_csv('end2.csv')

    # Convierte el género en una cadena y elimina posibles espacios en blanco al principio o al final
    genero = str(genero).strip()
    genero = genero.capitalize()

    # Filtra el DataFrame para obtener las filas que coinciden con el género
    df_genero = df_end2[df_end2['Genres'] == genero]

    if df_end2.empty:
        return {f"No existe este género: {genero}"}
    
    # Calcular la suma de horas jugadas por usuario y año
    horas_por_usuario_y_anio = df_end2.groupby(['User_id', 'Release_year'])['year4'].sum().reset_index()
    
    # Encontrar el usuario con más horas jugadas
    usuario_mas_horas = horas_por_usuario_y_anio.groupby('User_id')['year4'].sum().idxmax()
    
    # Filtrar las horas del usuario con más horas jugadas
    horas_del_usuario_mas_horas = horas_por_usuario_y_anio[horas_por_usuario_y_anio['User_id'] == usuario_mas_horas]
    
    # Crear la lista de acumulación de horas jugadas por año
    horas_acumuladas_por_anio = [{"Año": anio, "Horas": horas} for anio, horas in zip(horas_del_usuario_mas_horas['Release_year'], horas_del_usuario_mas_horas['year4'])]
    
    return {"Usuario con más horas jugadas para " + genero: usuario_mas_horas, "Horas jugadas": horas_acumuladas_por_anio}


@app.get('/UsersRecommend/{anio}')
def UsersRecommend(anio: int):

    # convierte el valor dado a tipo int y elimina espacios
    year = str(anio).strip()

    df_end3 = pd.read_csv('end3.csv')

    # Se filtra las filas en donde Recommend sea 1 y Positivo o Neutral sea 1
    recom_postivas = df_end3[(df_end3.Recommend == 1)&(df_end3.Positivo == 1)|(df_end3.Neutral == 1 )] # rp = recomendaicon positivas

    # se filtran las filas para el año especificado y se guarda en una variable
    Filtro_anio = recom_postivas[recom_postivas['Release_year'] == year]
    
    # Se filtra la variable anteior para agruparla por nombre y suma los valores de la columna 'Recomend', se ordena descendemente
    final = Filtro_anio.groupby('App_name')['Recommend'].sum().sort_values(ascending = False)

    # Se toman los 3 valores iniciales
    top_3 = final.head(3) 

    # Se crea una lista de diccionarios con los nombres y su posicion
    retorno = [{"Puesto 1": top_3.index[0]}, {"Puesto 2": top_3.index[1]}, {"Puesto 3": top_3.index[2]}]

    return retorno

@app.get('/UsersNotRecommend/{anio}')
def UsersNotRecommend(anio: int):

    # convierte el valor dado a tipo int y elimina espacios
    year = str(anio).strip()

    df_end4 = pd.read_csv('end3.csv')
    # Se filtra las filas en donde Recommend sea 0 y Malo sea 1
    recom_negativ = df_end4[(df_end4.Recommend == 0)&(df_end4.Malo == 1)] # rp = recomendaicon positivas
    
    # se filtran las filas para el año especificado y se guarda en una variable
    Filtro_anio = recom_negativ[recom_negativ['Release_year'] == year]
    
    # Se filtra la variable anteior para agruparla por nombre y suma los valores de la columna 'Recomend', se ordena descendemente
    rpy = Filtro_anio.groupby('App_name')['Recommend'].sum().sort_values(ascending = False)

    # Se toman los 3 valores iniciales
    top_3 = rpy.head(3) 

     # Se crea una lista de diccionarios con los nombres y su posicion
    retorno = [{"Puesto 1": top_3.index[0]}, {"Puesto 2": top_3.index[1]}, {"Puesto 3": top_3.index[2]}]

    return retorno

@app.get('/sentiment_analysis2/{anio}')
def sentiment_analysis2( anio : int ):
    df_end5 = pd.read_csv('end5.csv')

    year = str(anio).strip()

    # Se filtra las filas que coinciden con el año pedido
    comparar = df_end5[df_end5.Release_year == year]
    
    return{
        'Positivo': comparar.Positivo.to_list()[0],
        'Negativo': comparar.Malo.to_list()[0],
        'Neutral': comparar.Neutral.to_list()[0]
    }

@app.get('/recomendacion_juego/{id_game}')
def recomendacion_juego(id_game):

    id = int(id_game)  
    end6 = pd.read_csv('games_ml.csv')
    with open('item_similarity.pkl', 'rb') as model_file:
        # Carga el modelo serializado desde el archivo
        similarity_matrix = pickle.load(model_file)
    # Se encuentra el índice del juego
    
    game_index = end6[end6['Id_game'] == id].index[0]

    # Se calcula la similitud de coseno entre el juego seleccionado y todos los otros juegos
    similar_games_indices = similarity_matrix[game_index].argsort()[::-1][1:]

    # halla los títulos de los juegos similares a partir de los indices calculados
    similar_games_name = end6['App_name'].iloc[similar_games_indices]
    
    top5 = similar_games_name.head(5)

    return top5