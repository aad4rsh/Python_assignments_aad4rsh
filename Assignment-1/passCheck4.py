password = input("Afno password lekhnuhos: ")
special_chars = "@#$%&"

if len(password) < 6:
  print("Password dherai weak cha. Nursery ko bachha le hack gardincha")

elif len(password) >= 8:
  for char in password:
    if char in special_chars:
        print("Password strong cha! Aba ta hacker pani darauchha")
        break
      
elif len(password) >= 6:
       print("Password moderate condition cha. Thik cha, tara special character haru add garda aura plus huney sambhawana")

  


