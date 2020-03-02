``` python
import interval_decorator

@interval_decorator.interval(1)
def my_method(count):
    print("Pass interval")
    count += 1
    return count


@interval_decorator.interval_or_return_first_value(1)
def my_method_or_return_first_value(count):
    print("Pass interval")
    updated_count = count + 1
    return updated_count


assert my_method(10) == 11
assert my_method(10) == None
assert my_method_or_return_first_value(12) == 13
assert my_method_or_return_first_value(12) == 12
```
