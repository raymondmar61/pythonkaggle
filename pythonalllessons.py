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

#8. Exercise: Lists
def seconditem(inputlist):
	if len(inputlist) == 1:
		return None
	else:
		return inputlist[1]
desktoplist = ["Dell","HP","Apple","Alienware"]
print(seconditem(desktoplist)) #print HP
oneitem = ["good"]
print(seconditem(oneitem)) #print None
#Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that. These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.  Select the **captain** of the worst team.
def captainworseteam(teamslist):
	#get number of teams len(teamslist)
	numberofteams = len(teamslist)
	#get captain worse team
	return (teamslist[numberofteams-1][1])	
team1 = ["coach1","captain1","player11","player12","player13","player14","player15"]
team2 = ["coach2","captain2","player22","player22","player23","player24","player25"]
team3 = ["coach3","captain3","player33","player32","player33","player34","player35"]
allteams = [team1, team2, team3]
print(allteams) #print [['coach1', 'captain1', 'player11', 'player12', 'player13', 'player14', 'player15'], ['coach2', 'captain2', 'player22', 'player22', 'player23', 'player24', 'player25'], ['coach3', 'captain3', 'player33', 'player32', 'player33', 'player34', 'player35']]
print(len(allteams)) #print 3
print(captainworseteam(allteams)) #print captain3
#The next iteration of Mario Kart will feature an extra-infuriating new item, the *Purple Shell*. When used, it warps the last place racer into first place and the first place racer into last place. Complete the function below to implement the Purple Shell's effect.
def purpleshell(mariokartracerslist):
	print("Start race:",", ".join(mariokartracerslist))
	newfirstplace = mariokartracerslist[-1]
	newlastplace = mariokartracerslist[0]
	#a = 1 b = 0 a, b = b, a.
	mariokartracerslist[0], mariokartracerslist[-1] = newfirstplace, newlastplace
	#mariokartracerslist[0] = newfirstplace
	#mariokartracerslist[-1] = newlastplace
	print("End race:",", ".join(mariokartracerslist))	
racers = ["Mario","Bowser","Luigi","Toad","Peach","Koopa Trooper","Donkey Kong"]
purpleshell(racers) #return Start race: Mario, Bowser, Luigi, Toad, Peach, Koopa Trooper, Donkey Kong\n End race: Donkey Kong, Bowser, Luigi, Toad, Peach, Koopa Trooper, Mario
#What are the lengths of the following lists?
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]
print(len(a)) #print 3
print(len(b)) #print 2
print(len(c)) #print 0
print(len(d)) #print 2
print(d) #print [2:3]
#A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). [May and] Mona and Gilbert are the only guests who were fashionably late.  Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.  RM:  May counts as fashionably late because 4/7=.57 or at least half.
def fashionablylate(arrivals, name): #RM:  function inputs are arrivals and name
	partycount = len(arrivals)
	arrivalnumber = arrivals.index(name)+1
	if arrivalnumber/partycount == 1.0:
		print(name+" is the last to arrive.")
	elif arrivalnumber/partycount >.50:
		print("{} is fashionably late.".format(name))
	else:
		print("{} is on time.".format(name))
partyattendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
for eachpartyattendees in partyattendees:
	fashionablylate(partyattendees, eachpartyattendees) #return Adela is on time.\n Fleda is on time.\n Owen is on time.\n May is fashionably late.\n Mona is fashionably late.\n Gilbert is fashionably late.\n Ford is the last to arrive.

#9. Loops And List Comprehensions
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for eachplanets in planets:
	print(eachplanets, end=" ") #print Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for eachmultiplicands in multiplicands:
	product = product * eachmultiplicands
print(product) #print 360
loopstring = "The quick brown fox"
for eachloopstring in loopstring:
	print(eachloopstring, end=",") #print T,h,e, ,q,u,i,c,k, ,b,r,o,w,n, ,f,o,x,
s = "steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video."
for eachs in s:
	if eachs.isupper():
		print(eachs) #print H\n E\n L\n L\n O
print(range(0,5)) #print range(0, 5)
rangezerofive = range(0,5)
print(rangezerofive) #print range(0, 5)
print(list(range(0,5))) #print [0, 1, 2, 3, 4]  RM:  brain freeze.  print(range(0,5)) #print range(0, 5) obviously is incorrect.
realrangezerofive = [x for x in range(0,5)]
print(realrangezerofive) #print [0, 1, 2, 3, 4]
#enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
#We don't want the user to see things listed from index 0, since this looks unnatural. Instead, the items should appear to start at index 1. Modify the print statement to reflect this behavior by adding "+ 1.
#Finding the index of an item in a list
singledigits = list(range(0,10))
print(singledigits) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#for loop double each odd number in singledigits list
for i, eachsingledigits in enumerate(singledigits):
	if eachsingledigits % 2 == 1:
		singledigits[i] = eachsingledigits * 2
