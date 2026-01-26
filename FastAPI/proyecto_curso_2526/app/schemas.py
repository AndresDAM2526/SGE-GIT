from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel): #Schema
    id:int
    nombre:str
    apellido:str
    direccion:Optional[str] #Parámetro opcional; es necesario importar Optional
    telefono:int
    creacion_user:datetime=datetime.now() #Fecha por defecto

class UserId(BaseModel):
    id:int