from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renderiza el archivo HTML 'index.html'

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple web page created with Flask.</p>"

if __name__ == '__main__':
    app.run(debug=True)