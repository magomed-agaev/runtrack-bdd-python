import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="magaev",
    database="LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute("SELECT capacite FROM salle;")
results = cursor.fetchall()
capacite_total = 0
for i in results:
    capacite_total += i[0]
    print(capacite_total)

print(f"la capacite totale de laplateforme est de {capacite_total}")

cursor.close()
mydb.close()
