FROM python:3-slim

COPY src /opt/py_docker/src
WORKDIR /opt/py_docker/
COPY requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "-m", "src.main"]
