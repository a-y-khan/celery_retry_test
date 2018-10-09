# Testing Celery Retry

Testing new celery retry functionality introduced in
[v4.2](http://docs.celeryproject.org/en/latest/userguide/tasks.html#automatic-retry-for-known-exceptions):

* Automatic retry for known exceptions
* Retry backoff
* Setting retry jitter

## Run

### Build images

```bash
docker-compose build
```

### Run celery worker container

```bash
docker-compose up -d celery_worker
```

### Run test tasks
Check worker logs before this step to make sure worker is ready to run tasks.

```bash
docker-compose logs celery_worker
docker-compose run celery_test run_task.py
```

### Stop and cleanup
```bash
docker-compose down
```