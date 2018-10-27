from mongoengine import connect, Document, StringField, DecimalField
# Mongo server port: 27017

db_client = connect('store', host='localhost', port=27017)

class Stock(Document):
   name = StringField(required=True)
   price = DecimalField(required=True)
   description = StringField(required=False)

def create(name, price, description):
  new_documment = Stock(name, price, description).save()
  print(new_documment)

db_client.close()
