from mongoengine import connect, Document, StringField, DecimalField
# Mongo server port: 27017

db_client = connect('store', host='localhost', port=27017)

class Stock(Document):
   name = StringField(required=True)
   price = DecimalField(required=True)
   description = StringField(required=False)
   def __str__(self):
     return f'{self.id} {self.name} -> ${self.price} | {self.description}'

def create(name, price, description):
  new_document = Stock(name, price, description).save()
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


  # Borrar documentos


db_client.close()
