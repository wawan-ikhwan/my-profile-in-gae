from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  image_root_path = 'https://storage.googleapis.com/menjadi-gcloud-engineer.appspot.com/images/'
  return render_template('index.html', image_root_path=image_root_path)

if __name__ == '__main__':
  app.run(host="127.0.0.1", port=8080, debug=True)
