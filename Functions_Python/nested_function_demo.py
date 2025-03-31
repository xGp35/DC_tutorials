def multiply(a, b):
    return a*b
def double_args(func):
    def wrapper(a, b):
        return func(a*2, b*2)
    return wrapper
new_multiply = double_args(multiply)
print(new_multiply(1, 5)) # 4*10 = 40
print(new_multiply.__closure__[0].cell_contents) # <function multiply at 0x7f8b3c1b7d30>
print(new_multiply.__closure__[0].cell_contents(1, 5)) # 1*5 = 5
print(new_multiply(3, 4)) # 6*8 = 48
# Output:
# 40
# 48
# Explanation:  The double_args() function takes a function as an argument and returns a new function that doubles the arguments passed to the original function. In this case, the multiply() function is passed to double_args(), which returns a new function new_multiply(). When new_multiply() is called with arguments (1, 5), it doubles the arguments to (2, 10) and returns the result of multiply(2, 10) = 20. Similarly, when new_multiply() is called with arguments (3, 4), it doubles the arguments to (6, 8) and returns the result of multiply(6, 8) = 48.
#
# The double_args() function is an example of a decorator that modifies the behavior of a function by wrapping it with additional functionality. In this case, the wrapper function doubles the arguments passed to the original function before calling it. This allows you to reuse the original function with modified behavior without changing its implementation. Decorators are a powerful feature of Python that enable you to add functionality to existing functions without modifying their code.        