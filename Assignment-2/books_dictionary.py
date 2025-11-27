books = {}
while True:
  decision = input("Program start ko lagi Y press garnu hosh, exit ko lagi N: ")
  if decision.lower() == 'y':
    book_name = input("Book ko naam lekhnuhosh: ")
    quant = int(input("Book ko Quantity: "))
    books.update({book_name:quant})
  else:
    break
print(books)



