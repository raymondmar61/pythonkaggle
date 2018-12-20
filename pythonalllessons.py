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

#2. Exercise: Syntax, Variables, and Numbers
#Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.  Write an arithmetic expression below to calculate how many candies they must smash for a given haul.
alice_candies = 121
bob_candies = 77
carol_candies = 109
candiessmashed = (alice_candies+bob_candies+carol_candies) % 3
print(candiessmashed) #print 1
print(7------3) #print 10

#3. Functions And Getting Help
#The help() function is possibly the most important Python function you can learn. If you can remember how to use help(), you hold the key to understanding just about any other function in Python.  For example abs().
#print(help(abs)) #display Help on built-in function abs in module builtins:  abs(x, /)  Return the absolute value of the argument.  #press q to exit.
def least_difference(a, b, c):
	diff1 = abs(a-b)
	diff2 = abs(b-c)
	diff3 = abs(a-c)
	return min(diff1, diff2, diff3)
print(least_difference(1, 10, 100)) #print 9
print(least_difference(1, 10, 100), least_difference(1, 10, 10), least_difference(5, 6, 7)) #print 9 0 1
#print(help(least_difference)) #print Help on function least_difference in module __main__:\n  least_difference(a, b, c)
def least_differencehelp(a, b, c):
	"""help definition finds lowest difference combination"""
	diff1 = abs(a-b)
	diff2 = abs(b-c)
	diff3 = abs(a-c)
	return min(diff1, diff2, diff3)
#print(help(least_differencehelp)) #print Help on function least_differencehelp in module __main__:\n least_differencehelp(a, b, c)\n help definition finds lowest difference combination
#We can specify a value for sep to put some special string in between our printed arguments.  A seperator.  No sep the default is a single space ' '.
print(1, 2, 3, sep="<") #print 1<2<3
print(1, 2, 3, sep="  ") #print 1  2  3
print(1, 2, 3, sep="__") #print 1__2__3
#Function with a default value
def defaultvalue(who="Colin"):
	print("Hello {}".format(who))
defaultvalue("Jake") #return Hello Jake
defaultvalue() #return Hello Colin
#Function is an object, too.  Function has a type.
def f(n):
	return n*2
x = 12.5
print(type(f), type(x), sep="\n") #print <class 'function'>\n <class 'float'>
print((f), (x), sep="\n") #print <function f at 0x7f5c28b43840>\n 12.5
#We can call the function we receive as an argument.  RM:  a function argument calls the function at the return statement?
def call(fn, arg):
	"""call fn on arg"""
	return fn(arg)
print(call(f, 1)) #print 2
print(call(f, 1)) #print 2
print(call(f, 2)) #print 4
print(call(f, 20)) #print 40
#print(call(g, 1)) #print error message
#print(call(abcd, 2)) #print error message
def squaredcall(fn, arg):
    """Call fn on the result of calling fn on arg"""    
    return fn(fn(arg))
print(squaredcall(f,10)) #print 40
print(squaredcall(f,60)) #print 240
#If we pass in a function using the optional key argument, it returns the argument x that maximizes key max(,key=) (aka the 'argmax').
def mod5(x):
	return x % 5
print(max(100, 51, 14)) #print 100
print(max(100, 51, 14, key=mod5)) #print 14
print(51 % 5) #print 1
print(14 % 5) #print 4
#Lambda functions.  If you're writing a short throwaway function whose body fits into a single line, Python's lambda syntax is conveniently compact.
mod5lambda = lambda x: x % 5
print(mod5lambda(101)) #print 1
print(mod5lambda(100)) #print 0
print(mod5lambda(51)) #print 1
print(mod5lambda(14)) #print 4
absolutedifference = lambda a, b: abs(a-b)
print(absolutedifference(5, 7)) #print 2
always32 = lambda: 32
print(always32()) #print 32
#With judicious use of lambdas, you can occasionally solve complex problems in a single line.
names = ['jacques', 'Ty', 'Mia', 'pui-wa']
print("Longest name is:", max(names, key=lambda name: len(name))) #print Longest name is: jacques
print("Names sorted case insensitive:", sorted(names, key=lambda name: name.lower())) #print Names sorted case insensitive: ['jacques', 'Mia', 'pui-wa', 'Ty']

#4 Exercise: Functions and Getting Help
def roundtwodecimalplaces(num):
	return round(num,2)
print(roundtwodecimalplaces(104.5689)) #print 104.57
print(roundtwodecimalplaces(104.5426)) #print 104.54
print(round(153.5689,-2)) #print 200
print(round(143.5426,-2)) #print 100
print(round(155.5689,-1)) #print 160
print(round(153.5426,-1)) #print 150
#In the last exercise, I introduced candy-sharing friends Alice, Bob and Carol. As a reminder, they have some candies which they plan to split evenly among themselves. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
#Earlier, you wrote some code to calculate how many candies they'd have to smash, assuming they collected a particular number.
#Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
def smashcandies(totalcandies, numberoffriends=3):
	return totalcandies % numberoffriends
print(smashcandies((121+77+109),3)) #print 1
print(smashcandies((121+77+109),5)) #print 2
#continue #5