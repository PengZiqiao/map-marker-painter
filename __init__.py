from flask import Flask, render_template, jsonify, request, redirect, url_for

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


@app.route('/download_position', methods=['POST'])
def download_position():
    import pandas as pd
    from models import write_pos
    df = pd.read_csv(request.files['file'], header=0)
    df = write_pos(df)
    df.to_csv(f'{app.root_path}\static\output.csv', index=False, encoding='UTF-8')
    return redirect(url_for('static', filename='output.csv'))


if __name__ == '__main__':
    app.run(debug=True)
