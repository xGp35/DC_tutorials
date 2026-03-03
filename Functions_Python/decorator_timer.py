import time

    # The wrapper function is defined inside the decorator function and takes the same arguments as the original function.
    # This allows the wrapper to accept any number of arguments and keyword arguments, making it flexible and reusable.
    # The wrapper function is responsible for executing the original function and measuring its execution time.
    # It also prints the execution time of the original function.
    # The wrapper function is returned from the decorator function and is used to replace the original function.
    # This allows the decorator to modify the behavior of the original function without changing its implementation.

def timer(func):
    """
    A decorator that measures the time taken by a function to execute.
    Args:
        func (callable): The function being decorated.
    Returns:
        callable: The decorated function.
    """
    def wrapper(*args, **kwargs):
        # *args - any number of positional arguments
        # **kwargs - any number of keyword arguments
        t_start = time.time()  # Record the start time
        # Wrapper gets the result of calling the decorated function and stores the result.
        result = func(*args, **kwargs)  # Call the original function
        #After calling the decorated function, wrapper checkes the time again.
        t_total = time.time() - t_start  # Calculate the execution time
        print(f"Function '{func.__name__}' took {t_total:.4f} seconds to execute.")
        #We now return the value that the decorated function calculated.
        return result  # Return the result of the original function
    return wrapper

@timer
def sleep_n_seconds(n):
    time.sleep(n)  # Sleep for n seconds

sleep_n_seconds(5)
#This decorator is very useful for finding slow parts of my code
