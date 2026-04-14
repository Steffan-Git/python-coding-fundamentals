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

JacksBookshop = {
  "author1": {
  "name": "Rick Riordan",
  "book1": "The Lightning Thief", 
  "book2": "The Sea of Monsters", 
  "book3": "The Last Olympian",
},
  "author2": {
  "name": "Jonathan Haidt",
  "book1": "The Happiness Hypothesis", 
  "book2": "The Righteous Mind",
  "book3": "The Anxious Generation",  
},
  "author3": {
  "name": "Colleen Hoover", 
  "book1": "It Ends With Us",
  "book2": "Verity",
  "book3": "Hopeless",    
}
}
y = JacksBookshop.get("author2").get("name")
print(y)

record  = JacksBookshop.get("author2")

list_to_print = []

for k, v in record.items():
    if "book" in k:
        list_to_print.append(v)

print(", ".join(list_to_print))


a full book schema:
- authors/books(title, type, year, genre, publisher, ISBN)
5 authors 3 books each. 