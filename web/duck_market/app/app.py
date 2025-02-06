from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

DUCKS = {
    'rubber': {
        'id': 'rubber',
        'name': 'Rubber Duck',
        'image': 'rubber.png',
        'description': 'Classic yellow rubber duck, perfect for debugging!'
    },
    'mallard': {
        'id': 'mallard',
        'name': 'Mallard Duck',
        'image': 'mallard.png',
        'description': 'A majestic mallard duck with beautiful green feathers.'
    },
    'wood': {
        'id': 'wood',
        'name': 'Wood Duck',
        'image': 'wood.png',
        'description': 'Elegant wood duck with stunning colorful plumage.'
    }
}

@app.route("/")
def main():
    return render_template("index.html", ducks=DUCKS)

@app.route("/duck/<duck_id>")
def view_duck(duck_id):
    if duck_id in DUCKS:
        return render_template("duck.html", duck=DUCKS[duck_id])
    return "Duck not found!", 404

@app.route("/price")
def get_price():
    duck_file = request.args.get('duck')
    try:
        price_path = os.path.join(os.getcwd(), 'prices', duck_file)
        return open(price_path).read()
    except Exception as e:
        return "Error retrieving price!", 404

if __name__ == "__main__":
    app.run(debug=True)