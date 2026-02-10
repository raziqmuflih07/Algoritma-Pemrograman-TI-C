#python functions
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


def get_greeting():
  return "Hello from a function"

print(get_greeting())



#python scope
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#lambda function
x = lambda a : a + 10
print(x(5))



#recursion
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))


def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))