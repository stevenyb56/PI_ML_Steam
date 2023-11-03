# PROYECTO INDIVIDUAL Nº1 -Machine Learning 

### Objetivo

Este proyecto tiene como objetivo tomar datos proporcionada de la plataforma Steam, los cuales pasaran por diferentes etapas de limpieza y extracción necesarias para luego disponerlo en una API y generar un modelo de recomendación de juegos basado en Machine Learning.

Los datos proporcionados se encuentran comprimidos y en formato Json, cada Dataset se describe de la siguiente manera:  
1. steam_games consta de 120445 rows × 13 columns en las cuales se relaciona algunas como género, juego, precio y desarrolador 
2. user_reviews consta de 25799 rows × 3 columns en las cuales se relaciona algunas como usuario,juego, review y recoemndacion.
3. user_items consta de 88310 rows × 5 columns en las cuales se relaciona algunas como usuario, juego, cantidad de horas jugadas.

Los Dataset tienen en comun la columna id o item_id el cual es el identificador unico para cada juego, con este dato se podria relacionar los Datasets.

## API de Sistema de consultas y recomendaciones de juego.


Es necesario crear una API que pueda responder a diversas consultas utilizando los datos de STEAM relacionados con usuarios, reseñas y videojuegos.

Las consultas a desarrollar son las siguientes:

1) def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
2) def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
3) def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
4) def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
5) def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
6) def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.


## Desarrollo y arquitectura

Inicialmente, tenemos tres archivos .JSON:

* user_reviews.json: Contiene datos relacionados de reseñas y recomendaciones hechas por los usuarios.
* users_items.json: Contiene datos relacionados a usuarios, juegos, horas jugadas.
* steam_games.json: Contiene datos relacionados a los videojuegos, empresas desarrolladoras, género del juego.


Se efectuó un proceso de ETL (Extracción, Transformación y Carga) en relación a los tres archivos JSON originales. Dos de estos archivos poseían estructuras anidadas, es decir, contenían columnas con diccionarios o listas de diccionarios. Para abordar este desafío, se emplearon diversas estrategias con el propósito de convertir las claves de estos diccionarios en columnas individuales.

Además, se llevaron a cabo tareas de limpieza de datos, como el rellenado de valores nulos en aquellas variables esenciales para el proyecto. También se eliminaron columnas que presentaban una alta cantidad de valores faltantes o que no aportaban significativamente al proyecto, teniendo en cuenta las limitaciones de almacenamiento en la implementación.

Estas transformaciones y limpieza de datos se realizaron con el fin de mejorar el rendimiento de la API resultante. Para llevar a cabo todo este proceso, se hizo uso de la biblioteca Pandas.

Los documentos de ETL estan aca: [ETL_steamGames](https://github.com/stevenyb56/PI_ML_Steam/blob/main/Notebooks/2a_ETL_SteamGames.ipynb), [ETL UsersItems](https://github.com/stevenyb56/PI_ML_Steam/blob/main/Notebooks/2b_ETL_UserItems.ipynb) y [ETL UserReviews](https://github.com/stevenyb56/PI_ML_Steam/blob/main/Notebooks/2c_ETL_UserReviews.ipynb).

## Desarrollo de EDA

- En la exploracion de los datos limpios se pudo establecer correlaciones entre las variables, identificar patrones y tendencias:, detectar valores atipicos.

El documento EDA se encuentra aca [EDA](https://github.com/stevenyb56/PI_ML_Steam/blob/main/Notebooks/3_EDA.ipynb)

### Ajustes para la API

- Para habilitar las consultas, se implementó una solución consistente en generar archivos .csv más pequeños que pudieran ser consumidos por el web framework FastAPI. Esto resultó esencial debido a las restricciones de recursos en las versiones gratuitas tanto de FastAPI como de Render, una plataforma utilizada para alojar y desplegar aplicaciones en la nube.
EL documento Ajuste se encuentra aca [EDA](https://github.com/stevenyb56/PI_ML_Steam/blob/main/Notebooks/4_Ajustes_API.ipynb)


### Modelo de aprendizaje automático

- El modelo de ML se basa en una relación ítem-ítem, lo que significa que toma un juego en particular y, a partir de qué tan similar es ese juego con otros juegos en el conjunto de datos, recomienda otros juegos que son considerados similares. Esta recomendación se logra aplicando una métrica de similitud llamada "similitud del coseno". El cálculo de similitud del coseno permite medir cuán parecidos son dos juegos en función de sus características o atributos, como género, tema, características del juego, etc. Cuanto más cercano a 1 sea el valor del coseno, más similar se considera un juego a otro.

En resumen, este enfoque utiliza la similitud del coseno para determinar qué juegos son similares entre sí y, por lo tanto, cuáles pueden ser recomendados a los usuarios en función de sus preferencias y del juego que están explorando o jugando en ese momento.

El documento de ML se encuentra aca [Modelo ML](https://github.com/stevenyb56/PI_ML_Steam/blob/main/Notebooks/5_Modelo_recomendacion.ipynb)



## Enlaces

Link de Github 

* https://github.com/stevenyb56/PI_ML_Steam

Link de la Api
* https://steam-api-s5zr.onrender.com/docs#/default/recomendacion_juego_recomendacion_juego__id_game__get

Link del video
*
