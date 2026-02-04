from pydantic import BaseModel
from typing import Optional
from datetime import datetime


#User Model
class User(BaseModel): #Schema
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str] #Parámetro opcional; es necesario importar Optional
    telefono:int
    correo:str
    creacion:datetime=datetime.now() #Fecha por defecto


class ShowUser(BaseModel): #Schema para devolver datos de un usuario
    username:str
    nombre:str
    correo:str
#User Model para Update
class UpdateUser(BaseModel): #Schema
    username:str=None
    password:str=None
    nombre:str=None
    apellido:str=None
    direccion:str=None #Parámetro opcional; es necesario importar Optional
    telefono:int=None
    correo:str=None
   