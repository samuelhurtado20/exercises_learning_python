from typing import List, Dict

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' por {self.author}"

class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

class Library:
    def __init__(self):
        self.inventory: Dict[str, Dict] = {}
        self.users: List[User] = []

    def add_book(self, book: Book, quantity: int = 1) -> None:
        if book.isbn in self.inventory:
            self.inventory[book.isbn]['available'] += quantity
        else:
            self.inventory[book.isbn] = {'book': book, 'available': quantity, 'borrowed': []}
        print(f"Añadido(s) {quantity} ejemplar(es) de {book} al inventario")

    def register_user(self, user: User) -> None:
        self.users.append(user)
        print(f"Usuario '{user.name}' registrado")

    def show_available_books(self) -> None:
        available_books = [(info['book'], info['available']) for info in self.inventory.values() if info['available'] > 0]
        
        if not available_books:
            print("No hay libros disponibles en la biblioteca")
        else:
            print("Libros disponibles:")
            for book, quantity in available_books:
                print(f"{book} - {quantity} ejemplar(es) disponible(s)")

    def borrow_book(self, user: User, isbn: str) -> None:
        if isbn not in self.inventory:
            print(f"El libro con ISBN {isbn} no está en nuestro inventario")
            return
        
        book_info = self.inventory[isbn]
        if book_info['available'] > 0:
            book_info['available'] -= 1
            book_info['borrowed'].append(user)
            print(f"{user.name} ha tomado prestado '{book_info['book'].title}'")
        else:
            print(f"No hay ejemplares disponibles de '{book_info['book'].title}'")

    def return_book(self, user: User, isbn: str) -> None:
        if isbn not in self.inventory:
            print(f"El libro con ISBN {isbn} no pertenece a nuestro inventario")
            return
        
        book_info = self.inventory[isbn]
        if user in book_info['borrowed']:
            book_info['available'] += 1
            book_info['borrowed'].remove(user)
            print(f"{user.name} ha devuelto '{book_info['book'].title}'")
        else:
            print(f"{user.name} no tenía prestado '{book_info['book'].title}'")

    def find_book(self, isbn: str) -> Book:
        return self.inventory[isbn]['book'] if isbn in self.inventory else None

    def find_books_by_author(self, author: str) -> List[Book]:
        return [info['book'] for info in self.inventory.values() if info['book'].author.lower() == author.lower()]

# Ejemplo de uso
if __name__ == "__main__":
    library = Library()

    # Crear libros
    book1 = Book("El principito", "Antoine de Saint-Exupéry", "978-3140464079")
    book2 = Book("1984", "George Orwell", "978-0451524935")

    # Añadir libros a la biblioteca
    library.add_book(book1, 2)
    library.add_book(book2, 1)

    # Crear usuarios
    user1 = User("Carli", "001")
    user2 = User("Ana", "002")

    # Registrar usuarios
    library.register_user(user1)
    library.register_user(user2)

    # Mostrar libros disponibles inicialmente
    print("\nLibros disponibles inicialmente:")
    library.show_available_books()

    # Realizar préstamos
    library.borrow_book(user1, "978-3140464079")
    library.borrow_book(user2, "978-3140464079")
    library.borrow_book(user1, "978-0451524935")

    # Mostrar libros disponibles después de los préstamos
    print("\nLibros disponibles después de los préstamos:")
    library.show_available_books()

    # Devolver libros
    library.return_book(user1, "978-3140464079")
    library.return_book(user1, "978-0451524935")

    # Mostrar libros disponibles después de las devoluciones
    print("\nLibros disponibles después de las devoluciones:")
    library.show_available_books()

    # Prestar todos los libros disponibles
    library.borrow_book(user2, "978-3140464079")
    library.borrow_book(user2, "978-0451524935")

    # Mostrar libros disponibles cuando no hay ninguno
    print("\nIntentando mostrar libros disponibles cuando no hay ninguno:")
    library.show_available_books()from typing import List, Dict

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' por {self.author}"

class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

