from flask import Flask, request
from dotenv import load_dotenv
import os
import psycopg2
from datetime import datetime,timezone

load_dotenv()


app = Flask(__name__)

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)

SELECT_ROOM = (
    "SELECT name FROM rooms WHERE id = %s;"
)

CREATE_TEMPS_TABLE = (
    "CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"
)

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
INSERT_TEMP = (
    "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
)

GLOBAL_NUMBER_OF_DAYS = (
    "SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;"
)

GLOBAL_AVG = "SELECT AVG(temperature) as average FROM temperatures;"

@app.get("/")
def home():
    return "Hello World!"
    #render_template("intro.htmlfl")
@app.get("/room_id/<int:room_id>")
def room(room_id):
    
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ROOM, (room_id,))
            name = cursor.fetchone()[0]
    
    return f"room id is : {room_id}, refers to {name}", 200

@app.get("/api/average_temperature")
def avg_temp():


    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GLOBAL_NUMBER_OF_DAYS)
            
            average = cursor.fetchone()[0]
            cursor.execute(GLOBAL_AVG)
            days = cursor.fetchone()[0]
    
    return f"average temperature is  {average} global days is {days}", 200


@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
            room_id = cursor.fetchone()[0]
    return {"id": room_id, "message": f"Room {name} created"}, 201

@app.post("/api/temperature")
def add_temp():
    data = request.get_json()
    temperature = data["temperature"]
    room_id = data["room"]

    try:
        date = datetime.strptime(data["data"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TEMPS_TABLE)
            cursor.execute(INSERT_TEMP, (room_id, temperature, date))
    return {"message": "Temperature added."}, 201