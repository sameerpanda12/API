from flask import Flask, jsonify,render_template,request
import requests
import time
import datetime

app = Flask(__name__)
# another endpoint
target_api_url = "http://127.0.0.1:5000/advice"

transcripts = [
    {"name": "John", "utterance": "Hello"},
    {"name": "Jane", "utterance": "Hi there" },
]

@app.route('/')
def transcript_posting():
    return render_template('form.html')

@app.route('/submit_transcript', methods=['POST'])
def submit_transcript():
    for x in transcripts:
          name=x['name']
          uterence=x['utterance']
          timestamp=datetime.datetime.now().isoformat()
          n_transcript={"name":name,"utterance":uterence,"timestamp":timestamp}
          requests.post(target_api_url, json=n_transcript)
          time.sleep(3)
    return render_template('form.html')

# another endpoint for test purpose
@app.route('/advice', methods=['POST'])
def advice():
    # print("hello how r u")
    data = request.get_json() 
    print(data)
    return jsonify({"message": "Received the advice data."})


if __name__ == '__main__':
    app.run()
