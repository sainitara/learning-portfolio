import openai
from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/prompts", methods=['GET', 'POST'])
def prompts():
    result = ""

    if request.method == "POST":
        input1 = request.form.get("topic")
        input2 = request.form.get("wtype")
        if input2 == "Expository paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Create a writing prompt for an expository paragraph about " + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Expository essay":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Create a writing prompt for an expository essay about " + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Narrative story":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Create a writing prompt for a narrative story about " + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Informational paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Create a writing prompt for an informational paragraph about " + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Informational article":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Create a writing prompt for an informational article about " + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Argumentative paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Create a writing prompt for an argumentative paragraph about " + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Argumentative essay":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Create a writing prompt for an argumentative essay about " + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        result = json.loads(str(result))["choices"][0]["text"]

    return render_template('prompts.html', output=result, loading="")


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    result = ""

    if request.method == "POST":
        input1 = request.form.get("input")
        input2 = request.form.get("type")
        if input2 == "Expository paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Student: Here is my expository paragraph. Can I have feedback on this?" + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Expository essay":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Student: Here is my expository essay. Can I have feedback on this?" + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Narrative story":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Student: Here is my narrative story. Can I have feedback on this?" + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Informational paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Student: Here is my informational paragraph. Can I have feedback on this?" + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Informational article":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Student: Here is my informational article. Can I have feedback on this?" + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Argumentative paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Student: Here is my argumentative paragraph. Can I have feedback on this?" + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Argumentative essay":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Student: Here is my argumentative essay. Can I have feedback on this?" + input1 + "\nTeacher: Here is my lengthy response:",
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        result = json.loads(str(result))["choices"][0]["text"]


    return render_template('feedback.html', loading="", output=result)


@app.route('/write')
def write():
    return render_template('write.html', )


if __name__ == '__main__':
    app.run()
