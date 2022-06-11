FROM python:3-slim
LABEL maintainer="Djalma Jr"
ARG MLFLOW_VERSION=1.19.0

WORKDIR /mlflow/
RUN pip install --no-cache-dir mlflow==$MLFLOW_VERSION
# RUN mkdir -p /mlflow/mlruns

EXPOSE 8000

ENV BACKEND_URI sqlite:////mlflow/mlflow.db
ENV ARTIFACT_ROOT /mlflow/mlruns

CMD mlflow server --backend-store-uri ${BACKEND_URI} --default-artifact-root ${ARTIFACT_ROOT} --host 0.0.0.0 --port 8000


# FROM python:3-slim
# LABEL maintainer="Djalma Jr"
# ARG MLFLOW_VERSION=1.19.0

# # COPY --chown=admin:admin mlflow /usr/src/mlflow/
# WORKDIR /usr/src/mlflow/
# RUN mkdir -p /usr/src/mlruns/
# # RUN chmod ugo+rwx mlruns
# RUN chmod 777 /usr/src/mlruns/
# RUN pip install --no-cache-dir mlflow==$MLFLOW_VERSION
# EXPOSE 5000

# ENV BACKEND_URI sqlite:////usr/src/mlflow//mlflow.db
# ENV ARTIFACT_ROOT /usr/src/mlruns/

# CMD mlflow server --backend-store-uri ${BACKEND_URI} --default-artifact-root ${ARTIFACT_ROOT} --host 0.0.0.0 --port 5000






  
# FROM python:3.8.2-slim

# RUN pip install PyMySQL==0.9.3 && \   
#     pip install psycopg2-binary==2.8.5 && \
#     pip install mlflow[extras]==1.9.1

# ENTRYPOINT ["mlflow", "server"]