from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>CP Roaster is running!</h1>"

@app.route("/roast", methods=["POST"])
def roast():
    return jsonify({"message": "roast coming soon"})

if __name__ == "__main__":
    app.run(debug=True)