from flask import Flask
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="Attendance"
)

mycursor = mydb.cursor()

@app.route("/")
def home():
    
    myTable = "<table style=\"width:500\">\n<tr>\n<th>RFID</th>\n<th>Name</th>\n<th>Time</th>\n</tr>\n"
    
    mycursor.execute("SELECT RFID, Name, Time FROM Students order by Time desc limit 5")
    fetchResult = mycursor.fetchall()
    for row in fetchResult:
        print(row)
        myTable = myTable + "<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>".format(row[0],row[1], row[2])
    
    return myTable

if __name__=='__main__':
    app.run()
