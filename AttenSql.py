import mysql.connector
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
import time

reader = SimpleMFRC522()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="Attendance"
)

mycursor = mydb.cursor()

try:
    while True:
        mycursor.execute("CREATE TABLE IF NOT EXISTS Students(RFID INT, name TEXT,time datetime)")
        
        print("Please scan card")
        lcd.write_string("Please Scan Card")
        id, text = reader.read()
        print(id)
        print(text)
        lcd.clear()
        lcd.cursor_pos = (1,8)
        lcd.write_string(text)
        time.sleep(2)
        lcd.clear()
        
        
        add = "INSERT INTO Students (RFID, name, time) VALUES (%s,%s,NOW())"
        val = [id, text]
        mycursor.execute(add, val)
        mydb.commit()
        print("Finish scaning")
        
        
finally:
    GPIO.cleanup()