class Library:
    def __init__(self):
        self.inventory: Dict[str, Dict] = {}
        self.users: List[User] = []

    def add_book(self, book: Book, quantity: int = 1) -> None:
        if book.isbn in self.inventory:
            self.inventory[book.isbn]['available'] += quantity
        else:
            self.inventory[book.isbn] = {'book': book, 'available': quantity, 'borrowed': []}
        print(f"Añadido(s) {quantity} ejemplar(es) de {book} al inventario")

    def register_user(self, user: User) -> None:
        self.users.append(user)
        print(f"Usuario '{user.name}' registrado")

    def show_available_books(self) -> None:
        available_books = [(info['book'], info['available']) for info in self.inventory.values() if info['available'] > 0]
        
        if not available_books:
            print("No hay libros disponibles en la biblioteca")
        else:
            print("Libros disponibles:")
            for book, quantity in available_books:
                print(f"{book} - {quantity} ejemplar(es) disponible(s)")

    def borrow_book(self, user: User, isbn: str) -> None:
        if isbn not in self.inventory:
            print(f"El libro con ISBN {isbn} no está en nuestro inventario")
            return
        
        book_info = self.inventory[isbn]
        if book_info['available'] > 0:
            book_info['available'] -= 1
            book_info['borrowed'].append(user)
            print(f"{user.name} ha tomado prestado '{book_info['book'].title}'")
        else:
            print(f"No hay ejemplares disponibles de '{book_info['book'].title}'")

    def return_book(self, user: User, isbn: str) -> None:
        if isbn not in self.inventory:
            print(f"El libro con ISBN {isbn} no pertenece a nuestro inventario")
            return
        
        book_info = self.inventory[isbn]
        if user in book_info['borrowed']:
            book_info['available'] += 1
            book_info['borrowed'].remove(user)
            print(f"{user.name} ha devuelto '{book_info['book'].title}'")
        else:
            print(f"{user.name} no tenía prestado '{book_info['book'].title}'")

    def find_book(self, isbn: str) -> Book:
        return self.inventory[isbn]['book'] if isbn in self.inventory else None

    def find_books_by_author(self, author: str) -> List[Book]:
        return [info['book'] for info in self.inventory.values() if info['book'].author.lower() == author.lower()]

# Ejemplo de uso
if __name__ == "__main__":
    library = Library()

    # Crear libros
    book1 = Book("El principito", "Antoine de Saint-Exupéry", "978-3140464079")
    book2 = Book("1984", "George Orwell", "978-0451524935")

    # Añadir libros a la biblioteca
    library.add_book(book1, 2)
    library.add_book(book2, 1)

    # Crear usuarios
    user1 = User("Carli", "001")
    user2 = User("Ana", "002")

    # Registrar usuarios
    library.register_user(user1)
    library.register_user(user2)

    # Mostrar libros disponibles inicialmente
    print("\nLibros disponibles inicialmente:")
    library.show_available_books()

    # Realizar préstamos
    library.borrow_book(user1, "978-3140464079")
    library.borrow_book(user2, "978-3140464079")
    library.borrow_book(user1, "978-0451524935")

    # Mostrar libros disponibles después de los préstamos
    print("\nLibros disponibles después de los préstamos:")
    library.show_available_books()

    # Devolver libros
    library.return_book(user1, "978-3140464079")
    library.return_book(user1, "978-0451524935")

    # Mostrar libros disponibles después de las devoluciones
    print("\nLibros disponibles después de las devoluciones:")
    library.show_available_books()

    # Prestar todos los libros disponibles
    library.borrow_book(user2, "978-3140464079")
    library.borrow_book(user2, "978-0451524935")

    # Mostrar libros disponibles cuando no hay ninguno
    print("\nIntentando mostrar libros disponibles cuando no hay ninguno:")
    library.show_available_books()
