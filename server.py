import openai
from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]
grade_trends=None
feedback_trends=None
subject = "Math"

@app.route("/", methods=['GET', 'POST'])
def index():
    global subject
    if request.method == "POST":
        subject = request.form.get("wtype")
    print(subject)
    return render_template("index.html")


@app.route("/trends", methods=['GET', 'POST'])
def trends():
    global grade_trends
    global feedback_trends
    global subject
    result = ""
    feedback_trends=""
    grade_trends=""
    if request.method == "POST":
        topic1 = request.form.get("topic1")
        topic2 = request.form.get("topic2")
        topic3 = request.form.get("topic3")
        topic4 = request.form.get("topic4")
        topic5 = request.form.get("topic5")
        grade1 = request.form.get("grade1")
        grade2 = request.form.get("grade2")
        grade3 = request.form.get("grade3")
        grade4 = request.form.get("grade4")
        grade5 = request.form.get("grade5")
        feedback1 = request.form.get("feedback1")
        feedback2 = request.form.get("feedback2")
        feedback3 = request.form.get("feedback3")
        feedback4 = request.form.get("feedback4")
        feedback5 = request.form.get("feedback5")
        grade_trends = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant."
                },
                {
                "role": "user",
                "content": "What are some numerical patterns you notice in my " + subject + "assignment grades, with grades of "
            + grade1 + "in " + topic1 + ", " + grade2 + "in " + topic2 + ", " + grade3 + "in " + topic3 + ", " + grade4 + "in " + topic4 + ", and"
            + grade5 + "in " + topic5 + "?"
                }
            ],
            temperature=0.5,
            max_tokens=800,
            top_p=1,
            frequency_penalty=2,
            presence_penalty=2
        )
        grade_trends = json.loads(str(grade_trends))["choices"][0]["message"]["content"]

        feedback_trends = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant."
                },
                {
                "role": "user",
                "content": "What are some patterns you notice in my " + subject + "assignment feedback, with feedback of "
            + feedback1 + "in " + topic1 + ", " + feedback2 + "in " + topic2 + ", " + feedback3 + "in " + topic3 + ", "
            + feedback4 + "in " + topic4 + ", and" + feedback5 + "in " + topic5 + "?"
                }
            ],
            temperature=0.5,
            max_tokens=800,
            top_p=1,
            frequency_penalty=2,
            presence_penalty=2
        )
        feedback_trends = json.loads(str(feedback_trends))["choices"][0]["message"]["content"]

    return render_template('trends.html', feedback_trends=feedback_trends, grade_trends=grade_trends)


@app.route('/plans', methods=['GET', 'POST'])
def plans():
    global feedback_trends
    global grade_trends
    result = ""
    plans = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant."
                },
                {
                "role": "user",
                "content": "What are some plans I can follow to improve my grades? My teacher told me " + grade_trends + "and " + feedback_trends + "."
                }
            ],
            temperature=0.1,
            max_tokens=800,
            top_p=1,
            frequency_penalty=2,
            presence_penalty=2
        )
    plans = json.loads(str(plans))["choices"][0]["message"]["content"]

    return render_template('plans.html', plans = plans)


if __name__ == '__main__':
    app.run()
