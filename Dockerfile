FROM ubuntu:20.04
RUN apt update && apt install -y python python-pip
RUN pip install flask
COPY app.py /usr
ENTRYPOINT FLASK_APP="/usr/app.py run --host="0.0.0.0" --port=8080
