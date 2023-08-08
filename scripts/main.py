from fastapi import FastAPI, HTTPException, Query
from enum import Enum
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle

app = FastAPI(
    title="Steam Games Api ",
    description="Esta api es creada con la intención de que se pueda obtener a traves de metodos de solicitud HTTP diferente contenidos de nuestros dataframes de steam games",
    version="1.0.0",
)


df_parquet = pd.read_parquet(
    "../data/parquet/steam_model_api_parquet.parquet", engine="pyarrow"
)
df_v = df_parquet.copy()
## abrir modelo
with open("../modelos/modelo_entrenado_v3.pkl", "rb") as model_file:
    model = pickle.load(model_file)


## Listado de generos para elegir
class Genre(str, Enum):
    Action = "Action"
    Adventure = "Adventure"
    Casual = "Casual"
    Indie = "Indie"
    Racing = "Racing"
    Simulation = "Simulation"
    Sports = "Sports"
    Strategy = "Strategy"
    Massively_Multiplayer = "Massively Multiplayer"
    Rol = "RPG"


class Early(int, Enum):
    true = 1
    false = 0


def get_genre_values(selected_genre):
    genre_values = {genre: [1] if genre == selected_genre else [0] for genre in Genre}
    return genre_values


def filter_by_year(anio: str):
    anio_int = int(anio)
    if anio_int < 1970 or anio_int > 2018:
        raise HTTPException(
            status_code=400, detail="El año debe estar entre 1970 y 2018"
        )


@app.get(
    "/genero/{anio}",
    description="""En este endpoint donde pasaremos un año através del path para obtener los 5 generos que fueron lanzadas en el año que fue ingresado,                         
    Parámetros: - `anio`: Año para el cual se desean obtener los 5 generos mas lanzados.  
    Respuesta: - Retorna un diccionario con los 5 géneros más lanzados en el año ingresado.""",
)
async def genero(anio: str):
    filter_by_year(anio)
    df_year = df_v[df_v["año_v"].str.contains(anio)]
    lista = (
        df_year.loc[:, "Action":"Web Publishing"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .to_dict()
    )

    return {f"genres_top_5_for_{anio}": lista}


@app.get(
    "/juego/{anio}",
    description="""En este endpoint donde pasaremos un año através del path para obtener los juegos que fueron lanzadas en el año que fue ingresado,                            
    Parámetros: - `anio`: Año para el cual se desean obtener los juegos lanzados.  
    Respuesta: - Retorna un diccionario con los juegos más lanzados en el año ingresado.""",
)
async def juego(anio: str):
    filter_by_year(anio)
    df_year = df_v[df_v["año_v"].str.contains(anio)]
    lista = df_year["app_name"].head(20).tolist()
    return {f"Juegos del {anio}": lista}


@app.get(
    "/specs/{anio}",
    description="""En este endpoint donde pasaremos un año através del path para obtener las 5 especificaciones que fueron lanzadas en el año que fue ingresado,                    
    
    Parámetros: - `anio`: Año para el cual se desean obtener  las 5 especificaciones lanzados.
    
    Respuesta: - Retorna un diccionario con  las 5 especificacione más lanzados en el año ingresado.""",
)
async def specs(anio: str):
    filter_by_year(anio)
    df_year = df_v[df_v["año_v"].str.contains(anio)]
    lista = (
        df_year.loc[:, "Captions available":]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .to_dict()
    )

    return {f"specs_top_5_for_{anio}": lista}


@app.get(
    "/early_acces/{anio}",
    description="""En este endpoint donde pasaremos un año através del path para obtener los early_access especificaciones que fueron lanzadas en el año que fue ingresado, 
    
    Parámetros: - `anio`: Año para el cual se desean obtener los early_access lanzados.  
    
    Respuesta: - Retorna un diccionario con los early_access  más lanzados en el año ingresado.""",
)
async def early_acces(anio: str):
    filter_by_year(anio)
    df_year = df_v[df_v["año_v"].str.contains(anio)]
    lista = int(df_year["early_access"].sum())

    return {
        f"Cuantos Juegos con early access hubo en {anio}": f"La cantidad de juegos en early_Access fueron {lista} "
    }


@app.get(
    "/sentiment/{anio}",
    description="""En este endpoint donde pasaremos un año através del path para obtener la cantidad de criticas que tuvo el año que fue ingresado, 
    
    Parámetros: - `anio`: Año para el cual se desean obtener las criticas.  
    
    Respuesta: - Retorna un diccionario con los sentiment mas clasificados en el año ingresado.""",
)
async def sentiment(anio: str):
    filter_by_year(anio)
    df_year = df_v[df_v["año_v"].str.contains(anio)]
    df_limpio = df_year.drop(
        df_year[df_year["sentiment"].str.contains("user reviews", na=False)].index
    )
    df_limpio = df_limpio.dropna(subset=["sentiment"])
    df_limpio = df_limpio["sentiment"].value_counts().to_dict()
    return {anio: df_limpio}


@app.get(
    "/metascore/{anio}",
    description="""En este endpoint donde pasaremos un año através del path para obtener los juegos con mayor metascore en el año ingresado,  
    
    Parámetros: - `anio`: Año para el cual se desean obtener los metascore de los juegos. 
    
    Respuesta: - Retorna un diccionario con los juegos con mas metascore lanzados en el año ingresado.""",
)
async def metascore(anio: str):
    filter_by_year(anio)
    df_year = df_v[df_v["año_v"].str.contains(anio)]
    df_limpio = df_year.dropna(subset=["metascore"])
    df_eleg = df_limpio.loc[:, ["app_name", "metascore"]]
    app_names = (
        df_eleg.set_index("app_name")
        .sort_values(by="metascore", ascending=False)
        .head(5)
        .to_dict("series")
    )

    return {anio: app_names}


@app.post("/predict/")
async def predict(
    metascore: int,
    anio: str,
    early_access: Early = Query(..., description="Seleccione true o false"),
    genre: Genre = Query(..., description="Seleccione un genero"),
):
    if metascore < 0 or metascore > 100:
        raise HTTPException(
            status_code=400, detail="El año debe estar entre 1970 y 2018"
        )
    filter_by_year(anio)
    anio_int = int(anio)

    genre_values = get_genre_values(genre)
    genre_values_formatted = {
        genre.name: value for genre, value in genre_values.items()
    }

    # Crear un DataFrame con los valores de género
    input_data = pd.DataFrame(
        {
            "metascore": [metascore],
            "año_v": [anio_int],
            "early_access": [early_access],
            **genre_values_formatted,
        }
    )

    # Columnas a normalizar
    columns_to_normalize = ["año_v", "metascore"]

    # Crear un escalador MinMaxScaler
    scaler = MinMaxScaler()

    # Aplicar la normalización a las columnas seleccionadas
    input_data[columns_to_normalize] = scaler.fit_transform(
        input_data[columns_to_normalize]
    )

    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(input_data)

    return {
        "metascore": [metascore],
        "año_v": [anio_int],
        "early_access": [early_access],
        "selected_genre": genre,
        "prediction": prediction[0],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
