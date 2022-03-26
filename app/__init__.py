from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='../front-end/build', static_url_path='')


@app.errorhandler(404)
def serve(e):
    return send_from_directory(app.static_folder, 'index.html')


from app import functions
from app import views
