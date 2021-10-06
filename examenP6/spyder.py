import psycopg2 as pc
conexion= pc.connect(user="postgres", password="97Aguilar24",host="127.0.0.1", port="5432",database="mibasejhoselin")
 
cursor = conexion.cursor()


cursor.execute("INSERT INTO estudiante (ci, nombre, fechan, departamento) VALUES ('151515', ' Aguilar', '1996-10-28', 'SC')");

conexion.commit()
print("Record inserted successfully")
conexion.close()