from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "nothing here, yet"

if __name__ == '__main__':
    app.run()
