FROM alpine:3.5
RUN apk add --update py2-pip
RUN apk add --update bash
WORKDIR /code
ADD first_app.py /code
ADD config.py /code
ADD web_app /code
ADD migrations /code
ADD requirements.txt /code
RUN pip install -r /code/requirements.txt
CMD ["export", "FLASK_APP=first_app.py"]
CMD ["flask", "run"]
