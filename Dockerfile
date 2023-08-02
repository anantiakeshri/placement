FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip

RUN pip3 install --upgrade pip

RUN pip install flask flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run



# FROM ubuntu                                       #YT code + FAiled

# RUN apt-get -y update && apt-get -y install python3

# RUN pip install flask flask-mysql

# COPY . /opt/source-code

# ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run



# FROM python:3.6                           #LAb code
  
# RUN pip install flask

# COPY . /opt/

# EXPOSE 8080

# WORKDIR /opt

# ENTRYPOINT ["python", "app.py"]