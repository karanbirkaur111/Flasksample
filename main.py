from flask import Flask, request , render_template



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
app = Flask(__name__)
# Using Jinja2 template
# http://127.0.0.1:5000/welcome
@app.route('/welcome')
def welcome():
    return render_template('hello.html')  # Using render function from flask

#http://127.0.0.1:5000/
@app.route('/name')
def my_name():
    return 'karanbir<h1> kaur </h1>'
#http://127.0.0.1:5000/name
@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', myname=name)  # Passing Parameter to template

@app.route('/sum', methods=['GET'])
def add_number():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return 'SUM : ' + str(c)
#http://127.0.0.1:5000/sum?a=10&b=20
@app.route('/user-data', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        result = '''
                        <h1>First Name : {}<h1>
                        <h1>Last Name : {}<h1>
                    '''
        return result.format(first_name, last_name)
    return ''

@app.route('/user')
def user_form():
    return '''
        <form method="POST" action="http://127.0.0.1:5000/user-data">
               <div><label>First Name: <input type="text" name="first_name"></label></div>
               <div><label>Last Name: <input type="text" name="last_name"></label></div>
               <input type="submit" value="Submit">
        </form>
    '''




if __name__ == '__main__':
    print_hi('PyCharm')
app.run()


