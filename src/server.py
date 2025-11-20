from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    class page:
        title = "Home"
    return render_template('index.html', page=page)

def run():
    app.run(debug=True, port=1787)

if __name__ == '__main__':
    run()