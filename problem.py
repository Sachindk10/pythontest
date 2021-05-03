# print("Hello")
#my_str = input("Enter sentance:")
#req_word = input("what to search?")
#print(f"The no of times {req_word} occure in the sentance is {my_str.count(req_word)}")

# for i in range(num):
#   print(num, end=' ')
# print("\n")

# for i in range(1, 51):
#  if i % 15 == 0:
#       print("fizzbuzz")
#  elif i % 3 == 0:
#       print("fizz")
#  elif i % 5 == 0:
#      print("buzz")
#  else:
#      print(i)

terms = 10
no1, no2 = 0, 1
count = 0
print("Fibonacci series")
while count < terms:
    print(no1, end=' ')
    no3 = no1 + no2
    no1 = no2
    no2 = no3
    count += 1
