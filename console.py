import pdb
from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

    
book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Terry Prachett") 
author_repository.save(author1)
author2 = Author("J.R. Tolkein")
author_repository.save(author2)


book1 = Book("Good Omens", "Fantasy", author1)
book_repository.save(book1)

book2 = Book("Night Watch", "Fantasy", author1)
book_repository.save(book2)

book3 = Book("Lord of the Rings", "Historical Fantasy", author2)
book_repository.save(book3)

