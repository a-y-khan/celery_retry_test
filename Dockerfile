FROM python:3.7 as worker

WORKDIR /opt/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENTRYPOINT ["celery"]

FROM worker as task_runner

ENTRYPOINT ["python3"]