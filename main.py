from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

posts = [
    {"name": "Василий", "content": "Это Василий"},
    {"name": "Даша", "content": "Это Даша"},
]


@app.route('/')
def index():
    return render_template("list.html", posts=posts)

@app.route('/api/', methods=["POST"])
def get_json():
    data = request.json.get("data")
    print(data)
    return jsonify({"name": "sveta"})


if __name__ == "__main__":
    app.run()