```from typing import List, Dict



class Book:

&#x20;   def \_\_init\_\_(self, title: str, author: str, isbn: str):

&#x20;       self.title = title

&#x20;       self.author = author

&#x20;       self.isbn = isbn



&#x20;   def \_\_str\_\_(self):

&#x20;       return f"'{self.title}' por {self.author}"



class User:

&#x20;   def \_\_init\_\_(self, name: str, user\_id: str):

&#x20;       self.name = name

&#x20;       self.user\_id = user\_id



class Library:

&#x20;   def \_\_init\_\_(self):

&#x20;       self.inventory: Dict\[str, Dict] = {}

&#x20;       self.users: List\[User] = \[]



&#x20;   def add\_book(self, book: Book, quantity: int = 1) -> None:

&#x20;       if book.isbn in self.inventory:

&#x20;           self.inventory\[book.isbn]\['available'] += quantity

&#x20;       else:

&#x20;           self.inventory\[book.isbn] = {'book': book, 'available': quantity, 'borrowed': \[]}

&#x20;       print(f"Añadido(s) {quantity} ejemplar(es) de {book} al inventario")



&#x20;   def register\_user(self, user: User) -> None:

&#x20;       self.users.append(user)

&#x20;       print(f"Usuario '{user.name}' registrado")



&#x20;   def show\_available\_books(self) -> None:

&#x20;       available\_books = \[(info\['book'], info\['available']) for info in self.inventory.values() if info\['available'] > 0]

&#x20;      &#x20;

&#x20;       if not available\_books:

&#x20;           print("No hay libros disponibles en la biblioteca")

&#x20;       else:

&#x20;           print("Libros disponibles:")

&#x20;           for book, quantity in available\_books:

&#x20;               print(f"{book} - {quantity} ejemplar(es) disponible(s)")



&#x20;   def borrow\_book(self, user: User, isbn: str) -> None:

&#x20;       if isbn not in self.inventory:

&#x20;           print(f"El libro con ISBN {isbn} no está en nuestro inventario")

&#x20;           return

&#x20;      &#x20;

&#x20;       book\_info = self.inventory\[isbn]

&#x20;       if book\_info\['available'] > 0:

&#x20;           book\_info\['available'] -= 1

&#x20;           book\_info\['borrowed'].append(user)

&#x20;           print(f"{user.name} ha tomado prestado '{book\_info\['book'].title}'")

&#x20;       else:

&#x20;           print(f"No hay ejemplares disponibles de '{book\_info\['book'].title}'")



&#x20;   def return\_book(self, user: User, isbn: str) -> None:

&#x20;       if isbn not in self.inventory:

&#x20;           print(f"El libro con ISBN {isbn} no pertenece a nuestro inventario")

&#x20;           return

&#x20;      &#x20;

&#x20;       book\_info = self.inventory\[isbn]

&#x20;       if user in book\_info\['borrowed']:

&#x20;           book\_info\['available'] += 1

&#x20;           book\_info\['borrowed'].remove(user)

&#x20;           print(f"{user.name} ha devuelto '{book\_info\['book'].title}'")

&#x20;       else:

&#x20;           print(f"{user.name} no tenía prestado '{book\_info\['book'].title}'")



&#x20;   def find\_book(self, isbn: str) -> Book:

&#x20;       return self.inventory\[isbn]\['book'] if isbn in self.inventory else None



&#x20;   def find\_books\_by\_author(self, author: str) -> List\[Book]:

&#x20;       return \[info\['book'] for info in self.inventory.values() if info\['book'].author.lower() == author.lower()]



\# Ejemplo de uso

if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   library = Library()



&#x20;   \# Crear libros

&#x20;   book1 = Book("El principito", "Antoine de Saint-Exupéry", "978-3140464079")

&#x20;   book2 = Book("1984", "George Orwell", "978-0451524935")



&#x20;   \# Añadir libros a la biblioteca

&#x20;   library.add\_book(book1, 2)

&#x20;   library.add\_book(book2, 1)



&#x20;   \# Crear usuarios

&#x20;   user1 = User("Carli", "001")

&#x20;   user2 = User("Ana", "002")



&#x20;   \# Registrar usuarios

&#x20;   library.register\_user(user1)

&#x20;   library.register\_user(user2)



&#x20;   \# Mostrar libros disponibles inicialmente

&#x20;   print("\nLibros disponibles inicialmente:")

&#x20;   library.show\_available\_books()



&#x20;   \# Realizar préstamos

&#x20;   library.borrow\_book(user1, "978-3140464079")

&#x20;   library.borrow\_book(user2, "978-3140464079")

&#x20;   library.borrow\_book(user1, "978-0451524935")



&#x20;   \# Mostrar libros disponibles después de los préstamos

&#x20;   print("\nLibros disponibles después de los préstamos:")

&#x20;   library.show\_available\_books()



&#x20;   \# Devolver libros

&#x20;   library.return\_book(user1, "978-3140464079")

&#x20;   library.return\_book(user1, "978-0451524935")



&#x20;   \# Mostrar libros disponibles después de las devoluciones

&#x20;   print("\nLibros disponibles después de las devoluciones:")

&#x20;   library.show\_available\_books()



&#x20;   \# Prestar todos los libros disponibles

&#x20;   library.borrow\_book(user2, "978-3140464079")

&#x20;   library.borrow\_book(user2, "978-0451524935")



&#x20;   \# Mostrar libros disponibles cuando no hay ninguno

&#x20;   print("\nIntentando mostrar libros disponibles cuando no hay ninguno:")

&#x20;   library.show\_available\_books()
