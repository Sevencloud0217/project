from flask import Flask
app = Flask(__name__)

app.config.from_envvar('DEBUG')
if __name__ == '__main__':
    app.run()