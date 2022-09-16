from flask import Flask
import json , mysql.connector
from mysql.connector import pooling
app = Flask(__name__)

# User only have SELECT Privileges
read_config = { 'user' : 'dbUserRead', 'password' : '!dbUserRead1' }

# User only have UPDATE Privileges 
# if using WHERE condition MUST have SELECT Privilege also
create_config = { 'user' : 'dbUserCreate' , 'password' : '!dbUserCreate1'}

# User only have INSERT Privileges 
update_config = { 'user' : 'dbUserUpdate' , 'password' : '!dbUserUpdate1' }

# User only have DELETE Privileges
# if using WHERE condition MUST have SELECT Privilege also
delete_config = { 'user' : 'dbUserDelete' , 'password' : '!dbUserDelete1'}

config = {
  'pool_name' : "mypool",
  'pool_size' : 4,
  'pool_reset_session' : True,
  'auth_plugin' : 'mysql_native_password',
  'host' : 'localhost',
  'port' : '3306',
  'database' : 'pooling'
}

@app.route("/create")
def create() :
  
  try:
    pool=mysql.connector.pooling.MySQLConnectionPool(**config , **create_config )
    connection = pool.get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users values( 4 , 'Mohamed')") 
    connection.commit()
    connection.close()

    return json.dumps(True) 

  except Exception as e:
    print(e)

@app.route("/read")
def read() :

  try:
    pool=mysql.connector.pooling.MySQLConnectionPool(**config , **read_config)
    connection = pool.get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * from users")
    data = cursor.fetchall()

    return json.dumps(data)

  except Exception as e:
    print(e)

@app.route("/update")
def update() :

  try:
    pool=mysql.connector.pooling.MySQLConnectionPool(**config , **update_config)
    connection = pool.get_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET name = 'test' WHERE id = 4 ") 
    connection.commit()
    connection.close()

    return json.dumps(True) 

  except Exception as e:
    print(e)

@app.route("/delete")
def delete() :

  try:
    pool=mysql.connector.pooling.MySQLConnectionPool(**config , **delete_config)
    connection = pool.get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users ORDER BY id DESC LIMIT 1 ") 
    connection.commit()
    connection.close()
    
    return json.dumps(True) 

  except Exception as e:
    print(e)


if __name__ == "__main__":
  app.run(debug=True) 



