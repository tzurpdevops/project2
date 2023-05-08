from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def main_page():
    return render_template('main.html')
@app.route('/hello', methods=['GET','POST'])
def submit_page():
    name = request.form.get('name')
    print('name = ', name)
    if type(name) != str:
        name = 'no one (;'
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)