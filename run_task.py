from tasks import add, test_failure

try:
    # simple task
    result = add.delay(10, 1)
    result_sum = result.get(timeout=5)
    assert result_sum == 11

    # task that's expected to fail
    result = test_failure.delay(2)
    result.get(timeout=300)
except Exception as exc:
    print(result.traceback)