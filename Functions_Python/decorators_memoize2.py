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