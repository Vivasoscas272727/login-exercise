from pydantic import BaseModel, EmailStr

#esquema para cuando el usuario se registra
class UserCreate(BaseModel):
    email: EmailStr
    password: str  

#esquema para devolver la informacion del usuario
class UserResponse(BaseModel):
    id:int
    email: EmailStr
    is_active: bool
    
    class Config:
        from_attributes = True