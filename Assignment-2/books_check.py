books = {
    "The Silent Forest": 4,
    "Journey to Mars": 10,
    "Python Essentials": 7,
    "The Lost Kingdom": 3,
    "Mystery of the Blue Lake": 8,
    "Data Science Handbook": 5,
    "Winds of the East": 2,
    "The Final Empire": 6,
    "Shadows of Time": 9,
    "Digital Dreams": 11
}

while True:
    book_name = input("Kun book chaiyo? (exit ko lagi 'N' lehnuhola): ")

    if book_name.lower() == "n":
        print("Dhanyabad! Pheri bhetaula.")
        break

    if book_name not in books:
        print("Book available chhaina.")
        continue

    while True:
        book_quantity = input("Kati ota chaiyo? ")
        if not book_quantity.isdigit():
            print("Invalid quantity input. Matra number halnuhola.")
        else:
            book_quantity = int(book_quantity)
            break

    available = books[book_name]

    if book_quantity <= available:
        print("Available.")
    else:
        print(f"Partially Available: Matra {available} ota cha.")
