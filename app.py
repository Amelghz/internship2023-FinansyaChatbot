import time
from flask import Flask, render_template, request
from question_answering import your_question_answering_function, get_qa_model
from privateGPT import main

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    
    msg = request.form["msg"]
    input = msg
    return main(input)

if __name__ == '__main__':
    app.run(debug=True)