import interval_decorator
import time


def test_version():
    count = 0

    @interval_decorator.interval(1)
    def my_method(count):
        print("Pass interval")
        count += 1
        return count

    result = my_method(count)
    if result:
        count = result
    result = my_method(count)
    if result:
        count = result
    time.sleep(1)
    result = my_method(count)
    if result:
        count = result

    assert count == 2
