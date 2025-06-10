from flask import Flask, request, jsonify
from flask_cors import CORS
# import mysql.connector

# app = Flask(__name__)
# CORS(app, origins=["https://e-commerce-beige-beta.vercel.app"], supports_credentials=True)

# # ✅ MySQL Connection Function
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Root@123",  # apna password yahan likho
#         database="users"    # apna DB naam yahan likho
#     )



import mysql.connector

db = mysql.connector.connect(
    host="crossover.proxy.rlwy.net",
    user="root",
    password="CfhjiuQPraDsuNKOfUMAasRwfHnwYfXX",
    port=33688,
    database="railway"
)


@app.route("/")
def home():
    return "Flask backend is running!"

# ✅ Insert API
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    password = data['password']
    address = data['address']


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, phone,password, address) VALUES (%s, %s, %s, %s, %s)", (name, email, phone,password, address))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "You added successfully"})


# ✅ Insert API
@app.route('/contacted_users', methods=['POST'])
def contacted_users():
    data = request.get_json()
    email = data['email']
    password = data['password']
    msg = data['msg']


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacted_users ( email, password, msg) VALUES (%s, %s, %s)", ( email, password, msg))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "You added successfully"})


# ✅ Fetch API
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(users)

# ✅ Server Run
if __name__ == '__main__':
    app.run(debug=True)
