from passlib.context import CryptContext
import smtplib
from email.mime.text import MIMEText
import random

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