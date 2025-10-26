from flask import Flask
import time
import pymysql

app = Flask(__name__)

def connect_db(retries=10, delay=3):
    for i in range(retries):
        try:
            connection = pymysql.connect(
                host='db',
                user='root',
                password='my-secret-pw',
                database='mydb'
            )
            return connection
        except Exception as e:
            print(f"Retrying MySQL connection ({i+1}/{retries})...")
            time.sleep(delay)
    raise Exception("Could not connect to MySQL after multiple retries")

@app.route('/')
def home():
    try:
        conn = connect_db()
        return "Connected to MySQL successfully!"
    except Exception as e:
        return f"Failed to connect to MySQL: {e}"

if __name__ == "__main__":
    # Bind to all network interfaces inside the container
    app.run(host='0.0.0.0', port=5002, debug=True)
