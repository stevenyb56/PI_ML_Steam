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

Puede obtener información detallada sobre el proceso ETL en los documentos titulados "2a_ETL_SteamGames.ipynb," "ETL australian_users_items," y "ETL australian_user_reviews."

## Resultados

En el archivo main.py tenemos:

* La creación de la API
* La importación de las librerías necesarias
* La importación de los distintos csv que utilizaremos
* Las 7 funciones disponibles para ser consultadas mediante la API

En el archivo requirements.txt tenemos la lista de las librerías a utilizar

Los resultados están disponibles en un sitio de Render de acceso público, desde donde se pueden realizar las consultas

Se llevó a cabo un proceso de extracción, transformación y carga (ETL) de los tres conjuntos de datos proporcionados. Dos de estos conjuntos de datos estaban estructurados de manera anidada, lo que significa que contenían columnas con diccionarios o listas de diccionarios. Para abordar esto, se implementaron diversas estrategias con el fin de transformar las claves de esos diccionarios en columnas independientes. También se llevaron a cabo tareas de limpieza de datos, incluyendo el relleno de valores nulos en variables fundamentales para el proyecto, así como la eliminación de columnas con una alta cantidad de valores faltantes o que no contribuían significativamente al proyecto. Estas acciones se llevaron a cabo con el objetivo de optimizar el rendimiento de la API y considerando las restricciones de almacenamiento en la implementación. Para realizar estas transformaciones, se utilizó la biblioteca Pandas.

Los detalles específicos del proceso ETL se encuentran disponibles en los documentos titulados "ETL output_steam_games," "ETL australian_users_items," y "ETL australian_user_reviews."








## Desarrollo de EDA

- Explorar los datos limpios para establecer correlaciones entre las variables.



## Enlaces

Tenemos disponibles todos los archivos ipynb, txt, py, csv necesarios en el siguiente repositorio de GITHUB:

* https://github.com/Jeremias44/Proyecto_Individual_1.git

Tenemos disponible un sitio en Render para realizar las consultas mencionadas en la introducción:

* Sitio principal: https://consultas-steam-jeremias-pombo.onrender.com/

* Sitio de consultas: https://consultas-steam-jeremias-pombo.onrender.com/docs

Tenemos un video donde se muestra el funcionamiento de la API respondiendo a distintas consultas:

* Link de Youtube: https://www.youtube.com/watch?v=NIOKhnZ9J7E&ab_channel=JEREM%C3%8DASPOMBO

