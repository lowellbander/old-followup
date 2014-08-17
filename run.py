from flask import Flask, render_template, request
import unirest
import settings

app = Flask(__name__)
app.debug = True

def get(famID):
    response = unirest.get(settings.API_URL + 'tour/' + famID)
    return response.body

@app.route('/')
def index():
    data = {'id': request.args.get('id')}
    data['name'] = get(data['id'])['name']
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
