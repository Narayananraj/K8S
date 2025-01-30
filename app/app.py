from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': 'admin123',
    'database': 'user_db'
}

@app.route('/')
def index():
    return render_template('index.html', message=None)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    # Insert into MySQL
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        
        # Success message
        message = f"YOUR DATA STORED SUCCESSFULLY IN OUR DB"
        message_class = "success"  # Green background for success
    except Exception as e:
        # Error message
        message = f"Error: {e}"
        message_class = "error"  # Red background for error
    finally:
        cursor.close()
        conn.close()

    return render_template('index.html', message=message, message_class=message_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

