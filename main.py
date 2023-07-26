from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector as sql

app = Flask(__name__)

# Configure Host Variables
host_ip = '000.000.0.00'
host_port = 5000
app.secret_key = b'session-variable'

# Index Routing
@app.route("/")
def index():
    # Check Active Session
    if 'user' in session:
        return render_template("index.html", username = session['user'])
    else:
        return render_template("index.html")
    
# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        try:
            acc = request.form['account']
            pwd = request.form['password']
            # Connect to database
            connection = sql.connect(host='127.0.0.1', database='', user='', password='',  port=3306)
            # Query Database
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM users WHERE user = "{acc}" AND pass = "{pwd}";')
            # Check Login Credentials
            result = cursor.fetchall()
            if len(result) == 1:
                # Login Successful
                connection.close()
                session['user'] = f'{acc}'
            else:
                # Login Failed
                print(f'[-] Incorrect Credentials Provided for User: {acc}')

        except sql.Error as err :
            # Respond to error in request
            print('[-] MySQL Error: {}'.format(err))

        finally:
            return redirect(url_for('index'))
    else:
        #Method was a GET Request
        print("[-] Error: Request sent to /login was NOT a POST request")
        return redirect(url_for('index'))

# Register
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        try:
            acc = request.form['account']
            pwd = request.form['password']
            # Connect to database
            connection = sql.connect(host='127.0.0.1', database='', user='', password='',  port=3306)
            # Query Database
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO users (user, pass) VALUES ("{acc}","{pwd}")')
            connection.commit()
            
        except sql.Error as err :
            # Respond to error in request
            print('[-] MySQL Error: {}'.format(err))
            connection.rollback()

        finally:
            return redirect(url_for('index'))
    else:
        #Method was Not a POST Request
        print("[-] Error: Request sent to /register was NOT a POST request")
        return redirect(url_for('index'))

# Flask Debug Tool
if __name__ == '__main__':
    app.run(host=host_ip, port=host_port, debug=True, threaded=False)