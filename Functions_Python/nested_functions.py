# You want to show your niece that no matter what you do to my_special_function() after passing it to get_new_func(), the new function still mimics the behavior of the original my_special_function() because it is in the new function's closure.

def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)
# When I make the above function call, whatever is are the values inside my_special_function() are copied to new_func() as colusre and stored in the closure of new_func(). So I can use new_func() to call my_special_function() even if I delete my_special_function() or redefine it. new_func.__closure__ will show the closure of new_func() which will have the values of my_special_function() stored in it.

# Redefine my_special_function() to just print "hello"
def my_special_function():
    print('hello')

# Delete my_special_function()
del(my_special_function)

# Show that you still get the original message even if you overwrite my_special_function() with the new function.
# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

new_func()