print(singledigits) #print [0, 2, 2, 6, 4, 10, 6, 14, 8, 18]
seeindexnumbersinlist = ["UNO","DOS","Dixit","X-Men","Chess"]
print(list(enumerate(seeindexnumbersinlist))) #print [(0, 'UNO'), (1, 'DOS'), (2, 'Dixit'), (3, 'X-Men'), (4, 'Chess')]
for i, eachseeindexnumbersinlist in enumerate(seeindexnumbersinlist):
	if i == 2:
		print(eachseeindexnumbersinlist) #print Dixit
x = 0.125
numerator, denominator = x.as_integer_ratio()
print(numerator) #print 1
print(denominator) #print 8
romannumbers = [('one', 1, 'I'),('two', 2, 'II'), ('three', 3, 'III'), ('four', 4, 'IV')]
for word, numbers, roman in romannumbers:
	print(word, numbers, roman, sep="=", end="; ") #print one=1=I; two=2=II; three=3=III; four=4=IV;
i = 0
while i < 10:
	print(i, end=" ") #print 0 1 2 3 4 5 6 7 8 9
	i += 1
#list comprehension
squares = [n**2 for n in range(0,10)]
print(squares) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
shortplanets = [eachplanets for eachplanets in planets if len(eachplanets) < 6]
print(shortplanets) #print ['Venus', 'Earth', 'Mars']
from statistics import mean
numbers = [1,5,9,8,6,5,1,5,9,2,4,8]
belowaveragenumbers = [eachnumbers for eachnumbers in numbers if eachnumbers < mean(numbers)]
print(belowaveragenumbers) #print [1, 5, 5, 1, 5, 2, 4]
from random import randint
counter = randint(10,20)
numberslist = [randint(-10,10) for n in range(0,counter)]
print(numberslist) #print [-1, 4, -1, 5, 3, 2, -10, 6, 9, 8, 3, -2, 9, 0, 3, 9, -3, -10]
positivenumberslist = [eachnumberslist for eachnumberslist in numberslist if eachnumberslist >=0]
print(positivenumberslist) #print [4, 5, 3, 2, 6, 9, 8, 3, 9, 0, 3, 9]

#10. Exercise: Loops And List Comprehensions
#Try to identify the bug and fix it in the cell below
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    print(nums)
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
print(has_lucky_number([7,11,14,170])) #print True  RM:  The answer is the return True and return False stops the for loop after the first item in list nums; in particular, if the first item in has_lucky_number is not divisible by seven and another item is divisible by seven, then for loop stops at first item return False.  The return causes a function to exit immediately.
#print([1, 2, 3, 4] > 2) #print TypeError: '>' not supported between instances of 'list' and 'int'
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is True if L[i] is greater than thresh, and False otherwise.    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    answer = []
    for eachL in L:
    	if eachL > thresh:
    		answer.append(True)
    	else:
    		answer.append(False)
    print(answer)
elementwise_greater_than([1, 2, 3, 4],2) #return [False, False, True, True]
from collections import Counter
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the same meal has ever been served two days in a row, and False otherwise.  RM:  return a list of meals served two or more times."""
    duplicatemeal = []    
    counterdictionary = Counter(meals)
    for item, value in counterdictionary.items():
    	if value >= 2:
    		duplicatemeal.append(item)
    print(duplicatemeal)
menu_is_boring(["walffles","bacon","pancakes","steak","French Fries","hamburger","broccoli","sausage","sushi","pancakes","steak","green beans","chow mein","chow mein","apples","pancakes"]) #return ['pancakes', 'steak', 'chow mein']
menu_is_boring(["apples","orange","chicken fried steak","tacos","pizza"]) #return []

#11. Strings and Dictionaries
print("A reminder of an escape character use backslash \\ \' \".")
triplequotes = """Hello
World"""
print(triplequotes) #print Hello\n World
print("""Triple Quotes 
Okie dokey '" """) #print Triple Quotes\n Okie dokey '"
print("Word Number Roman", sep="=", end="; ") #print Word Number Roman;
planet = "Pluto"
print(planet[-3:]) #print uto
print(planet[2:]) #print uto
print(planet[:-3]) #print Pl
print(planet[0:2]) #print Pl
print(planet[::-1]) #print otulP
print([eachplanet+"!" for eachplanet in planet]) #print ['P!', 'l!', 'u!', 't!', 'o!']
#Strings are immutable.  We can't modify them.
#planet[0] = "B"  #returns error message 'str' object does not support item assignment
claimplanet = "Pluto is a planet!"
print(claimplanet.upper()) #print PLUTO IS A PLANET!
print(claimplanet.lower()) #print pluto is a planet!
print(claimplanet.index("plan")) #print 11 #RM:  plan starts at index position 11
print(claimplanet.startswith(planet)) #print True
print(claimplanet.startswith("Pluto")) #print True
print(claimplanet.startswith("Zebra")) #print False
print(claimplanet.endswith("planet!")) #print True
splitclaimplanet = claimplanet.split()
print(splitclaimplanet) #print ['Pluto', 'is', 'a', 'planet!']
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year) #print 1953
print(month) #print 01
print(day) #print 03
print(" ".join(splitclaimplanet)) #print Pluto is a planet!
position = 9
print(planet+" you'll always be the " +str(position)+"th planet to me.") #print Pluto you'll always be the 9th planet to me.
print("{} you'll always be the {}th planet to me.".format(planet,position)) #print Pluto you'll always be the 9th planet to me.  Notice how we didn't even have to call str() to convert position 9 from an int. format() takes care of that for us.
plutomass = 1.303 * (10**22)
earthmass = 5.9722 * (10**24)
population = 52910390
print("{:.2} two decimal places.  {:.3} three decimal places, {:.3%} three decimal places as percent.  {:,} separate with commas".format(plutomass, earthmass, plutomass/earthmass, population)) #print 1.3e+22 two decimal places.  5.97e+24 three decimal places, 0.218% three decimal places as percent.  52,910,390 separate with commas
print("Pluto is a {0}  No it's a {1}.  {0}.  {1}".format("planet","dwarf planet")) #print Pluto is a planet  No it's a dwarf planet.  planet.  dwarf planet

