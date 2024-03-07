def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()

        print("Something is happening after the function is called.")

    return wrapper


# Define a another decorator function
def validate_request(func):
    def wrapper_func(*args):
        print("Validating the request")
        for arg in args:
            if not isinstance(arg, str):
                print("Request is not valid")
                return "Request is not valid"
        func(*args)

    return wrapper_func


# Apply the decorator using the "@" syntax
# @my_decorator
@my_decorator
def say_hello():
    print("Hello!")


@validate_request
def say_hello_2(args):
    print("Hello! " + args)


# triggering the function
say_hello()
