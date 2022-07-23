import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
mycursor = mydb.cursor()

########### Select data from all databases ###############

def querytest():
    sql = ("""SELECT * FROM persons""")
    mycursor.execute(sql)
    count = mycursor.fetchall()
    countrow = mycursor.rowcount
    print(countrow)
    return count

########### INSERT data into database ###############

# def querytest():
#     sql = (""" INSERT INTO persons (id, name, color, phone) VALUES ('3', 'chain555', 'chain5555555', '1111');
#     """)
#     mycursor.execute(sql)
#     mydb.commit()
#     count = mycursor.rowcount
#     return count
