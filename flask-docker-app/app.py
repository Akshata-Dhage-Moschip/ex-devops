from flask import Flask, render_template
import os
 
app = Flask(__name__, template_folder='template', static_folder='static')
 
@app.route('/')
def home():
    return render_template('index.html')
 
if __name__ == '__main__':
    print("Current directory:", os.getcwd())
    app.run(debug=True, host='0.0.0.0')
