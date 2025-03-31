import time

def memoize(func):
    """
    Store the results of the decorated function for fast lookup
    """
    # Store results in a dictionary that maps arguments to results.
    cache = {}
    # Create a wrapper to be the new decorated function.
    def wrapper(*args, **kwargs):
        # Define a hashable key for  'kwargs'.
        kwargs_key = tuple(sorted(kwargs.items()))
        # kwargs_key is a tuple of the sorted items in kwargs. It looks like this:
        # (('a', 1), ('b', 2))
        # kwargs.items() look like this:
        # {'a': 1, 'b': 2}
        # If these arguments haven't been seen before:
        if (args, kwargs_key) not in cache:
            # Call func and store the result.
            cache[(args, kwargs_key)] = func(*args, **kwargs)
        return cache[(args, kwargs_key)]
    return wrapper

@memoize
def slow_function(a, b):
    """
    Simulate a slow function by sleeping for 2 seconds
    """
    print('Sleeping...')
    time.sleep(2)
    return a + b

if __name__ == "__main__":
    print(slow_function(3, 4))
    print(slow_function(3, 4)) # This will return the cached result without sleeping
    print(slow_function(5, 6)) # This will take 2 seconds to compute
    print(slow_function(5, 6)) # This will return the cached result without sleeping

