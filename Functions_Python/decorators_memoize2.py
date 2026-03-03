import time
def memoize(func):
    """
    Store the results of the decorated function for fast lookup
    """
    # Store results in a dict that maps arguments to results
    cache = {}
    # Define the wrapper function to return.
    def wrapper(*args, **kwargs):
        # Define a hashable key for 'kwargs'.
        kwargs_key = tuple(sorted(kwargs.items()))
        # If these arguments haven't been seen before,
        if (args, kwargs_key) not in cache:
            # Call func() and store the result.
            cache[(args, kwargs_key)] = func(*args, **kwargs)
        return cache[(args, kwargs_key)]
    return wrapper


@memoize
def slow_function(a, b):
    print('Sleeping...')
    time.sleep(5)
    return a + b

if __name__ == '__main__':
    # Call the function with the same arguments multiple times
    print(slow_function(3, 4))
    print(slow_function(3, 4))
    print(slow_function(5, 6))
    print(slow_function(3, 4))
    print(slow_function(5, 6))
    print(slow_function(7, 8))
    print(slow_function(7, 8))
    