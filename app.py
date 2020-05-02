from sklearn.datasets import load_iris
from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    data = [
        {
            'route': '/iris'
        }
    ]
    return jsonify(data)


@app.route('/iris')
def iris():
    model = joblib.load('iris.joblib')
    data = request.get_json() or request.args
    # A list containing a single tuple with values to use in the prediction
    inputs = [(
        data['sepal_length'],
        data['sepal_width'],
        data['petal_length'],
        data['petal_width']
    )]
    predicted_value = model.predict(inputs).astype(float).tolist().pop()
    predicted_label = load_iris()['target_names'][int(predicted_value)]
    print(predicted_label)
    return jsonify(inputs=data, predicted=predicted_label)


if __name__ == "__main__":
    app.run()
