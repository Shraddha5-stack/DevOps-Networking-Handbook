from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running",
        "service": "Python Flask"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "backend"
    })

@app.route("/db")
def database():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "database"),
            user=os.getenv("DB_USER", "appuser"),
            password=os.getenv("DB_PASSWORD", "apppassword"),
            database=os.getenv("DB_NAME", "appdb")
        )

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return jsonify({
            "status": "connected",
            "database": "MySQL",
            "version": version
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
