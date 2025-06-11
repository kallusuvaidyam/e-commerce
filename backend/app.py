from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, origins=["https://e-commerce-beige-beta.vercel.app"], supports_credentials=True)

# ✅ MySQL Connection Function
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Root@123",  # apna password yahan likho
#         database="users"    # apna DB naam yahan likho
#     )




# Railway ke Public credentials
app.config['MYSQL_HOST'] = 'shinkansen.proxy.rlwy.net'
app.config['MYSQL_PORT'] = 36432
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ZEikXboxKPEqFajAykfZZfToWRUnujgx'
app.config['MYSQL_DB'] = 'railway'


@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    tables = cur.fetchall()
    return jsonify(tables)


# ✅ Insert API
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    password = data['password']
    address = data['address']

    print(name, email, phone, password, address, "===========================================")

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
