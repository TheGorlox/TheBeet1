from flask import Flask, render_template

app = Flask(__name__)



# @ signifies a decorator -way to wrap a function and modigying its behavior
@app.route('/<user>/home')
@app.route("/")
def index(user=None):
    return render_template('home.html')
@app.route('/<user>/article')
@app.route('/article')
def article(user=None):
    #Outputs
    classifier="hate"
    username="Username"
    headline="Headline"
    credibility=80
    bias=58
    blank=11
    return render_template('article.html', classifier=classifier, credibility=credibility, bias=bias, blank=blank, headline=headline, user=user, username=username)

@app.route('/<user>/history')
def history(user=None):
    credibility = 80
    return render_template('_history.html', credibility=credibility)

if __name__ == "__main__":
    app.run(debug=True)