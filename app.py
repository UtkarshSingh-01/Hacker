from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app) # This allows your HTML files to talk to this Python server

DB_FILE = 'user_database.csv'

# Initialize CSV if it doesn't exist
if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["username", "email", "password"])

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    # Append to CSV
    with open(DB_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['username'], data['email'], data['password']])
    return jsonify({"status": "success", "message": "Recruit Enlisted"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    with open(DB_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['username'] == data['username'] and row['password'] == data['password']:
                return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401

if __name__ == '__main__':
    app.run(port=5000)