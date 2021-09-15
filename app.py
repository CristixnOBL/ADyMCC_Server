from utilities import get_frame as gf
from config import Config
from flask import Flask, render_template, Response, jsonify
from datetime import datetime
from utilities import inf_data as iD

app = Flask(__name__, template_folder=Config.TEMPLATE_FOLDER, static_folder=Config.STATIC_FOLDER)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/streaming_camara')
def streaming_camara():
    return Response(gf.getFrame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/screen_img")
def screen_img():
    name_img = gf.screen()
    return jsonify({
        "name_img": name_img,
    })

@app.route("/record")
def record():
    state = gf.record()
    return jsonify(state)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/captures')
def captures():
    return render_template("captures.html")

@app.route('/loco-efa')
def locoefa():
    return render_template("loco-efa.html")

@app.route('/memory')
def memory():
    return jsonify(iD.memory())

if __name__ == "__main__":
    app.run(debug=Config.DEBUG, port=Config.PORT, host=Config.HOST)
