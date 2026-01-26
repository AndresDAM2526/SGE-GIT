from fastapi import APIRouter
from app.schemas import User,UserId

usuarios=[]

router=APIRouter(prefix="/user",tags=["Users"])

@router.get("/ruta1")
def ruta1():
    return{"mensaje":"Hemos creado nuestra primera API!!!"}


@router.get("/user")
def obtener_usuarios():
    return usuarios

@router.get("/user/{user_id}")
def obtener_usuario(user_id:int):
    for user in usuarios:
        if user["id"]==user_id: #Acceder al id de user(tipo dict) y comparar con user_id que se pasa como query
            return {"usuario":user}
    return{"respuesta":"Usuario no encontrado"}

@router.post("/user")
def crear_usuario(user:User):
    usuario=user.model_dump()
    usuarios.routerend(usuario)
    return{"respuesta":"Usuario creado!"}

@router.post("/userjson")
def obtener_usuario_json(user_id:UserId):
    for user in usuarios:
        if user["id"]==user_id.id: #Acceder al id del user (tipo dict) y comparar con el id de user_id que se pasa como json
            return{"usuario": user}
    return {"respuesta":"Usuario no encontrado"} #Si se pasa un id de un usuario que no existe

@router.delete("/user/{user_id}")
def eliminar_usuario(user_id:int):
    for index,user in enumerate(usuarios): #Necesitamos saber el índice y el valor para ver si el user_id es igual al que estamos recorriendo
        if user["id"]== user_id:
            usuarios.pop(index)
    return {"respuesta":"Usuario eliminado correctamente"}

@router.put("/user/{user_ïd}")
def actualizar_usuario(user_id:int,updateUser:User):
    for index,user in enumerate(usuarios): #Necesitamos saber el índice y el valor para ver si el user_id es igual al que estamos recorriendo
        if user["id"]== user_id:
            usuarios[index]["id"]=updateUser.model_dump()['id']
            usuarios[index]["nombre"]=updateUser.model_dump()['nombre']
            usuarios[index]["apellido"]=updateUser.model_dump()['apellido']
            usuarios[index]["direccion"]=updateUser.model_dump()['direccion']
            usuarios[index]["telefono"]=updateUser.model_dump()['telefono']
            return {"respuesta":"Usuario actualizado correctamente"}
    return {"respuesta":"Usuario NO encontrado"}
