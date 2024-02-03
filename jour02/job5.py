import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="magaev",
    database="LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute(
    "SELECT superficie FROM etage")
results = cursor.fetchall()
superficieTotal = 0
print(results)
for i in results:
    superficieTotal += i[0]
    print(superficieTotal)
print(f"la superficie de la plateforme est de {superficieTotal}")

cursor.close()
mydb.close()
