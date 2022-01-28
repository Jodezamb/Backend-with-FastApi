#Python
from typing import Optional # ti[ado estatico]

# Pydactic  -> es una libreria para importar modelos
from pydantic import BaseModel

#FASTAPI
from fastapi import FastAPI
from fastapi import Body # me permite de manera explicita que un parametro que llegas es de tipo Body

app=FastAPI()

# por el momento 

#models

'''Aqui vamos a crear los modelos nesarios para la aplicacion
    Pueden ser personas, carros, twitter y demas'''

class Person(BaseModel):
    #definir lo satributos del modelo 
    first_name: str
    last_name: str
    age:int
    hair_color:Optional[str]=None
    is_married:Optional[bool]=None

    '''Tambien podemos tener parametos opcionales para eso se importo 
        la libreria optional, el none se pone ya que puede haver o no puede haber nada en la base de datos'''



@app.get("/")  # del servidor al cliente
def home():
    return {"Hellow ":"World"}


#Request and response Body
# cuando se encuentre el ... signifia que un parametro es obligatorio
@app.post("/person/new") #El cliente se comunica con el servidor  tipo post datos del cliente al servidor
def create_person(person: Person=Body(...)): # hay que enbiar el request body dentro de la funcion 
    return person
