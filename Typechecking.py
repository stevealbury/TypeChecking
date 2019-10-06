#scratch script for trying stuff out
from allimports import pi
from allimports import circleArea
from allimports import Tuple
from allimports import List
from allimports import argv

from allimports import path

current_path = path

script = first = second  = "empty"
print(f"""the script is {script}
      the first arg is {first}
      the 2nd arg is {second}
      """)

a = circleArea(5)

#check the annotation types and docstring
print(circleArea.__annotations__)
print (a)
print(circleArea.__doc__)


#identifying types
b = 1.5
print(b)
print(type(b))

someList = ["test", 1, 'a', 5.5]
print(someList)
print(type(someList))

someType: Tuple[int, int, int] = (1,2,3)
print(someType)
print(type(someType))
someBool: bool = False
someBool2: bool = True
someBool3: bool = False
#can coerce values - called 'casting' in some languages

someList = list(someType)
x = 1
z = 1
print(id(x))
print(id(z))
eval_mystring = "that joke isn't funny anymore {}"

print(f"here is the text of {someType}")
print(rf'a raw string with backslashes in it \t' )
print(rf"here is a backslash \n \\ and a variable {eval_mystring.format(someBool)}")


print(id(someBool))
print(id(someBool2))
print(id(someBool3))

print("?" * 10)

#just a string with formatting code - can then use format method to add correct number of args
threeArgs = "{} {} {}"
a = 2
b = 4
c = 'six'


asf = "& "
bsf = "&"
csf = "longer string"
dsf = "longer string"

print(asf, bsf, id(asf), id(bsf))
print(csf, dsf, id(csf), id(dsf))
print( threeArgs.format( a, b, c ) )
print("type something here >>>> ", end = '')
#myinput = input('|')
#print(myinput,'\n')

#filter for numeric input
print ("salary? ===> ", end = '')
#salary = input('> ')
#print(salary + '\n')
