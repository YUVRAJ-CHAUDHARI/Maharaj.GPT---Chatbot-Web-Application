from flask import Flask, render_template, request, jsonify

from flask_pymongo import PyMongo

import openai

openai.api_key = "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"


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://yuvrajchaudhari11111:zUjLG7IVOxUwRnOH@cluster0.on8hd.mongodb.net/chatgpt"
mongo = PyMongo(app)

app = Flask(__name__)

@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(mychats)
    return render_template("index.html", context={"mychats": mychats})




@app.route("/api", methods=['GET', 'POST'])
def QA():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"question": question, "answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
           response = openai.completions.create(
                model="gpt-4o-mini",
                messages=[],
                response_format={
                    "type": "text"
                },
                temperature=1,
                max_completion_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
        print(response)
        data = {"question": question, "answer": response["choices"][0]["text"]}
        mongo.db.chats.insert_one({"question": question, "answer": response["choices"][0]["text"]})
        return jsonify(data)

    # Default response if POST method fails
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)

  

app.run(debug=True, port=5000)