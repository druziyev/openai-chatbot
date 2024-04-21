from flask import Flask, render_template, request
from utils import chatbot


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        response = chatbot.chat(message)
        response = response.splitlines(keepends=True)
        result = {
            'response': response,
        }

        return render_template('index.html', result=result)

    return render_template('index.html')



if __name__ == "__main__":
    app.run()