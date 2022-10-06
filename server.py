from turtle import onclick
from urllib import response
from flask import Flask, redirect, render_template, url_for, request
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.ejs')


@app.route('/success/<name>')
def success(name):
    name = name.lower()
    if name in data:
        val = data[name]
        return render_template('success_search.ejs', name=val)

    elif len(get_close_matches(name, data.keys(), cutoff=0.8)) > 0:
        match = get_close_matches(name, data.keys())[0]
      #  return render_template('check_word.ejs', temp=match)
        responce = input(
            "Did you mean %s insted? If Yes enter Y else enter N: " % match)
        responce = responce.lower()
        if responce == "y":
            return success(match)
        else:
            return render_template('no_result.ejs', name=name)
    else:
        return render_template('no_result.ejs', name=name)




@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/user_response', methods=['POST', 'GET'])
def user_response():
    if request.method == 'POST':
        re = request.form['re']
        re = re.lower()
        temp = request.form['word']
        if re == 'y':
           return re
        else:
            return re
            return render_template('invalid.ejs')
    else:
         re = request.form['re']
         re = re.lower()
         temp = request.form['word']
         if re == 'y':
           return re
         else:
            return re
        # user = request.args.get('nm')
        # return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
