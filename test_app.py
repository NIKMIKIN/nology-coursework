import sys
sys.path.insert(1, './code')
from flask import Flask, request
# import sqlite3
# import requests
import os
import psycopg2
# from datetime import datetime, timezone
import logging
import pytest
from app import create_app, connection


logging.basicConfig(filename='test.log', level = logging.DEBUG)
@pytest.fixture(scope ="session")
def app():
    app = create_app(connection)
    yield app


@pytest.fixture(autouse = True, scope='session')
def setup_database():
    connection = psycopg2.connect("postgres://tbulsqro:aIIHwVCmk89hBztTFsxPTQQRalk5VnRp@kashin.db.elephantsql.com/tbulsqro")
    assert connection is not None
    print("Connection: CONNECTED")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS enclosures_test (id SERIAL PRIMARY KEY, enclosure_name TEXT);")
    sample_enclosure_data = [
        (1,'mammals'),
        (2,'reptiles'),
        (3,'fish'),
    ]
    cursor.executemany("INSERT INTO enclosures_test VALUES (%s, %s);", sample_enclosure_data)
    cursor.execute("SELECT COUNT(*) FROM enclosures_test")
    db_size = cursor.fetchone()[0]

    assert db_size == len(sample_enclosure_data)
    print("enclosures_test: FILLED")
    cursor.execute("CREATE TABLE IF NOT EXISTS animals_test(id SERIAL PRIMARY KEY, animal_name TEXT, quantity REAL, enclosure_name TEXT, enclosure_id INTEGER);")
    sample_animals_data = [
        (1, 'lion', 3, 'mammals', 1),
        (2, 'lizard', 6, 'reptiles', 2),
        (3, 'puffer', 20, 'fish', 3),
    ]

    cursor.executemany("INSERT INTO animals_test VALUES(%s, %s, %s, %s, %s);", sample_animals_data)
    cursor.execute("SELECT COUNT(*) FROM animals_test")
    db_size = cursor.fetchone()[0]

    assert db_size == len(sample_animals_data)
    print("Animals_test table: FILLED")
    yield connection, cursor

#TESTING CONNECTION
def test_connection(setup_database):
    
    connection, cursor = setup_database
    logging.info(setup_database)
    cursor.execute('SELECT COUNT(*) FROM enclosures_test')
    db_size = cursor.fetchone()[0]

    assert db_size == 3
    print("Enclosure_test: CONNECTED ") 

    cursor.execute('SELECT * FROM animals_test')
    assert db_size == 3
    print("Animals_test: CONNECTED")




#TESTING FILES

def test_file_exists():
    logging.info(os.path.exists('./test.log'))
    assert os.path.exists('./test.log')

def test_file_contents():
    with open('./test.log', 'r') as f:
        contents = f.read()
        assert "Testing log" in contents

#TESTING SPECIFIC FUNCTIONALITY/TYPES
@pytest.mark.parametrize("inputs, expected_type", [
    (['mammals', str]),
    ([4], int)
])
def test_animal_types(inputs, expected_type):
    assert inputs, expected_type

#TESTING DUMMY DATA BY PARAMETRIZING
@pytest.mark.parametrize("inputs, expected_output",[
    ([1, 'mammals'], 1),
    ([2, 'reptiles'], 2),
    ([3, 'fish'], 3),
])
def test_enclosure_insert(inputs, expected_output):
    print("\n Insert Iteration - Test Start")
    assert inputs, expected_output

@pytest.mark.parametrize("inputs, expected_output",[
    ([1, 'lion', 3, 'mammals', 1], 1),
    ([2, 'lizard', 6, 'reptiles', 2], 2),
    ([3, 'puffer', 20, 'fish', 3], 3),
    ([4, 'humans', 1, 'mammals', 1], 1),
])
def test_animals_insert(inputs, expected_output):
    print("\n Insert Iteration - Test Start")
    assert inputs, expected_output







    # @pytest.mark.parametrize("inputs, expected_output",[
    # ([1, 'mammals'], 1),
    # ([2, 'reptiles'], 2),
    # ([3, 'fish'], 3),
    # ])
    # def test_insert(inputs, expected_output, connection):
    #     cursor = connection.cursor()
    #     cursor.execute("CREATE TABLE IF NOT EXISTS enclosures_test (id SERIAL PRIMARY KEY, enclosure_name TEXT);")
    #     cursor.executemany("INSERT INTO enclosures_test VALUES (%s, %s);", inputs)
    #     print("\n Insert Iteration - Test Start")
    #     assert inputs, expected_output


    #app = Flask(__name__)
    #make logic and send database through create_app
    # app.config.update({
    #     "Testing": True,
    # })

    
    # client = app.test_client()
    # url = '/'

    # response = client.get(url)
    # assert response.get_data() == b'Hello, World!'
    # assert response.status_code == 200


    # other setup can go here






# @pytest.mark.parametrize("inputs, expected_output",[
#     ([1, 'mammals'], 1),
#     ([2, 'reptiles'], 2),
#     ([3, 'fish'], 3),
#     ])
# def test_insert(inputs, expected_output):
    
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS enclosures_test (id SERIAL PRIMARY KEY, enclosure_name TEXT);")
#     cursor.executemany("INSERT INTO enclosures_test VALUES (%s, %s);", inputs)
#     print("\n Insert Iteration - Test Start")
#     assert (inputs, expected_output) 
    # clean up / reset resources here
# @pytest.fixture()
# def client(app):
#     yield app.test_client()

# def test_json_data(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"Welcome to the Zoo Inventory!"}