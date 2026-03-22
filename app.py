from flask import Flask
import os

app = Flask(__johnnas__)

@app.route('/')
def hello():
    return f"Hello from {'hardened' if os.getuid() != 0 else 'vulnerable'} container!"

if __name__ == '__main__':
    # Körs på 0.0.0.0 för att vara nåbar utanför containern
    app.run(host='0.0.0.0', port=5000)
