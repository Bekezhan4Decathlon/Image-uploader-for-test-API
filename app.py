import re
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests, ast, os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      if 'inputs' not in os.listdir():
            os.makedirs("inputs")
      file.save("inputs/input.webp")
      filename = secure_filename(file.filename)
      req = requests.post('http://127.0.0.1:5000//similar-image', files = {'file':(filename, open("inputs/input.webp", 'rb'))})
      models = ast.literal_eval(req.text)
      models = map(str, models)
      return render_template('content.html', models = models)
   return render_template('upload.html')
			
if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 5000, debug = True)