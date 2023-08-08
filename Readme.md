# Proyecto Individual Nº1 - Machine Learning Operations (MLOps)
<center>

![Henry Logo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)
</center>
<h1 align="center">  Descripción </h1>

Este repositorio contiene mi primer proyecto individual de la etapa de labs en Henry, donde asumo el rol de un MLOps Engineer. El objetivo del proyecto es llevar un modelo de recomendación al mundo real, abordando desde la preparación de datos hasta la creación de una API para consultas y la implementación de un modelo de predicción de precios de videojuegos.

<h1 align="center">  Contexto y Rol </h1>

Como Data Scientist en Steam, me enfrento al desafío de predecir el precio de un videojuego. Los datos disponibles presentan dificultades por la cantidad de datos nulos que se encuentran en las distintas columnas, y tambien datos que pueden llegar a ser irrelevantes para mi modelo. Para abordar este desafío, asumiré el rol de Data Engineer y MLOps Engineer.
<h1 align="center"> Estructura de datos  </h1>

```
Steam_ml_api_mlops/
├── Data/
│   ├── json/
│   ├── csv/
│   └── parquet/
├── modelos/
├── notebooks/
├── scripts/
└── src/
└── main.py
```
<h1 align="center"> Propuesta de Trabajo

<center>

![Steam](https://th.bing.com/th/id/OIP._M3izRCJakZiQrgJ0p9WVAHaEK?pid=ImgDet&rs=1)
</center>

<h2 align="center"> ETL-Scrapping </h2>
En la primer instancia del proyecto hice un script para extraer los datos faltantes que habia en release_date y sentiment, ¿Cómo hice esto? Através de webscrapping donde teniamos un filtro para obtener las url de los años que eran nulos, entonces a partir de esto podiamos entrar a la url y acceder a la información que faltaba, esto no salió a la perfección porque hubo muchos datos nulos igualmente pero quería hacer la prueba 

<h2 align="center"> ETL </h2>

En el MVP, el enfoque será en la lectura adecuada del dataset para su uso en la REST-api, y su uso en el modelo

<h2 align="center">  Desarrollo API </h2>

Se crea una API utilizando FastAPI para realizar consultas sobre los datos:

- Consulta de géneros más lanzados en un año. ``def genero(anio : str)`` 
- Consulta de juegos lanzados en un año. ``def juegos(anio : str)`` 
- Consulta de specs más repetidos en un año. ``def specs(anio : str)`` 
- Consulta de juegos lanzados en un año con early access.  ``def access(anio : str)`` 
- Consulta del análisis de sentimiento según el año de lanzamiento. ``def sentiment(anio : str)`` 
- Consulta de los top 5 juegos según año con mayor metascore. ``def metascore(anio : str)`` 

<h2 align="center"> Deployment  </h2>

<div display="flex">
<center>
<section>
<h2> Servicio para hacer deploy de nuestra api </h2>
<h3 >Render </h3>

![Render Logo](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/j8z02ssteea4zj1k1nyz)

La API se despliega en [Render](https://mlops-agustin-samperi.onrender.com) para su consumo.
</section>
<h2>FrameWork Usados</h2>

![FastApi Logo](https://th.bing.com/th/id/OIP.pGkVSWn5t5W8Hoi5WAkOEAAAAA?pid=ImgDet&rs=1)

![Pandas](https://www.kindpng.com/picc/m/574-5747046_python-pandas-logo-transparent-hd-png-download.png)

![Scikit-learn](https://th.bing.com/th/id/OIP.lkqc68a6b7_TLALs5fmI6AHaD_?pid=ImgDet&rs=1)

![Numpy](https://th.bing.com/th/id/OIP.SWV16sONAikzxOEE-So3XwHaC7?pid=ImgDet&rs=1)

</center>

</div>



<h2 align="center">  Análisis Exploratorio de los Datos (EDA) </h2>

Se realiza un análisis manual de los datos para comprender relaciones, outliers y patrones interesantes (Esta parte la emepece a hacer en conjunto con el ETL por eso hay partes donde hago analisis exploratorio en el mismo archivo [ETL_2](https://github.com/Pridewolf/PI-MlOps-AgustinS/blob/main/notebooks/ETL_2.ipynb).
 
<h2 align="center">  Modelo de Predicción </h2>

Se entrena un [modelo](https://github.com/Pridewolf/PI-MlOps-AgustinS/blob/main/notebooks/Modelo.ipynb) de machine learning para predecir precios de videojuegos, basado en género, año, early_access y metascore.

<h2 align="center">   Video </h2>

Se presenta un video de demostración mostrando consultas a la API y explicando el modelo de predicción. [VIDEO](https://www.youtube.com/watch?v=CMcQu7exAHs&feature=youtu.be)

<h2 align="center">  Criterios de Evaluación </h2>

- Prolijidad del código.
- Organización del repositorio y uso de carpetas.
- Cumplimiento de los requerimientos propuestos.
- Entrega del video de demostración.

## Fuente de Datos

- [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj?usp=drive_link)
- [Diccionario de Datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link)

## Material de Apoyo

Consulta los [recursos adicionales](https://github.com/HX-PRomero/PI_ML_OPS/raw/main/Material%20de%20apoyo.md) disponibles para el proyecto.

## Redes Personales 
[LinkedIn] (https://www.linkedin.com/in/agustin-samperi/)
[GitHub] (https://github.com/Pridewolf?tab=overview&from=2023-08-01&to=2023-08-08)
