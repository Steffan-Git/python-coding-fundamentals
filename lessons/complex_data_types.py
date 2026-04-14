# collections of values - storing data.
# lists, dictionaries, sets, tuples.

# lists - ordered(indexed), mutable, duplicate ok, any data type. 
# dictionaries - unordered(no index), key:value pair, any datatype fine + no key duplicates.

# x = hash("hello"): 1
# print(x)
# mem = x%(16 - 1)

# import sys
# d = {}
# for i in range(80):
#     d[i] = i
#     print(sys.getsizeof(d))

# import time 

# large_dict = {num : True for num in range(10_000_000)}
# large_list = list(range(10_000_000))

# target = 9_999_990

# start = time.time()
# search = target in large_list
# finish = time.time()
# print(f"list: {finish - start:.10f}")

# start = time.time()
# search = target in large_dict
# finish = time.time()
# print(f"dict: {finish - start:.10f}")

# drinks = {"still": "water", "fizzy": "cola"}

# # print(drinks["stilll"])
# print(drinks.get("stilll", ))
# string method
# .join()

# exercise:
#     - make a dictionary with keys as authors and 3 books per author.
#     - input asking the user for an author name (think about ux here).
#     - print the authors books AS A STRING!!!!!!!!!!!!!!!!!!!!!!!!!!
#     - error handling for author names.
#     - use built-ins/methods and only things we have covered.
#     - JUSTIFY YOUR CHOICES!
#     - later full schema design.  

# book_dictionary = {
# 	"N.T. Wright": ["The Bible for Everyone: A New Translation", "Surprised by Hope: Rethinking heaven, the resurrection and the mission of the Church"],
# 	"Martin Luther": ["95 Theses", "The Bondage of the Will", "Table Talk"],
# 	"Karl Barth": ["Church Dogmatics", "The Epistle to the Romans"]
# }

# author = input("Enter the name of the author: ")

# if author in book_dictionary:
# 	print("Books by " + author + ": ")
# 	books = ", ".join(book_dictionary[author])
# 	print(books)
# else:
# 	print("Cannot find any book by the author.")


# booklist = {

#     "J.K. Rowling": [
#         "Harry Potter and the Sorcerer's Stone",
#         "Harry Potter and the Chamber of Secrets",
#         "Harry Potter and the Prisoner of Azkaban"
#     ],
#     "Roald Dahl": [
#         "Charlie and the Chocolate Factory",
#         "Matilda",
#         "James and the Giant Peach"
#     ],
#     "Sheila McCullagh": [
#         "The Land of the Blue Flower",
#         "Tim and the Hidden People",
#         "The Village with Three Corners"
#     ]
# }

# print("Availible authors:")
# print(", ".join(booklist.keys()))

# author = input("please enter an authors name " )

# books = booklist.get(author, []) # or ["sorry no books found"] "sorry no books found"

# print(", ".join(books) or "no books found")

# JacksBookshop = {
#   "author1": {
#   "name": "Rick Riordan",
#   "book1": "The Lightning Thief", 
#   "book2": "The Sea of Monsters", 
#   "book3": "The Last Olympian",
# },
#   "author2": {
#   "name": "Jonathan Haidt",
#   "book1": "The Happiness Hypothesis", 
#   "book2": "The Righteous Mind",
#   "book3": "The Anxious Generation",  
# },
#   "author3": {
#   "name": "Colleen Hoover", 
#   "book1": "It Ends With Us",
#   "book2": "Verity",
#   "book3": "Hopeless",    
# }
# }
# y = JacksBookshop.get("author2").get("name")
# print(y)

# record  = JacksBookshop.get("author2")

# list_to_print = []

# for k, v in record.items():
#     if "book" in k:
#         list_to_print.append(v)

# print(", ".join(list_to_print))


# a full book schema:
# - authors/books(title, type, year, genre, publisher, ISBN)
# 5 authors 3 books each. 


# 1) Print out the title of every book in the structure.
# 2) Update the publisher of one book (your choice).


