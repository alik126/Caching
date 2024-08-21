from flask import Flask, request, jsonify
from models.user import get_user, add_user

app = Flask(__name__)


@app.route('/user/<username>', methods=['GET'])
def get_user_api(username):
    user = get_user(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/user', methods=['POST'])
def add_user_api():
    data = request.json
    user_id = add_user(data['username'], data['email'], data['age'])
    return jsonify({"message": "User added", "user_id": str(user_id)}), 201


if __name__ == "__main__":
    app.run(debug=True)
