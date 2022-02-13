from flask import Flask
import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)


def read_string_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


@app.route('/', methods=['GET'])
def show_map():
    json_map = json.loads(read_string_from_file('map.json'))
    # removing points that are further away than 8 meter
    x = [x[0]for x in json_map if x[0] > -800 and x[0] < 800]
    y = [y[1]for y in json_map if y[0] > -800 and y[0] < 800]

    plt.scatter(x, y, s=1)

    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png', dpi=180)
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

    plt.close()

    return html


def start_server(debug=False):
    app.run(debug=debug)


if __name__ == '__main__':
    start_server(debug=True)
