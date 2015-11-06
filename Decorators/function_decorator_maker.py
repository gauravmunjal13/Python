maker_arg = "gaurav"


def decorator_maker(arg):
    print("decorator_maker:", arg)

    def decorator(function):
        print("decorator:", arg, function)

        def wrapper(*args, **kwargs):
            print("wrapper", arg, args, kwargs)
            function(*args, **kwargs)
            print("wrapper ends")

        print("decorator ends")
        return wrapper

    print("decorator_maker ends")
    return decorator


# @decorator_maker(maker_arg)
def function_to_be_decorated(arg1, arg2, arg3="None"):
    print("function_to_be_decorated:", arg1, arg2, arg3)

# equivlent to:
function_to_be_decorated = decorator_maker(maker_arg)(function_to_be_decorated)


def main():
    print("main")
    function_to_be_decorated("hello", "world")
    print("main ends")


if __name__ == "__main__":
    main()
