# Import the "time" module to handle time-related operations
import time

# Import the "Flask" class and other functions from "flask" to create a web application
from flask import Flask, render_template, request

# Import functions from custom Python files ("question_answering.py" and "privateGPT.py")
from question_answering import your_question_answering_function, get_qa_model
from privateGPT import main

# Initialize an instance of the Flask application
app = Flask(__name__)

# Define the root route of the application
@app.route("/")
def index():
    # Return the content of the "index.html" template when this route is accessed
    return render_template('index.html')

# Define another route to handle GET and POST requests
@app.route("/get", methods=["GET", "POST"])
def chat():
    # Retrieve the content of the "msg" form field sent via the POST request
    msg = request.form["msg"]
    
    # Store the content in an "input" variable
    input = msg
    
    # Call the "main" function from the "privateGPT" module with "input" as an argument and return the response
    return main(input)

# Execute the application only if this file is run directly (and not imported as a module)
if __name__ == '__main__':
    # Launch the application in debug mode
    app.run(debug=True)
