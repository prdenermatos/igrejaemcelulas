from flask import Flask

app = Flask(__name__)
app.secret_key = 'sigelo'

from src.controller.login import *
from src.controller.menu import *


if __name__ == "__main__":
    app.run(debug=True)



 







 