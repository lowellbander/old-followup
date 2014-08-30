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

@app.route('/<fid>', methods=['GET','POST'])
def index(fid):
    #process submission
    first = request.args.get('first')
    second = request.args.get('second')
    third = request.args.get('third')
    if bool(first) or bool(second) or bool(third):
        review = ''
        if bool(first):
            review += "How awesome was your tour guide?\n\n"
            review += first + '\n\n'
        if bool(second):
            review += "Was there anything you would have liked to have heard about, but didn't?\n\n"
            review += second + '\n\n'
        if bool(third):
            review += "Was there anything you could have done without?\n\n"
            review += third
        print review

        params = {'review': review}
        response = unirest.put(os.environ['CLERK_URL'], params=params)
        print response.body

        return "Submitted"

    #serve form
    try:
        data = {'id': fid}
        data['name'] = get(data['id'])['name']
        return render_template('followup.html', data=data)
    except TypeError:
        return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
