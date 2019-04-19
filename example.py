import elegantE as elg


def do_something(value):
    print(value)


test_exception_handler = elg.ExceptionHandler

test_exception_handler.regist(
    Exception,
    lambda: print('Global Exception')
)

test_exception_handler.regist(
    ValueError,
    do_something,
    {'value': 'Test value'}
)


class ArgumentError(Exception):
    pass


class NoneArgumentError(ArgumentError):
    pass


def fib(n):
    if n is None:
        raise NoneArgumentError
    if not isinstance(n, int):
        raise ArgumentError

    if n == 0 or n == 1: return 1
    return fib(n - 1) + fib(n - 2)


@test_exception_handler([
    (NoneArgumentError, lambda: print('None Argument Error')),
    (ArgumentError, lambda: print('Argument Error')),
    (AttributeError, lambda x: print(f'Attribute Error {x}'), {'x': 'test'})
])
def main():
    fib('Hello world')


if __name__ == '__main__':
    main()

