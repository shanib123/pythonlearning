#1. A user wants to save their top 3 favourite movies. Take all three as input from the
#user, one by one, store them in a list, and print the list.
a = input('enter your 1st favourite movie')
b = input('enter your 2nd favourite movie')
c = input('enter your 3rd favourite movie')
print(list((a,b,c)))

#A small shop's daily sales for a week are recorded as [1200, 1500, 900, 1700, 1100,
#2000, 1800]. Store this and print the sales of the highest and the lowest day.
WeeklySales = [1200,1500,900,1700,1100,2000,1800]
print('Sales of the highest day : ',max(WeeklySales))
print('sales of the lowest day : ',min(WeeklySales))

#A grocery list is ["Milk", "Bread", "Eggs"]. The customer forgot to add "Butter" — add
#it to the end of the list and print the updated list.
GroceryList = ["Milk" , "Bread" , "Eggs"]
GroceryList.append("Butter")
print(GroceryList)

#A teacher recorded these marks: [56, 78, 45, 90, 67]. Print the total and the average
#mark.
marks = [56, 78, 45, 90, 67]
print('total marks : ',sum(marks))
Number_of_Marks = len(marks)
averageMarks = (sum(marks)/Number_of_Marks)
print('average marks : ',averageMarks)

#A playlist contains ["Song A", "Song B", "Song C", "Song D"]. The user wants "Song
#C" removed from it — update the list and print the result.
playlist = ["Song A", "Song B", "Song C", "Song D"]
a = 'Song C'
playlist.remove(a)
print(playlist)

#A list of ages is [15, 22, 34, 45, 19]. Print the ages arranged from smallest to largest.
ages = [15, 22, 34, 45, 19]
ages.sort()
print(ages)

#A cricket team lineup is ["Rahul", "Aman", "Vikram", "Sunil", "Ravi"]. The captain,
#"Vikram", got injured before the match, so he needs to be replaced with "Kiran" without
#changing anyone else's position. Print the updated lineup.
lineup = ["Rahul", "Aman", "Vikram", "Sunil", "Ravi"]
lineup[2] ="kiran"
print(lineup)

#Two friends collected phone numbers separately: contacts1 = ["9998887771",
#"9998887772"] and contacts2 = ["9998887773", "9998887774"]. Combine both into a
#single list and print it.
list1 = ["9998887771","9998887772"]
list2 = ["9998887773", "9998887774"]
combination = list1+list2
print(combination)

#A list of exam scores is [88, 45, 67, 45, 92, 45]. Print how many students scored
#exactly 45.
list = [88, 45, 67, 45, 92, 45]
print('students scored exactly 45 :',list.count(45))

#A delivery app stores restaurant ratings as [4.5, 3.8, 4.9, 4.1, 3.5]. Print the highest
#rating among them.
ratings = [4.5, 3.8, 4.9, 4.1, 3.5]
print(max(ratings))

#A user enters 5 product prices one by one. Store them in a list and print the total
#bill amount.
prices = [
    float(input("Enter price 1: ")),
    float(input("Enter price 2: ")),
    float(input("Enter price 3: ")),
    float(input("Enter price 4: ")),
    float(input("Enter price 5: "))
]

print("Prices:", prices)
print("Total bill:", sum(prices))

#A list of usernames is ["admin", "guest123", "root", "test_user"]. Print the position of
#"root" in the list.
username = ["admin", "guest123", "root", "test_user"]
print(username.index("root"))



