FROM python:latest

# ENV PYTHON_VERSION 3.10.0

# Creating Application Source Code Directory
RUN mkdir -p /usr/src/topbottombank

# Setting Home Directory for containers
WORKDIR /usr/src/topbottombank

# Copy requirements and credentials into docker local folders
COPY requirements.txt /usr/src/topbottombank/ 

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

# Copying src code to Container
COPY . /usr/src/topbottombank

CMD python /usr/src/topbottombank/src/main.py
