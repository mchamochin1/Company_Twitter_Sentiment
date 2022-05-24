from flask import Flask, jsonify, request
import json

from functions import predictSentiment


app = Flask(__name__)
#app.config["DEBUG"] = True

# 1. Test endpoint to check if it is up & running
@app.route('/', methods=['GET'])
def home():
    return "<h1>Deployment of the Sentiment Prediction Model</h1><p>This site is a prototype API for sentiment analysis of tweets.</p>"

# 2.Endpoint to get a sentiment by providing a tweet_text as parameter in the call
# http://127.0.0.1:5000/api/v0/sentiment/tweet_text?text=''
@app.route('/api/v0/sentiment/tweet_text', methods=['GET'])
def tweet_text():
    results = []
    if 'text' in request.args:
        aux_text = str(request.args['text'])

        df = predictSentiment(aux_text)

        data_set = {'Polarity' : df['Polarity'].item(), 
                    'Polarity_Pos' : df['Polarity_Pos'].item(), 
                    'Polarity_Neg' : df['Polarity_Neg'].item()}

        json_data = json.dumps(data_set)
        return jsonify(json_data)
    else:
        return "No text field provided"

app.run()