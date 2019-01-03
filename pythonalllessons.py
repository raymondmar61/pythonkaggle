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

#4. Exercise: Functions and Getting Help
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

#5. Booleans and Conditionals
def canrunforpresident(age):
	return age >=35
print("Can a 19 year old run fore President?",canrunforpresident(19)) #print Can a 19 year old run fore President? False
print("Can a 45 year old run fore President?",canrunforpresident(45)) #print Can a 45 year old run fore President? True
print(3.0==3) #print True
def isodd(n):
	return (n % 2) == 1
print(isodd(100)) #print False
print(isodd(5)) #print True
def canrunforpresident2(age, citizen):
	return age >=35 and citizen=="yes"
print(canrunforpresident2(19,"yes")) #print False
print(canrunforpresident2(50,"no")) #print False
print(canrunforpresident2(65,"yes")) #print True
def canrunforpresident3(age, citizen):
	return age >=35 and citizen
print(canrunforpresident3(65,True)) #print True
print(canrunforpresident3(19,True)) #print False
print(canrunforpresident3(50,False)) #print False
#and has a higher precedence than or; e.g True or True and False.  Answer is True.
def conditionals(x):
	if x == 0:
		print(x,"is zero")
	elif x > 0:
		print(x,"is positive")
	elif x < 0:
		print(x,"is negative")
	else:
		print(x,"is something else")
conditionals(0) #return 0 is zero
conditionals(-15) #return -15 is negative
conditionals(2303) #return 2303 is positive
#Boolean conversion
print(1) #print 1
print(bool(1)) #print True
print(bool(0)) #print False
print(bool("all strings are treated as true except the empty string \"\"")) #print True
print(bool("")) #print False
#We can use non-boolean objects in if conditions and other places where a boolean would be expected. Python will implicitly treat them as their corresponding boolean value.
if 0:
	print(0)
elif "spam":
	print("spam") #print spam
if 0:
	print(0)
if bool(0)==False:
	print(0) #print 0
if 1:
	print("1 love") #print 1 love
if "text":
	print("True text") #print True text

#6. Exercise: Functions and Getting Help
def sign(n):
	if n < 0:
		return -1
	elif n == 0:
		return 0
	elif n > 0:
		return 1
	else:
		return ("What is this?")
print(sign(5288)) #print 1
print(sign(-100)) #print -1
print(sign(0)) #print 0
def tosmash(totalcandies):
	print("Splitting",totalcandies,"candies.  Number of candies remained")
	return totalcandies % 3
print(tosmash(91)) #print Splitting 91 candies.  Number of candies remained\n 1
def tosmash2(totalcandies):
	if totalcandies == 1:
		return "Splitting 1 candy."
	elif totalcandies % 3 == 1:
		print("Splitting",totalcandies,"candies.  Number of candy remained")
		return totalcandies % 3
	else:
		print("Splitting",totalcandies,"candies.  Number of candies remained")
		return totalcandies % 3
print(tosmash2(91)) #print Splitting 91 candies.  Number of candies remained\n 1
print(tosmash2(101)) #print Splitting 91 candies.  Number of candies remained\n 2
print(tosmash2(1)) #print Splitting 1 candy.

#7. Lists
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
hands = [
    ["J", "Q", "K"],
    ["2", "2", "2"],
    ["6", "A", "K"], # (Comma after the last element is optional)
]
#I could also have written this on one line, but it can get hard to read
hands = [["J", "Q", "K"], ["2", "2", "2"], ["6", "A", "K"]]
print(planets[0]) #print Mercury
print(planets[1]) #print Venus
print(planets[-1]) #print Neptune
print(planets[-2]) #print Uranus
print(planets[0:3]) #print ['Mercury', 'Venus', 'Earth']
print(planets[:3]) #print ['Mercury', 'Venus', 'Earth']
print(planets[3:]) #print ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[1:len(planets)-1]) #print ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[1:-1]) #print ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[-4:]) #print ['Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets[3] = "Malacandra"
print(planets) #print ['Mercury', 'Venus', 'Earth', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets[0:3] = ["Mer","Ven","Ear"]
print(planets) #print ['Mer', 'Ven', 'Ear', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets[0:5]) #print ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
print(sorted(planets)) #print ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
planets.append("Pluto")
print(planets) #print ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planets.pop()
print(planets) #print ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#planets[len(planets)] = "Pluto" #RM:  can't add item to a list using listname[next avaiallbe index number]=item
print(planets.index("Earth")) #print 2
print("Earth" in planets) #print True
print("Pluto" in planets) #print False
#print(help(planets)) #print tell us about all the list methods
primes = [2, 3, 5, 7]
print(sum(primes)) #print 17
print(max(primes)) #print 7
print(min(primes)) #print 2
#tuples use parantheses and cannot be modified or are immutable
numbertuple = (1, 2, 3)
print(numbertuple) #print (1, 2, 3)
#Tuples are often used for functions that have multiple return values.
x = 0.5
print(x.as_integer_ratio()) #print (1, 2)
x = 0.125
print(x.as_integer_ratio()) #print (1, 8)
numerator, denominator = x.as_integer_ratio()
print(numerator) #print 1
print(denominator) #print 8
print(numerator/denominator) #print 0.125
#swapping two variables
a = 1
b = 0
a, b = b, a
print(a) #print 0
print(b) #print 1
#start 8. Exercise: Lists