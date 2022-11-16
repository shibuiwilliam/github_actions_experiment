FROM python:3-slim

COPY py_docker/src /opt/py_docker/src
WORKDIR /opt/py_docker/
COPY py_docker/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "-m", "src.main"]
