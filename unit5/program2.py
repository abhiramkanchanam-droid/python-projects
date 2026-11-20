class BookCatalog:
  def __init__(self):
    self.items = []
  def add_book(self, title):
    self.items.append(title)
    print(f"{title} added successfully")
  def display_books(self):
    print("Available Books:")
    for title in self.items:
      print(title)
catalog = BookCatalog()
catalog.add_book("Python Programming")
catalog.add_book("Java Programming")
catalog.add_book("Data Structures")
catalog.display_books()