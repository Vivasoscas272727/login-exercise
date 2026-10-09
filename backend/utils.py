from passlib.context import CryptContext

#configuramos el motor de encriptacion

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#toma la contrasena y la transforma en untexto ilegible
def get_password_hash(password: str):
    return pwd_context.hash(password)

#compara la contrasena del usuario con la encriptada en la base de datos
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)