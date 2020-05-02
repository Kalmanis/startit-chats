from flask import Flask, render_template, request


app = Flask('app')


@app.route('/')
def index_page():
  return render_template ('BioM.html')


if __name__ == '__main__':
  
app.run(threaded=True, port=5000)