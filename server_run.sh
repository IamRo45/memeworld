cd xmeme

flask db upgrade
FLASK_APP=xmeme.py
flask run -h localhost -p 8081 &
