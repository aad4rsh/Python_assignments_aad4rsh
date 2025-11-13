name = input("Tapiko full name halnuhosh: ")
print(name)
first_initial = name[0]


for i in range(len(name)):
  if name[i] == " ":
    last_initial = name[i+1]

print("Tapaiko initials: " + first_initial +"." +last_initial)