from flask import Blueprint, request, jsonify
import sqlite3
import subprocess

main = Blueprint('main', __name__)

@main.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # SQL Injection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()
    return jsonify({"user": str(user)})

@main.route("/exec")
def execute():
    cmd = request.args.get("cmd")

    # Dangerous subprocess execution
    output = subprocess.check_output(cmd, shell=True)
    return jsonify({"output": output.decode()})

@main.route("/eval")
def run_eval():
    expr = request.args.get("expr")

    # Dangerous use of eval
    try:
        result = eval(expr)
    except Exception as e:
        result = str(e)
    return jsonify({"result": result})
