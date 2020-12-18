#1, 2, 3 - Welcome the user, username & password, match inserted information with registered users
print("-" * 40)
print("Welcome to the app. Please log in:")
username = input("USERNAME: ")
password = input("PASSWORD: ")
registered_users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
if registered_users.get(username) == password:
    print("You are already registered user.")
else:
    print("Thank you for your registration. You are a new user.")
print("-" * 40)

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#4 - Select a paragraph
print("We have 3 texts to be analyzed.")
text_number = int(input("Enter a number btw. 1 and 3 to select: "))
print("-" * 40)

#Text split
selected_text = (TEXTS[text_number-1].split())

#5 - Number of words in selected paragraph
word_count = len(selected_text)
print("There are", word_count, "words in the selected text.")

#5 - Titlecase words
count_title = len([letter for letter in selected_text if letter[0].isupper()])
print("There are", count_title, "titlecase words.")

#5 - Uppercase words
count_upper = len([letter for letter in selected_text if letter.isupper()])
print("There are", count_upper, "uppercase words.")

#5 - Lowercase words
count_lower = len([letter for letter in selected_text if letter[0].islower()])
print("There are", count_lower, "lower words.")

#5 - Numeric strings
count_numbers = len([letter for letter in selected_text if letter.isnumeric()])
print("There are", count_numbers, "numeric strings.")
print("-" * 40)

#6 - Bar chart
clean_text = [word0.strip(',.!?') for word0 in selected_text]
letters_counts = {}
for i in clean_text:
    if len(i) not in letters_counts:
        letters_counts[len(i)] = 1
    else:
        letters_counts[len(i)]+=1
letters_counts = sorted(letters_counts.items(), key=lambda x:x[0])
for c in letters_counts:
    print (str(c[0]), ("*" * c[1]),  str(c[1]))
print("-" * 40)

#7 - Sum of numbers in a text
text0 = TEXTS[0].split()
text1 = 0
for a in text0[15:45]:
  if a.isdigit():
    text1 += int(a)
print("If we summed all the numbers in this text we would get:", text1)
print("-" * 40)