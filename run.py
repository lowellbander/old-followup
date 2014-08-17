from flask import Flask, render_template, request
import unirest
import settings

app = Flask(__name__)
app.debug = True

def get(famID):
    if famID is not None:
        response = unirest.get(settings.API_URL + 'tour/' + famID)
        return response.body
    else:
        return None

@app.route('/')
def index():
    data = {'id': request.args.get('id')}
    try:
        data['name'] = get(data['id'])['name']
        return render_template('index.html', data=data)
    except TypeError:
        return "No ID in URL."

if __name__ == '__main__':
    app.run()
