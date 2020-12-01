from flask import Flask, render_template
from flask_script import Manager
from models import db
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(environ.get("DBUSER"), environ.get("DBPASS"), environ.get("DBHOST"), environ.get("DBNAME"))
manager = Manager(app)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()

'''

Si se establece en True, Flask-SQLAlchemy rastreará las modificaciones de los objetos y emitirá señales. 
El valor predeterminado es None, que habilita el seguimiento, pero emite una advertencia de que se 
deshabilitará de manera predeterminada en el futuro. Esto requiere memoria adicional y debe desactivarse 
si no es necesario.

'''
