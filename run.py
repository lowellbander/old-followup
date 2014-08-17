from flask import Flask, render_template, request
import os
import unirest

app = Flask(__name__)
app.debug = True

def get(famID):
    try:
        response = unirest.get(os.environ['CLERK_URL'] + 'tour/' + famID)
        return response.body
    except TypeError:
        return None

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return "Submitted!"
    try:
        data = {'id': request.args.get('id')}
        data['name'] = get(data['id'])['name']
        return render_template('index.html', data=data)
    except TypeError:
        return "Error. Probably no ID in URL."

if __name__ == '__main__':
    app.run()
