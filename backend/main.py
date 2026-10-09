from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
import utils
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
from database import engine, get_db

#python -m uvicorn main:app --reload

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

@app.post("/register" , response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    #verificamos que el correo no este duplicado
    usuario_existente = db.query(models.User).filter(models.User.email == user.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail ="Este correo ya esta registrado")  

    #Verificamos que la cédula/RIF no esté duplicada
    cedula_existente = db.query(models.User).filter(models.User.cedula_rif == user.cedula_rif).first()
    if cedula_existente:
        raise HTTPException(status_code=400, detail="Esta cédula o RIF ya está registrada")
    
    #encriptamos la contrasena para que sea segura
    hashed_pw = utils.get_password_hash(user.password)
    
    codigo_generado = utils.generar_codigo()
    
    nuevo_usuario = models.User(
        nombre=user.nombre,
        apellido=user.apellido,
        cedula_rif=user.cedula_rif,
        telefono=user.telefono,
        email=user.email,
        hashed_password=hashed_pw,
        codigo_verificacion=codigo_generado
    )
    
    #guardamos en base de datos
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    utils.enviar_correo(nuevo_usuario.email, codigo_generado)
    
    return nuevo_usuario

@app.post("/verify")
def verify_user(user_data: schemas.UserVerify, db: Session = Depends(get_db)):
    #buscamos el usuario por su correo
    usuario = db.query(models.User).filter(models.User.email == user_data.email.first())
    #validamos que el usuario exista
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    #validamos que no este activo ya 
    if usuario.is_active:
        raise HTTPException(status_code=400, detail="La cuenta ya está verificada")
    
    #validamos que el codigo sea correcto
    if usuario.codigo_verificacion != user_data.codigo:
        raise HTTPException(status_code=400, detail="Código de verificación incorrecto")
    
    #activamos la cuenta
    usuario.is_active = True
    usuario.codigo_verificacion = None
    db.commit()
    
    return{"mensaje": "Cuenta verificada exitosamente. Ya puedes iniciar sesión."}