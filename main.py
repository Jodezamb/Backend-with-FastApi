#Python
from turtle import update
from typing import Optional
from unittest import result # ti[ado estatico]

# Pydactic  -> es una libreria para importar modelos
from pydantic import BaseModel

#FASTAPI
from fastapi import FastAPI
from fastapi import Body , Query, Path# me permite de manera explicita que un parametro que llegas es de tipo Body

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

class Location(BaseModel):
    City:str
    Country:str
    Address:str

@app.get("/")  # del servidor al cliente
def home():
    return {"Hellow ":"World"}


#Request and response Body
# cuando se encuentre el ... signifia que un parametro es obligatorio
@app.post("/person/new") #El cliente se comunica con el servidor  tipo post datos del cliente al servidor
def create_person(person: Person=Body(...)): # hay que enbiar el request body dentro de la funcion 
    return person


#Validaciones query parameters

@app.get("/person/detail")
def show_person(
    name:Optional[str]=Query(
        None,
        min_length=1,# como un query pamater puedo ser opcional, pero para validar hay que poner el rango 
        max_length=50, 
        title="Person Name",
        description='This is the person name, its between 1 and 50 characters'
        ),
    age:str=Query(
        ...,
        title="Person Age",
        description="This is the person age. It's requiered"
        )
):
    return {name:age}

'''
Para especificar las validaciones, debemos pasarle como parámetros a la función Query lo que necesitemos validar.

Para tipos de datos str:

max_length : Para especificar el tamaño máximo de la cadena.
min_length : Para especificar el tamaño minimo de la cadena.
regex : Para especificar expresiones regulares.

Para tipos de datos int:

ge : (greater or equal than ≥) Para especificar que el valor debe ser mayor o igual.
le : (less or equal than ≤) Para especificar que el valor debe ser menor o igual.
gt : (greater than >) Para especificar que el valor debe ser mayor.
lt : (less than <) Para especificar que el valor debe ser menor.'''


# Validaciones path_paramaters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int=Path(...,gt=0),
    name:Optional[str]=Query(
        None,
        min_length=1,# como un query pamater puedo ser opcional, pero para validar hay que poner el rango 
        max_length=50, 
        title="Person Name",
        description='This is the person name, its between 1 and 50 characters'
        ),
    age:str=Query(
        ...,
        title="Person Age",
        description="This is the person age. It's requiered"
        )
    
    
    
):
    return {person_id: 'It exists'}


#Validations: rEQUEST BODY
@app.put("/person/{person_id}")
def update_person(
    person_id: int =Path(
    ...,
    title="Person Id",
    description="This is person Id",
    gt=0

    ),
    person: Person=Body(...),
    location: Location=Body(...)
    


    ):
    result=person.dict()
    result.update(location.dict())

    return result

