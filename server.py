from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# key database
licenses = {}

# 🧑‍💻 ADMIN PANEL (web UI)
@app.route("/")
def home():
    return render_template("index.html", licenses=licenses)

# 🔑 key yaratmaq
@app.route("/create", methods=["POST"])
def create():
    key = request.form["key"]
    licenses[key] = None
    return ("OK")

# 🔐 aktivasiya
@app.route("/activate", methods=["POST"])
def activate():
    data = request.json
    key = data["key"]
    hwid = data["hwid"]

    if key not in licenses:
        return jsonify({"status": "invalid"})

    if licenses[key] is None:
        licenses[key] = hwid
        return jsonify({"status": "activated"})

    if licenses[key] == hwid:
        return jsonify({"status": "ok"})

    return jsonify({"status": "used"})

app.run(host="0.0.0.0", port=5000)
