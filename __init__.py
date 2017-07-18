from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    amap_key = '15c70ee1f164cc08cdb4883bed9f3dd7'
    return render_template('index.html', **locals())


@app.route('/table_upload', methods=['POST'])
def table_upload():
    import pandas as pd
    df = pd.read_csv(request.files['file'], header=0)
    data = dict()
    data['table'] = df.iloc[:, [0, 1, 4]].to_html(classes='el-table', border=0, index=False)
    data['json'] = df.to_dict(orient='records')
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
