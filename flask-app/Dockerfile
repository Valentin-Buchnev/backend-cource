FROM python:3.4-alpine
WORKDIR /code
ADD . /code
RUN pip3 install -r /code/requirements.txt
CMD ["export", "FLASK_APP=first_app.py"]
CMD ["flask", "run"]
