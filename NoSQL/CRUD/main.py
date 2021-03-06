# mongoengine es una libreria que funciona para conectarse a una instancia de mongodb
# e interactuar con la base de datos.
from mongoengine import connect, Document, StringField, DecimalField
# Mongo server port: 27017

DATABASE_NAME = 'store'

# db_client recibe el resultado de la ejecucion de connect (que al parecer es una función)
# y que recibe como argumentos lo necesario para conectarse a la base de datos
#la base de datos en este caso se llama store

arguments = {
  'db': DATABASE_NAME,
  'host': 'localhost',
  'port': 27017
}

db_client = connect(**arguments)

# Document: es una clase que sale de mongoEngine y provee 
# las caracteristicas y funcionalidades necesarias para 
# que los objetos puedan interactuar con la base de datos.
# por ejemplo .save(), .object estarán disponibles en cada 
# instancia de Stock

# Stock representa una colección en mongodb
# cada instancia de Stock representa a cada documento
# la clase Stock hereda la funcionalidad de Document,
# por ejemplo: .save, object...
class Stock(Document):
   name = StringField(required=True)
   price = DecimalField(required=True)
   description = StringField(required=False)
   def __str__(self):
     return f'{self.id} {self.name} -> ${self.price} | {self.description}'

def create(name, price, description):
  new_document = Stock(description, price, name)
  new_document.save()
  print(new_document)

def read_all():
  for document in Stock.objects:
    print(document)

def read_one(name):
  try:
    document = Stock.objects(name=name)[0]
    print(document)  
  except IndexError as error:
    print(f"Ups! the item {name} was not found")

  # Actualizar documentos recibiendo el nombre
def update(name):
  try:
    document = Stock.objects(name=name)[0]
    field_name = input("Which field do u want to update: name, price, description? ")
    value = input('what\'s the value? ')

    data_to_update = dict()
    data_to_update[field_name] = value
    document.update(**data_to_update)
    document.reload()
    print(document)
  except IndexError:
    print(f'ups! I can\'t find the document with name: {name}')

def delete(name):
  try:
    document = Stock.objects(name=name)[0]

    entity_to_delete = input("What do you want to delete, \n[d]escription, \n[w] whole document?, \n[e]mpty database ")

    if entity_to_delete == 'w':
      document.delete()
    elif entity_to_delete == 'd':
      document.update(description=None)
    elif entity_to_delete == 'e':
      db_client.drop_database(DATABASE_NAME)
    else:
      print('you have just two options: [f] or [d]')


  except Exception:
    print(f'ups! I can\'t find the document with name: {name}')

  # Borrar documentos


db_client.close()
