# FROM python:latest

# RUN pip install mlflow
# RUN apt-get update
# # RUN apt install sudo

# RUN apt-get install postgresql postgresql-contrib postgresql-server-dev-all

# # RUN sudo -u postgres psql

# RUN CREATE DATABASE mlflow;
# RUN CREATE USER mlflow WITH ENCRYPTED PASSWORD 'mlflow';
# RUN GRANT ALL PRIVILEGES ON DATABASE mlflow TO mlflow;

# RUN apt install gcc
# RUN pip install psycopg2

# RUN mkdir ~/mlruns

# CMD mlflow server --backend-store-uri postgresql://mlflow:mlflow@localhost/mlflow --default-artifact-root file:/home/your_user/mlruns -h 0.0.0.0 -p 8000


FROM python:3.8.2-slim

RUN pip install PyMySQL==0.9.3 && \   
    pip install psycopg2-binary==2.8.5 && \
    pip install mlflow[extras]==1.9.1
    
ENTRYPOINT ["mlflow", "server"]