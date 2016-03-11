import cPickle as pickle
import random
import string
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


# index route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = str(request.form.get('url'))  # get url from POSTed form data

        with open('url_list.p') as f:
            url_list = pickle.load(f)  # list of (url, hash) tuples

        # Handle POSTed URLs that have been shortened previously
        for item in url_list:
            if url == item[0]:
                shortened_url = 'localhost:5000/%s' % item[1]
                return redirect(url_for('shortened', url=shortened_url))

        # handle new URLs to be shortened
        letters = string.ascii_letters + string.digits  # a-Z + 0-9
        # create random hash of 7 chars length from letters
        url_hash = ''.join(random.SystemRandom().choice(letters) for n in range(7))
        # add new URL and associated hash to url_list as tuple
        url_list.append((url, url_hash))

        # repickle url_list
        with open('url_list.p', 'w') as f:
            pickle.dump(url_list, f)

        # redirect to shortened page displaying shortened URL
        # shortened URL passed as query param
        shortened_url = 'localhost:5000/%s' % url_hash
        return redirect(url_for('shortened', url=shortened_url))

    else:
        # get request, renders form for submitting url to shorten
        return render_template('index.html')


# route for shortened url display page
@app.route('/shortened/')
def shortened():
    url = request.args.get('url')
    return render_template('shortened.html', url=url)


# route for redirect shortened urls to full url
@app.route('/<hash>/')
def redirect_url(hash):
    with open('url_list.p') as f:
        url_list = pickle.load(f)
    for item in url_list:
        if hash == item[1]:
            return redirect(item[0])
    return "No URL exists"


if __name__ == '__main__':
    app.run(debug=True)
