from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    msg = request.args.get('msg')
    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": msg})
    
    response = ''
    for i in r.json():
        response += i['text']
    
    print('Bot says:', response)  # Print the bot's response
    
    return response

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
