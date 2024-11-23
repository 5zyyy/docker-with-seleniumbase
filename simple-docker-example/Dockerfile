FROM python:3.13

ADD requirements.txt .

ADD simple-docker.py .

RUN pip install -r requirements.txt

CMD ["python3", "./simple-docker.py"]