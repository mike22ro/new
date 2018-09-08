from flask import Flask, render_template  # Need render_template() to render HTML pages

app = Flask(__name__)

@app.route('/')
def main():
   """Render an HTML template and return"""
   return render_template('hello.html')  # HTML file to be placed under sub-directory templates

app.run(port=4995)