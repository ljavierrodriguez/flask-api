from flask import Flask, render_template
from flask_script import Manager
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

manager = Manager(app)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()

