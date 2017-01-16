from pymongo import MongoClient
from flask import Flask, render_template, request

client = MongoClient('localhost', 27017)
db = client.test_database
app = Flask(__name__)

@app.route("/")
def hello():
    return "Olar"

@app.route("/add", methods=['GET', 'POST'])
def person_form():
    if request.method == 'POST':
            add_person( request.form['name'],
                        request.form['email'],
                        request.form['topics'])
    return render_template('form.html')

@app.route('/list')
@app.route('/list/<topic>')
def list_persons(topic=None):
    posts = db.posts
    persons = posts.find({"topics": topic}) if topic else posts.find()
    return render_template('list.html',
                            persons=persons,
                            topic=topic)

def list_persons_by_topic():
    posts = db.posts
    return render_template('list.html', persons=posts.find(), topic=request.form['topic'])

def add_person(name, email, topics):
    posts = db.posts
    topics_list = topics.split(",")
    formatted_topics_list = list(map(str.strip, topics_list))
    post = {"name": name,
            "email": email,
            "topics": formatted_topics_list}
    posts.insert_one(post)

if __name__ == "__main__":
    app.run()
