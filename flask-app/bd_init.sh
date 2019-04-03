flask db init
flask db migrate -m "user table"
flask db migrate -m "post table"
flask db upgrade