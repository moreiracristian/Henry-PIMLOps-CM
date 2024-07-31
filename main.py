from fastapi import FastAPI
import pandas as pd


app = FastAPI()

# Leer los archivos Parquet
df_credits = pd.read_parquet('D:/CM_R480/HENRY/Módulos/PI LABs/Henry-PIMLOps-CM/data/procesado/credits_pilabs.parquet')
df_movies = pd.read_parquet('D:/CM_R480/HENRY/Módulos/PI LABs/Henry-PIMLOps-CM/data/procesado/movies_pilabs.parquet')


# Convertir la columna 'release_date' a datetime
df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], errors='coerce')

# Función para obtener el mes en español
def get_month_in_spanish(month_number):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return months[month_number - 1]

# Función para obtener el día en español
def get_day_in_spanish(day_number):
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return days[day_number - 1]

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    month_number = months.index(mes.lower()) + 1
    count = df_movies[df_movies['release_date'].dt.month == month_number].shape[0]
    return f"{count} películas fueron estrenadas en el mes de {mes}"

@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    day_number = days.index(dia.lower())
    count = df_movies[df_movies['release_date'].dt.weekday == day_number].shape[0]
    return f"{count} películas fueron estrenadas en los días {dia}"

@app.get("/score_titulo/{titulo_de_la_filmacion}")
def score_titulo(titulo_de_la_filmacion: str):
    film = df_movies[df_movies['title'].str.contains(titulo_de_la_filmacion, case=False)].iloc[0]
    return f"La película {film['title']} fue estrenada en el año {film['release_year']} con un score/popularidad de {film['popularity']}"

@app.get("/votos_titulo/{titulo_de_la_filmacion}")
def votos_titulo(titulo_de_la_filmacion: str):
    film = df_movies[df_movies['title'].str.contains(titulo_de_la_filmacion, case=False)].iloc[0]
    if film['vote_count'] < 2000:
        return f"La película {film['title']} no cumple con la condición de al menos 2000 valoraciones."
    return f"La película {film['title']} fue estrenada en el año {film['release_year']}. La misma cuenta con un total de {film['vote_count']} valoraciones, con un promedio de {film['vote_average']}"

@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    actor_films = df_credits[df_credits['actor'].str.contains(nombre_actor, case=False)]
    total_return = actor_films['return'].sum()
    avg_return = actor_films['return'].mean()
    count = actor_films.shape[0]
    return f"El actor {nombre_actor} ha participado de {count} cantidad de filmaciones, conseguiendo un retorno de {total_return} y un promedio de {avg_return} por filmación"

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    director_films = df_credits[(df_credits['department'].str.contains(nombre_director, case=False)) & (df_credits['job'].str.contains('director', case=False))]
    response = []
    for index, film in director_films.iterrows():
        response.append({
            "title": film['title'],
            "release_date": film['release_date'],
            "return": film['return'],
            "budget": film['budget'],
            "revenue": film['revenue']
        })
    return response