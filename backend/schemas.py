from pydantic import BaseModel, EmailStr

#esquema para cuando el usuario se registra
class UserCreate(BaseModel):
    nombre: str
    apellido: str
    cedula_rif: str
    telefono: str
    email: EmailStr
    password: str  

#esquema para devolver la informacion del usuario
class UserResponse(BaseModel):
    id:int
    nombre: str
    apellido: str
    email: EmailStr
    is_active: bool
    
    class Config:
        from_attributes = True
        