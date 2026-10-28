from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def task1():
  return (
    """
      <p>Rishabh: POS ( Point of Sale ;);) )</p>
      <p>Daniel: LOL (Laughing of Loud)</p>
      <p>Alan: LMAO (Laughing my ahh off)</p>
    """
  )

@app.route('/ethan')
def ethan():
  return render_template('template.html', message='GGWP')