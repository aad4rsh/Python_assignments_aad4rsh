numbers = []

count = 1
while True:
  num = int(input(f"List ko {count} th number halnush: "))
  if num > 50:
    break
  numbers.append(num)
  count = count +1

filtered = list(filter(lambda x : x % 5 !=0, numbers ))
print(filtered)

