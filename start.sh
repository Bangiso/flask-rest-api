echo "Setting up environment"
export FLASK_APP=hello
export FLASK_ENV=production
python -m venv venv
. venv/bin/activate
echo "Installing flask and mysql connector"
pip install Flask
pip install mysql-connector-python
echo "Setup finished"
flask run --host=127.0.0.1 --port=8080