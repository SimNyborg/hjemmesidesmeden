from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

current_year = date.today().year

@app.route('/')
def homepage():
    return render_template('index.html', year=current_year)

@app.route('/kontakt')
def contact():
    return render_template('contact.html', year=current_year)

@app.route('/om')
def about_us():
    return render_template('about.html', year=current_year)

@app.route('/portefølje')
def portfolio():
    return render_template('portfolio.html', year=current_year)

@app.route('/priser')
def prices():
    return render_template('pricing.html', year=current_year)

if __name__ == "__main__":
    #run app in debug mode to auto-reload
    app.run(debug=True)

