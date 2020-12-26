from flask import Flask, render_template, url_for, redirect, request
import json
import random

app = Flask(__name__)

@app.route('/')
def home():
    with open('items.json') as file:
        data = json.load(file)
    return render_template('layout.html', data=data)

@app.route('/add_item', methods=["POST", "GET"])
def add_item():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        with open("items.json") as file:
            data = json.load(file)
        lis = []
        for item in data:
            lis.append(item['id'])
        while True:
            id = random.randrange(10000000, 100000000)
            if id not in lis:
                break
        new = {
            "name": title,
            "description" : description,
            "image": image,
            "id": id
        }
        data.append(new)
        with open("items.json", "w") as file:
            json.dump(data, file, indent=4)
        return redirect(url_for("add_item"))
    else:
        return render_template("items.html")

@app.route('/items/<int:id>')
def get_item(id):
    with open("items.json") as file:
        data = json.load(file)
    show_item = {}
    for item in data:
        if item['id'] == id:
            show_item = item
    print(show_item)
    return render_template('item.html', show_item=show_item)
    
if __name__ == '__main__':
    app.run(debug=True)