from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def rupal():
    name2 = "Rupal"
    return render_template('about.html', name=name2)


@app.route("/bootstrap")
def boot():
    return render_template('bootstrap.html')


@app.route("/health")
def health():
    return render_template('health.html')


app.run(debug=True)