library = {
  "George Orwell": {
    "1984": {
      "Genre": "Dystopian",
      "Year": 1949,
      "Publisher": "Secker & Warburg",
      "ISBN": "9780451524935"
    },
    "Animal Farm": {
      "Genre": "Political Satire",
      "Year": 1945,
      "Publisher": "Secker & Warburg",
      "ISBN": "9780451526342"
    },
    "Homage To Catalonia": {
      "Genre": "Memoir",
      "Year": 1938,
      "Publisher": "Secker & Warburg",
      "ISBN": "9780156421171"
    },
    "Down And Out In Paris And London": {
      "Genre": "Memoir",
      "Year": 1933,
      "Publisher": "Victor Gollancz",
      "ISBN": "9780156262248"
    },
    "Coming Up For Air": {
      "Genre": "Fiction",
      "Year": 1939,
      "Publisher": "Victor Gollancz",
      "ISBN": "9780156196253"
    }
  },
  "J.K. Rowling": {
    "Harry Potter And The Sorcerer's Stone": {
      "Genre": "Fantasy",
      "Year": 1997,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747532699"
    },
    "Harry Potter And The Chamber Of Secrets": {
      "Genre": "Fantasy",
      "Year": 1998,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747538493"
    },
    "Harry Potter And The Prisoner Of Azkaban": {
      "Genre": "Fantasy",
      "Year": 1999,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747542155"
    },
    "Harry Potter And The Goblet Of Fire": {
      "Genre": "Fantasy",
      "Year": 2000,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747546245"
    },
    "Harry Potter And The Order Of The Phoenix": {
      "Genre": "Fantasy",
      "Year": 2003,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747551003"
    }
  },
  "J.R.R. Tolkien": {
    "The Hobbit": {
      "Genre": "Fantasy",
      "Year": 1937,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928227"
    },
    "The Fellowship Of The Ring": {
      "Genre": "Fantasy",
      "Year": 1954,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928210"
    },
    "The Two Towers": {
      "Genre": "Fantasy",
      "Year": 1954,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928203"
    },
    "The Return Of The King": {
      "Genre": "Fantasy",
      "Year": 1955,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928197"
    },
    "The Silmarillion": {
      "Genre": "Fantasy",
      "Year": 1977,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780618126989"
    }
  },
  "Agatha Christie": {
    "Murder On The Orient Express": {
      "Genre": "Mystery",
      "Year": 1934,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062693662"
    },
    "And Then There Were None": {
      "Genre": "Mystery",
      "Year": 1939,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062073488"
    },
    "The Murder Of Roger Ackroyd": {
      "Genre": "Mystery",
      "Year": 1926,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062693662"
    },
    "Death On The Nile": {
      "Genre": "Mystery",
      "Year": 1937,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062073556"
    },
    "The ABC Murders": {
      "Genre": "Mystery",
      "Year": 1936,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062073563"
    }
  },
  "Stephen King": {
    "The Shining": {
      "Genre": "Horror",
      "Year": 1977,
      "Publisher": "Doubleday",
      "ISBN": "9780307743657"
    },
    "It": {
      "Genre": "Horror",
      "Year": 1986,
      "Publisher": "Viking",
      "ISBN": "9781501142970"
    },
    "Misery": {
      "Genre": "Psychological Horror",
      "Year": 1987,
      "Publisher": "Viking",
      "ISBN": "9780450417399"
    },
    "Pet Sematary": {
      "Genre": "Horror",
      "Year": 1983,
      "Publisher": "Doubleday",
      "ISBN": "9781501156700"
    },
    "Doctor Sleep": {
      "Genre": "Horror",
      "Year": 2013,
      "Publisher": "Scribner",
      "ISBN": "9781476727653"
    }
  }
}




# library = {
#   "J.K. Rowling": [
#     {
#       "title": "Harry Potter and the Sorcerer's Stone",
#       "genre": "Fantasy",
#       "year": 1998,
#       "publisher": "Bloomsbury",
#       "ISBN": "978-0747532699",
#     },
#     {
#       "title": "Harry Potter and the Chamber of Secrets",
#       "genre": "Fantasy",
#       "year": 1999,
#       "publisher": "Bloomsbury",
#       "ISBN": "978-0747538494",
#     },
#     {
#       "title": "Harry Potter and the Prisoner of Azkaban",
#       "genre": "Fantasy",
#       "year": 1999,
#       "publisher": "Bloomsbury",
#       "ISBN": "978-0747542699",
#     },
#   ],
#   "J.R.R. Tolkien": [
#     {
#       "title": "The Hobbit",
#       "genre": "Fantasy",
#       "year": 1937,
#       "publisher": "George Allen & Unwin",
#       "ISBN": "978-0547928227",
#     },
#     {
#       "title": "The Lord of the Rings",
#       "genre": "Fantasy",
#       "year": 1954,
#       "publisher": "George Allen & Unwin",
#       "ISBN": "978-0544003415",
#     },
#     {
#       "title": "The Silmarillion",
#       "genre": "Fantasy",
#       "year": 1977,
#       "publisher": "George Allen & Unwin",
#       "ISBN": "978-0544003438",
#     },
#   ],
#   "George Orwell": [
#     {
#       "title": "1984",
#       "genre": "Dystopian",
#       "year": 1949,
#       "publisher": "Secker & Warburg",
#       "ISBN": "978-0451524935",
#     },
#     {
#       "title": "Animal Farm",
#       "genre": "Political Satire",
#       "year": 1945,
#       "publisher": "Secker & Warburg",
#       "ISBN": "978-0451526342",
#     },
#     {
#       "title": "Homage to Catalonia",
#       "genre": "Political Non-fiction",
#       "year": 1938,
#       "publisher": "Secker & Warburg",
#       "ISBN": "978-0141182711",
#     },
#   ],
#   "Jane Austen": [
#     {
#       "title": "Pride and Prejudice",
#       "genre": "Romance",
#       "year": 1813,
#       "publisher": "T. Egerton",
#       "ISBN": "978-0141439518",
#     },
#     {
#       "title": "Sense and Sensibility",
#       "genre": "Romance",
#       "year": 1811,
#       "publisher": "T. Egerton",
#       "ISBN": "978-0141439662",
#     },
#     {
#       "title": "Emma",
#       "genre": "Romance",
#       "year": 1815,
#       "publisher": "John Murray",
#       "ISBN": "978-0141439587",
#     },
#   ],
#   "Agatha Christie": [
#     {
#       "title": "Murder on the Orient Express",
#       "genre": "Mystery",
#       "year": 1934,
#       "publisher": "Collins",
#       "ISBN": "978-0062693556",
#     },
#     {
#       "title": "And Then There Were None",
#       "genre": "Mystery",
#       "year": 1939,
#       "publisher": "Collins",
#       "ISBN": "978-0062073556",
#     },
#     {
#       "title": "The ABC Murders",
#       "genre": "Mystery",
#       "year": 1936,
#       "publisher": "Collins",
#       "ISBN": "978-0062074002",
#     },
#   ],
# }

# for author, books in library.items():
#     for book in books:
#         print(book["title"])

# for author, books in library.items():
#     for title in books:
#         print(title)

# update publisher:

# author = "George Orwell"
# target = "1984"
# update = "Penguin"


# for book in library.get(author, []):
#     if book["title"] == target:
#         book["publisher"] = update
#         break
        
#  library["George Orwell"]["1984"]["publisher"] = "penguin". 


