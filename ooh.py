import openai
from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]


@app.route('/', methods=['GET', 'POST'])
def main():
    result = ""

    if request.method == "POST":
        input1 = request.form.get("input")
        input2 = request.form.get("type")
        if input2 == "Expository paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Give suggestions to improve this expository paragraph" + input1,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Expository essay":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Give suggestions to improve this expository essay" + input1,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Narrative story":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Give suggestions to improve this narrative story" + input1,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Informational paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Give suggestions to improve this informational paragraph" + input1,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Informational article":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Give suggestions to improve this informational article" + input1,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Argumentative paragraph":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Give suggestions to improve this argumentative paragraph" + input1,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        elif input2 == "Argumentative essay":
            result = openai.Completion.create(
                model="text-davinci-002",
                prompt="Give suggestions to improve this argumentative essay" + input1,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=2
            )
        result = json.loads(str(result))["choices"][0]["text"]

    return render_template('template.html', loading="", output=result)


if __name__ == '__main__':
    app.run()
