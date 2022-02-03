# python3 -m venv env/myenv
# source env/myenv/bin/activate

from dojos_app import app
from dojos_app.controllers import dojos_controller

if __name__=="__main__":
    app.run(debug=True)