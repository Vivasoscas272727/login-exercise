from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine

#con este comando le decimos a SQLALCHEMY que revise y cree las tablas en MariaDB
models.Base.metadata.create_all(bind=engine)

#inicializamos FastAPI
app = FastAPI(title= "API de Autenticacion")

#configuramos los permisos los (CORS)
app.add_middleware( 
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#ruta basica para comprobar que todo este bien
@app.get("/")
def read_root():
    return{"mensaje" : "el backend esta funcionando bien y la base de datos esta conectada"}