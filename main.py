import psycopg2
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

@app.post("/person")


@app.post("/person")
def create_person(person: Person):
    name = person.name
    age = person.age
    id = person.id

    DB_NAME = "postgres"
    user = os.getenv("user")
    password = os.getenv("password")
    host = "localhost"
    port = "5432"

    try: 
        connection = psycopg2.connect(dbname=DB_NAME, user=user, password=password, host=host, port=port)
        cursor = connection.cursor()
        print("successfully connected")

        query = """
            INSERT INTO people (id, name, age) 
            VALUES(%s, %s, %s);
        """
        d = (id, name, age) 
        cursor.execute(query, d)
        connection.commit()

        print('row added')

    except (Exception, psycopg2.Error) as error:
        print("UNEXPECTED ERROR:", error)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        
        return "operation complete"
