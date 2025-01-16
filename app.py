from flask import (
    Flask,
    render_template,
    redirect,
    request
)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_index():
    
    return render_template('index.html')

@app.route('/log', methods=['GET', 'POST'])
def get_log():
    pass
    return render_template('log.html')

@app.route('/reg', methods=['GET', 'POST'])
def get_reg():
    pass
    return render_template('reg.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )