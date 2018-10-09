from celery import Celery
from celery.utils.log import get_task_logger

from time import sleep

app = Celery('tasks', broker='pyamqp://guest@rabbit//', backend='mongodb://mongo')
logger = get_task_logger(__name__)


class TestException(Exception):
    pass


@app.task
def add(x, y):
    return x+y


def raise_exception(sleep_interval):
    sleep(sleep_interval)
    raise TestException('this function raises an exception')


@app.task(autoretry_for=(TestException,), retry_jitter=False, retry_backoff=2, retry_kwargs={'max_retries': 4})
def test_failure(sleep_interval):
    try:
        raise_exception(sleep_interval)
    except TestException as exc:
        logger.warning('Caught exception: {}'.format(exc))
        raise
