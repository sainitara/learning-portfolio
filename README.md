# Eduhack

This is our project for the EmP Eduhack hackathon.
## Inspiration

We found that in school writing courses, the structure of learning is that you get a project, you complete it, and then you get a grade. This is usually not conducive to learning because it does not allow the student to get feedback on what to improve along the way. We wanted to make an application that could allow students to receive feedback in real time while they work. This application also allows students to learn by themselves, by getting a prompt, writing off of it, and receiving feedback. This can be used alongside a classroom so that students can learn writing better and also get better grades.


## What it does

Our application consists of 3 parts - a prompt generator, a simple writing editor, and feedback provider. The prompt generator creates writing prompts for any topic and a variety of writing types with AI, the writing editor provides a simple way to write and download your writing, and the feedback provider also uses AI to give feedback to any kind of writing.

## How we built it

We built a web server with Flask and Python, which also handled OpenAI GPT-3 API calls. Our frontend was made with HTML/CSS/JS alongside the Bulma framework.

## Challenges we ran into

The UI design required lots of perseverance getting things to size correctly and be responsive on many different devices. Also, it took a very long time to figure out the prompts and the API calls for good quality feedback and prompt generations using GPT-3 endpoints.

## Accomplishments that we're proud of

We are proud that we were able to make a good looking UI along with a functional backend. We are also proud of calibrating the AI model and getting great completions for our feedback and prompt generation.

## What we learned

We learned a lot about UI design and Flask programming, along with how to best use the hugely powerful GPT-3 model to the best of its functionality.

## What's next for EssayWay

We plan to add a better text editor that can save within browser, and possibly tools to help teacher with their classroom using this application.
