# -*- coding: utf-8 -*-

# https://medium.com/inside-machine-learning/what-is-a-transformer-d07dd1fbec04
# https://medium.com/datadriveninvestor/deploy-machine-learning-model-in-google-cloud-using-cloud-run-6ced8ba52aac
# https://medium.com/huggingface/distilbert-8cf3380435b5
import os
import json
import flask
import logging
from generate import generate
from flask_cors import CORS, cross_origin


app = flask.Flask(__name__)
CORS(app)
app.config['PROPAGATE_EXCEPTIONS'] = True

# Logs
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s :: %(levelname)s :: %(message)s')


# Load Environment Variables
HOST = os.environ.get('HOST', 'http://localhost')
PORT = os.environ.get('PORT', 8080)
ROUTE_GENERATE = os.environ.get('PORT', 'generate')
N_TOKENS = int(os.environ.get('N_TOKENS', 20))

# This create a json file with the environment variables for javascript script
data_env = {
    "APP_URL": "{}:{}".format(HOST, PORT) if 'localhost' in HOST
    else "{}".format(HOST),
    "ROUTE": "/{}".format(ROUTE_GENERATE),
}

# Save env.json file
with open(os.path.join("./static", "env.json"), 'w') as f:
    json.dump(data_env, f)


@app.route('/')
@cross_origin()
def index():
    """
    Function to render the html file

    :return:
    """

    return flask.render_template('main.html')


@app.route('/generate', methods=['POST'])
@cross_origin()
def prediction():
    """
    Function to receive an user query and return generated text

    :return: Generated text
    """

    income_query = json.loads(flask.request.data)['input']

    logging.info('Query received: {}'.format(income_query))

    res = generate(income_query, size=N_TOKENS)
    generated = res.split(income_query)[-1]

    logging.info('Result: {}'.format(res))

    return flask.jsonify({
        'version': 'v1.0.0',
        'body': {'query': income_query,
                 'generated': generated,
                 'result': res}
        }), 200


@app.route('/health_liveness')
@cross_origin()
def health_check():
    """
    Check status code

    :return:
    """

    return flask.jsonify({'status': 'success'}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=PORT)
