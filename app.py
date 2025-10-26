import time
import pymysql
from flask import Flask

app = Flask(__name__)

def connect_db():
    retries = 5
    while retries > 0:
        try:
            db = pymysql.connect(
                host="mydb",
                user="root",
                password="my-secret-pw",
                database="mysql"
            )
            return db
        except pymysql.OperationalError:
            retries -= 1
            time.sleep(3)  # wait 3 seconds before retrying
    raise Exception("Could not connect to MySQL after multiple retries")

@app.route('/')
def hello_world():
    db = connect_db()
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    db.close()
    return f'Hello, World! MySQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
