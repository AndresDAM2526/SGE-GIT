from fastapi import APIRouter
from fastapi import APIRouter,Depends
from app.schemas import User
from app.db.database import get_db
from sqlalchemy.orm import Session
from app import models
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.schemas import User,ShowUser,UpdateUser
from typing import List


router=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/",response_model=List[ShowUser])
def obtener_usuarios(db:Session=Depends(get_db)):
    data=db.query(models.User).all()
    print(data)
    return data



@router.get("/{user_id}",response_model=ShowUser)
def obtener_usuario(user_id:int,db:Session=Depends(get_db)):
    usuario=db.query(models.User).filter(models.User.id==user_id).first()
    if not usuario:
        return {"Respuesta": "Usuario no encontrado"} #Si se pasa un id de un usuario que no existe
    return usuario
@router.post("/user")
def crear_usuario(user:User,db:Session=Depends(get_db)):
    usuario=user.model_dump()
    # user es lo que llega mediante el esquema del body
    #usuarios.append(usuario)
    nuevo_usuario=models.User(
        username=usuario['username'],
        password=usuario['password'],
        nombre=usuario['nombre'],
        apellido=usuario['apellido'],
        direccion=usuario['direccion'],
        telefono=usuario['telefono'],
        correo=usuario['correo'],
    )
    try:
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
    except IntegrityError as e:
        db.rollback
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El nombre de usuario o el correo ya existen en nuestra base de datos")


    

@router.delete("/user/{user_id}")
def eliminar_usuario(user_id:int,db:Session=Depends(get_db)):
    usuario=db.query(models.User).filter(models.User.id==user_id).first()
    if not usuario:
        return {"Respuesta": "Usuario NO encontrado"}
    db.delete(usuario)
    db.commit()
    return {"Respuesta": "Usuario eliminado correctamente"}
   


@router.patch("/{user_id}")
def actualizar_usuario(user_id:int,updateUser:UpdateUser,db:Session=Depends(get_db)):
    usuario=db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        return {"Respuesta": "Usuario NO encontrado"}
    usuario.update(updateUser.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta": "Usuario actualizado correctamente"}
    
