FROM python:slim-buster

RUN pip install boto3 requests pyyaml
ADD app/ /opt/
