FROM python:3.9
ENV LISTEN_PORT=5000
EXPOSE 5000
WORKDIR /backend

ADD . /backend

RUN pip install --upgrade pip

RUN pip install -r requirements.txt



CMD [ "python","app.py" ]