from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users (replace with a database in production)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_all_users():
    return jsonify(users)

@app.route("/status")
def get_status():
    return jsonify({"status": "OK"})

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if "username" in data:
        username = data["username"]
        users[username] = data
        return f"User {username} added successfully!"
    else:
        return "Invalid data. Please provide a username.", 400

if __name__ == "__main__":
    app.run(debug=True)
