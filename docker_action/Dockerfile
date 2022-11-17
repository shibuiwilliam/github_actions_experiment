FROM python:3-slim

WORKDIR /opt
COPY src /opt/src
COPY requirements.txt /opt/requirements.txt
COPY entrypoint.sh /opt/entrypoint.sh

RUN pip install -r /opt/requirements.txt && \
    chmod +x /opt/entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
