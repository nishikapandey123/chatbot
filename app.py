from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import openai
from chatterbot.storage import SQLStorageAdapter
import time
time.clock = time.time
import collections.abc
collections.Hashable = collections.abc.Hashable


app = Flask(__name__)

# Configure ChatterBot and train it on English corpus
chatbot = ChatBot('anna')
chatbot.storage = SQLStorageAdapter(database_uri='sqlite:///database.sqlite3')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Set your OpenAI API key here
openai.api_key = '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'

# Function to generate a response using OpenAI GPT-3.5-turbo model
def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    userText = request.args.get('msg')

    if userText.lower() == "what is your name":
        chatbot_name = "chota bheem"  # Replace with your desired name
        return chatbot_name

    # Create messages for the OpenAI model
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": userText}
    ]

    # Get response from the chatbot or OpenAI model
    if userText.startswith("chatbot:"):
        chatbot_response = str(chatbot.get_response(userText[8:]))
    else:
        chatbot_response = generate_response(messages)

    chatbot_name = "chota bheem"  # Replace 'MyCustomChatBotName' with your desired name
    response = chatbot_name + ": " + chatbot_response
    
    return response

@app.route("/store_info", methods=["POST"])
def store_info():
    userText = request.form.get('msg')  # Access the user input from the form data

    # Store information in the database
    store_information(userText)

    return "Information stored successfully!"

def store_information(info):
    from flask_sqlalchemy import SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:nishika@localhost/chatbot'  # Replace with your MariaDB connection details
    db = SQLAlchemy(app)

    # Define a model for the data
    class ChatBotData(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        information = db.Column(db.String(250))

    # Create a new object and store it in the database
    chatbot_data = ChatBotData(information=info)
    db.session.add(chatbot_data)
    db.session.commit()

@app.route("/get_data", methods=["GET"])
def get_data():
    from flask_sqlalchemy import SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:nishika@localhost/chatbot'  # Replace with your MariaDB connection details
    db = SQLAlchemy(app)

    # Define a model for the data
    class ChatBotData(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        information = db.Column(db.String(250))

    # Fetch data from the database
    data = ChatBotData.query.all()
    data_list = [d.information for d in data]

    # Return data as JSON response
    return jsonify(data_list)

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)
