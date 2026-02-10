#python else

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#Python Shorthand If
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Python Logical Operators
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Python Nested If
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


#Python Pass Statement
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")


