from passlib.context import CryptContext
import smtplib
from email.mime.text import MIMEText
import random
import jwt 
from datetime import datetime, timedelta, timezone

#configuramos el motor de encriptacion

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#toma la contrasena y la transforma en untexto ilegible
def get_password_hash(password: str):
    return pwd_context.hash(password)

#compara la contrasena del usuario con la encriptada en la base de datos
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


#seccion de correos
CORREO_ORIGEN = "hvivas3027@gmail.com"
CONTRASENA_APP = "onwa elzv pyuu tqwr"

def generar_codigo():
    return str(random.randint(100000, 999999))

def enviar_correo(correo_destino: str, codigo: str):
    mensaje = MIMEText(f"¡Hola! Tu código de verificación es: {codigo}")
    mensaje["Subject"] = "Código de Verificación - App de Registro"
    mensaje["From"] = CORREO_ORIGEN
    mensaje["To"] = correo_destino
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(CORREO_ORIGEN, CONTRASENA_APP)
        server.sendmail(CORREO_ORIGEN,correo_destino, mensaje.as_string())
        
        
#token JWT

SECRET_KEY = "villarroel676767676767676767"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    #calculamos el tiempo en el que token expirara
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    
    #se crea el topken con la firma secreta
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    correo: str = payload.get("sub")
    return correo
    
