from flask import Flask, render_template

app = Flask(__name__)



# @ signifies a decorator -way to wrap a function and modigying its behavior
@app.route("/")
def index():
    return render_template('home.html')
@app.route('/article')
def article():
    #Outputs
    headline="Headline"
    credibility=80
    bias=58
    blank=11
    return render_template('article.html', credibility=credibility, bias=bias, blank=blank, headline=headline)

if __name__ == "__main__":
    app.run(debug=True)