numbersdictionary = {'one':1, 'two':2, 'three':3}
print(numbersdictionary["one"]) #print 1
numbersdictionary["eleven"] = 11
print(numbersdictionary) #print {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}
numbersdictionary["one"] = "Pluto"
print(numbersdictionary) #print {'one': 'Pluto', 'two': 2, 'three': 3, 'eleven': 11}
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planetsdictionary = {}
planetsdictionary.update({"Mercury":"M"})
planetsdictionary["Venus"] = "V" 
print(planetsdictionary) #print {'Mercury': 'M', 'Venus': 'V'}
#dictionary comprehension
planetdictionarycomprehension = {eachplanet:eachplanet[0] for eachplanet in planets}
print(planetdictionarycomprehension) #print {'Mercury': 'M', 'Venus': 'V', 'Earth': 'E', 'Mars': 'M', 'Jupiter': 'J', 'Saturn': 'S', 'Uranus': 'U', 'Neptune': 'N'}
numbersdictionary = {'one':1, 'two':2, 'three':3}
for key in numbersdictionary:
	print("{} = {}".format(key,numbersdictionary[key])) #print one = 1\n two = 2\n three = 3
print(" ".join(planetdictionarycomprehension.values())) #print M V E M J S U N
for planet, initial in planetdictionarycomprehension.items(): #planet is key, initial is value in for key, value in planetdictionarycomprehension.itmes():
	print("{} begins with {}".format(planet, initial)) #print Mercury begins with M\n Venus begins with V . . . Neptune begins with N

#12. Exercise: Strings and Dictionaries
a = ""
print(len(a)) #print 0
a = "\n"
print(len(a)) #print 1 The newline character is just a single character! (Even though we represent it to Python using a combination of two characters.)
#Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.
def isvalidzip(zipcode):	
	if len(zipcode) != 5:
		print("Not a valid zip code")
	elif zipcode.isdigit() is True:	
		print("Valid zip code")		
	else:
		print("Not a valid zip code")
isvalidzip("12345") #print Valid zip code
isvalidzip("abcdo") #print Not a valid zip code
isvalidzip("12io0") #print Not a valid zip code
isvalidzip("12io0pop") #print Not a valid zip code
isvalidzip("946") #print Not a valid zip code
#A researcher has gathered thousands of news articles. Wants articles including a specific word.  Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword "closed", you would not include the string "enclosed."  She does not want you to distinguish upper case from lower case letters. So the phrase "Closed the case." would be included when the keyword is "closed".  Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is "closed". But you can assume there are no other types of punctuation.
def wordsearch(document, keyword):
	document = document.lower()
	document = document.replace(".","") #RM:  split includes punctuation marks next to a string
	document = document.replace(",","") #RM:  split includes punctuation marks next to a string
	for eachdocument in document.split():
		if keyword == eachdocument:
			print("{} is found using split()".format(keyword))
			break
wordsearch("The Learn Python Challenge Casino.","casino") #print casino is found using split()
wordsearch("They bought a car","casino") #print
wordsearch("Casinoville","casino") #print
#RM:  Can't use .find() because .find() returns index number 0 in Casinoville
#The researcher wants to supply multiple keywords to search for.
def multiplewordsearch(document, keywords):
	document = document.lower()
	document = document.replace(".","")
	document = document.replace(",","")
	if any(eachkeywords in document.split() for eachkeywords in keywords):
		print(keywords,"is in")
	for eachdocument in document.split():
		for eachkeywords in keywords:
			if eachkeywords == eachdocument:
				print("{} is found using split()".format(eachkeywords))
keywords = ["casino", "they"]
multiplewordsearch("The Learn Python Challenge Casino.",keywords) #print ['casino', 'they'] is in\n casino is found using split()
multiplewordsearch("They bought a car",keywords) #print ['casino', 'they'] is in\n they is found using split()
multiplewordsearch("Casinoville",keywords) #print
#official solution using function wordsearch
def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = wordsearch(documents, keyword)
    return keyword_to_indices
#start 13. Working with External Libraries