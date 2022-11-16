FROM python:3-slim

WORKDIR /
COPY src /src
COPY requirements.txt /src/requirements.txt

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "-m", "src.main"]
