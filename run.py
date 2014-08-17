from flask import Flask, render_template, request
import os
import unirest

app = Flask(__name__)
app.debug = True

def get(famID):
<<<<<<< HEAD
    try:
        response = unirest.get(os.environ['CLERK_URL'] + 'tour/' + famID)
        return response.body
    except TypeError:
=======
    if famID is not None:
        response = unirest.get(settings.API_URL + 'tour/' + famID)
        return response.body
    else:
>>>>>>> FETCH_HEAD
        return None

@app.route('/')
def index():
<<<<<<< HEAD
    try:
        data = {'id': request.args.get('id')}
        data['name'] = get(data['id'])['name']
        return render_template('index.html', data=data)
    except TypeError:
        return "Error. Probably no ID in URL."
=======
    data = {'id': request.args.get('id')}
    try:
        data['name'] = get(data['id'])['name']
        return render_template('index.html', data=data)
    except TypeError:
        return "No ID in URL."
>>>>>>> FETCH_HEAD

if __name__ == '__main__':
    app.run()
