#https://www.kaggle.com/learn/python

#1. Hello, Python
spamamount = 0
print(spamamount) #print 0
print(type(spamamount)) #print <class 'int'>
spamamount = spamamount + 4
if spamamount > 0:
	print("But I don't want any spam") #print But I don't want any spam
vikingsong = "Spam"*spamamount
print(vikingsong) #print SpamSpamSpamSpam
print(5/2) #print 2.5
print(6/2) #print 3.0
print(5//2) #print 2 #floor division removes fractional parts
print(6//2) #print 3 #floor division removes fractional parts
#some built-in functions
print(min(1, 2, 3)) #print 1
print(max(1, 2, 3)) #print 3
print(abs(32)) #print 32
print(abs(-32)) #print 32
print(float(10)) #print 10.0
print(int(3.33)) #print 3
print(int(7.87)) #print 7
#Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.  Write an arithmetic expression below to calculate how many candies they must smash for a given haul.
alice_candies = 121
bob_candies = 77
carol_candies = 109
candiessmashed = (alice_candies+bob_candies+carol_candies) % 3
print(candiessmashed) #print 1
print(7------3) #print 10