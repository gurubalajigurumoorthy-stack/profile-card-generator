from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile", methods=["POST"])
def profile():
    data = request.get_json()

    return jsonify({
        "name": data["name"],
        "bio": data["bio"],
        "image": data["image"]
    })

if __name__ == "__main__":
    app.run(debug=True)