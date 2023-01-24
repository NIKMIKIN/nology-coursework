from flask import Flask, request
from dotenv import load_dotenv
import os
import psycopg2
from datetime import datetime, timezone
import logging

load_dotenv()


app = Flask(__name__)

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
logging.basicConfig(filename='test.log', level = logging.DEBUG)


CREATE_ENCLOSURE_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (enclosure_id SERIAL PRIMARY KEY, enclosure_name TEXT);"
)

CREATE_ANIMAL_TABLE = (
    "CREATE TABLE IF NOT EXISTS animals (id SERIAL PRIMARY KEY, animal_name TEXT, quantity REAL, enclosure_name TEXT,  enclosure_id INTEGER);"
)

SELECT_ENCLOSURE = (
    "SELECT enclosure_name FROM enclosures where id = %s;"
)

SELECT_ANIMAL = (
    "SELECT animal_name FROM animals where id = %s;"
)
INSERT_ENCLOSURE = "INSERT INTO enclosures (enclosure_name) VALUES (%s) RETURNING id;"

INSERT_ANIMAL = (
    "INSERT INTO animals(animal_name, quantity, enclosure_id) VALUES (%s, %s, %s)"
)

#can pass more than config into create app
def create_app(db_url):
    app = Flask(__name__)
    #app.config.from_object()
    # connection = psycopg2.connect(url)
    # cursor = connection.cursor()
    @app.get("/")
    def home():
        return "Welcome to the Zoo Inventory!"

    @app.get("/api/get_enclosure/<int:enclosure_id>")
    def get_enclosure(enclosure_id):
        #remove withs replace with something else
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ENCLOSURE, (enclosure_id,))
                enclosure = cursor.fetchone()
                
        return f"enclosure id is : {enclosure_id}, enclosure_name refers to {enclosure[0]}", 200


    @app.get("/api/get_animals/<int:id>")
    def get_animals(id):
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ANIMAL, (id,))
                animals = cursor.fetchone()

        return f"animal id is: {id}, refers to {animals}", 200


    @app.post("/api/enclosure")
    def create_room():
        data = request.get_json()
        enclosure_name = data["enclosure_name"]
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_ENCLOSURE_TABLE)
                cursor.execute(INSERT_ENCLOSURE, (enclosure_name,))
                room_id = cursor.fetchone()[0]
                logging.info(INSERT_ENCLOSURE)
                print(INSERT_ENCLOSURE)
                
        
        return {"id": room_id, "message": f"Room {enclosure_name} created"}, 201

    @app.post("/api/animal")#<int:enclosure_name>
    def add_animal():
        data = request.get_json()
        # id = data["id"]
        animal_name = data["animal_name"]
        quantity = data["quantity"]
        # enclosure_name = data["enclosure_name"]
        enclosure_id = data["enclosure_id"]
        
        # try:
        #     date = datetime.strptime(data["data"], "%m-%d-%Y %H:%M:%S")
        # except KeyError:
        #     date = datetime.now(timezone.utc)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_ANIMAL_TABLE)
                # enclosure_name = cursor.execute(SELECT_ENCLOSURE, (enclosure_id))
                cursor.execute(INSERT_ANIMAL, ( animal_name, quantity, enclosure_id))
                #enclosure_id = cursor.fetchone()[0]
                logging.info(INSERT_ANIMAL)
                return {f"message": f"{animal_name} added."}, 201    
    return app

app = create_app(connection)