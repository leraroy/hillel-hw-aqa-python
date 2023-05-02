"""
Написать декоратор skip, которым можно декорировать функции.

Если переданное выражение condition истинное,
функция не должна выполнятся, а должна вывестись строка
переданная в аргументе reason.

Если выражение condition ложное, функция должна выполнится.

def skip(condition, reason=''):
    pass
Пример использования:

@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5

test_two_plus_two()  # Skipped because of JIRA-123 bug
"""


def skip(condition, reason=''):
    def param(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(reason)
            if not condition:
                return func(*args, **kwargs)

        return wrapper

    return param


@skip(condition=False, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two(a, b):
    return a + b


print(test_two_plus_two(45, 45))  # Skipped because of JIRA-123 bug
