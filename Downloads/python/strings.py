name=("Muahammed Shanib p")
print(name.upper())

### A student's registered email is "student@gmail.com". Store it and print how many
###characters it contains
email = ("student@gmail.com")
print(len("student@gmail.com"))

###A customer left this feedback: " Amazing product, highly recommend! ". Store it and
###print it without the extra spaces at the start and end.
feedback = (" Amazing product, highly recommend! ")
print(feedback.strip())

###Ask the user to enter a book title in lowercase (for example, "the alchemist") and
###print it the way it would appear on a book cover, with each word capitalized.
Title = 'the alchemist'
print(Title.title())

###A company slogan is stored as "We build apps for Java developers". Print the
###slogan after replacing "Java" with "Python".
slogan = 'we build apps for java developers'
print(slogan.replace('java','python'))

###Ask the user to enter their full name and print just the first 4 letters as their
##username.
fullName = (input('enter your full name : '))
print('username :',fullName[0:4])

###A teacher stores the subjects she teaches as one line of text:
#"Maths,Science,English,History". Print each subject separately.
subjects = "Maths,Science,English,History"

for subject in subjects.split(","):
    print(subject)

###Ask the user to enter a sentence and print the total number of words in it.
a = input('enter a sentence')
words = a.split()
print("total number of words :",len(words))

#Store the word "level". Print the word reversed, and also print whether the original
#word and the reversed word are exactly the same.
word = "level"
reversed_word = word[::-1]
print('reversed word :',reversed_word)
print('are they are same?',word == reversed_word)

##In the word "banana", print how many times the letter "a" appears.
word = "banana"
print(word.count("a"))

##Ask the user to enter their username and print whether it starts with the text
#"admin".
a = input('enter your name')
print(a.startswith("admin"))

#A user enters their date of birth as text in the format "17-09-2000". Print just the
#year part of it.
text = "17-09-2000"
print(text[6:10])
