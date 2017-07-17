from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    amap_key = '15c70ee1f164cc08cdb4883bed9f3dd7'
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
