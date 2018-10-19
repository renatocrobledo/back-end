# sqlite3 es una libreria que nos ayuda a controlar una base de datos relacional.
# connect es un objeto que se encuentra dentro de sqlite3

from sqlite3 import connect

# connection será nuestro objeto resultante de la ejecucion de connect
# la cuál exije como parámetro el nombre de la base de datos

connection = connect("company.db")

# el cursor será nuestro ayudante en la comunicacion con la base de datos
# se encargará de realizar la traducción de sentencias SQL hacia el motor de la base de datos
cursor = connection.cursor()

# Lo siguiente Sólo funciona para la librería de sqlite3 y lo que hace es habilitar
# la funcionalidad de las relaciones (llaves primarias y foraneas)
# el numero 1 hace referencia a que se van a utilizar llaves foraneas
# por default está en 0 que significa que esa foncionalidad está apagada
cursor.execute("PRAGMA foreign_keys = 1")

# Habilita la posibilidad de retornar el nombe de las columnas
# después de realizar un query, cursor.description contendrá una tupla 
# con esa info, pero hay que extraerla ya que tiene un formato bastante curioso:
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.description
cursor.execute("PRAGMA table_info(table_name);")

# Lo siguiente es un string que representa una sentencia en SQL 
# La cuál define la esctura de una tabla llamada "office"
# con dos campos "id" que va a ser su llave primaria (única e incremental)
# y "name" que contendrá texto de no más de 20 caracteres
sql_command = """
                CREATE TABLE IF NOT EXISTS office(
                  id INTEGER PRIMARY KEY,
                  name VARCHAR(20)
                );
                """
# acá ocurre la ejecución de nuestra sentencia anterior
cursor.execute(sql_command)

# En este punto la tabla debería haberse creado.. :)

# lo siguiente define la vliable : "new_office" con el valor en texto 
# que el usuario introduzca desde la consola  
new_office = input('newv ofice: ')

# re-definimos la variable sql_command, ahora con otrs instrucción
# insertar un registro dentro de la table "office"
# hacemos uso de las F-strings que no es mas que texto
# que contendrá valores dados por variables en tiempo de ejecución:
# https://realpython.com/python-f-strings/
sql_command = f'INSERT INTO office(id, name) VALUES (NULL, "{new_office}");'

# De nuevo usamos al cursor para ejecutar la sentencia anerior
cursor.execute(sql_command)

# Se define ahora una consulta, la cuál retorará todas las columnas con sus respectivos 
# valores de la table office
# el asterisco hace referencia a todas las columnas (en este caso id y name)
# de tal form que la misma consulta se puede definir como: 
# 'SELECT id, name FROM office;'
sql_command = 'SELECT * FROM office;'

cursor.execute(sql_command)

# El resultado de la consulta es igual a la ejecucion del metodo fetchall de nuestro cursor
result = cursor.fetchall()

# cursor.description retorna un objeto iterable podría ser una Tupla o una Lista
# https://librosweb.es/libro/algoritmos_python/capitulo_7.html
# Ese objeto se manda como parámetro a la funcion "map" 
# después de otra función la cual se ejecutará por cada elemento contenido
# en cursor.description, 
# esa funcoin lambda se refiere a una funcion anonima (sin nombre):
# https://recursospython.com/guias-y-manuales/funciones-lambda/
# al finalizar el resultado de map (que será una Tupla) se transorma en una lista
# en otras palabrasesa linea resume lo siguiente:
'''
column_names = []
for element in cursor.description
  column = element[0]
  column_names.append(column)
'''

column_names = list(map(lambda x:x[0], cursor.description))  

# Imprime los nombres de las columnas en pantalla
print(column_names)

# Imprime los valores de nuestra consulta "SELECT"
print(result)

# Aquí los datos se vuelven persistentes, es decir se guardan en "company.db"
connection.commit()

# Se cierra la conexión co la base de datos
connection.close()