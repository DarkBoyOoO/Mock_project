import os
from inference import process
from lipsync.inference import get_config
from flask import Flask, render_template, request, send_file
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'data'),
    # Flask-Dropzone config:
    DROPZONE_MAX_FILE_SIZE=1024,  # set max size limit to a large number, here is 1024 MB
    DROPZONE_TIMEOUT=5 * 60 * 1000  # set upload timeout to a large number, here is 5 minutes
)

dropzone = Dropzone(app)

@app.route('/', methods=['POST', 'GET'])
def upload():
    global path
    if request.method == 'POST':
        f = request.files.get('file')
        path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
        f.save(path)
    return render_template('index.html')

@app.route('/result',methods = ['POST'])
def result():
    get_config(path)
    process(path)
    return render_template("result.html")

@app.route('/again',methods = ['POST'])
def again():
    os.remove(path)
    os.remove("results/result.avi")
    os.remove("results/result_voice.mp4")
    os.remove("results/result.wav")
    return render_template("index.html")

@app.route('/<audio_file_name>')
def returnAudioFile(audio_file_name):
    if audio_file_name=='result.wav':
        path_to_audio_file = "results/" + audio_file_name
        return send_file(
         path_to_audio_file,
         mimetype="audio/wav")
    else:
        path_to_audio_file = path
        return send_file(
            path_to_audio_file,
            mimetype="audio/wav")

if __name__ == '__main__':
    app.run(debug=True)
