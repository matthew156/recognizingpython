num1 = 42  #variable declaration, initialize number
num2 = 2.3 #variable declaration, initialize number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #prints to console, type check
print(pizza_toppings[1]) #prints to console and list acess value
pizza_toppings.append('Mushrooms') #list add value 
print(person['name'])  #print to console, dictionary access value
person['name'] = 'George' #Dictionary change value
person['eye_color'] = 'blue' #Dictionary change value
print(fruit[2]) #print to console, Tuple access data

if num1 > 45: #Conditional if, evaluation, print to console
    print("It's greater")
else: #Conditional statement if condition is not met, print to console
    print("It's lower")

if len(string) < 5: #Conditional if statement
    print("It's a short word!")
elif len(string) > 15: #Conditional if statement for an additional condition, print to console
    print("It's a long word!")
else: 
    print("Just right!")

for x in range(5): #loop starting from 0-5
    print(x)
for x in range(2,5): #loop starting from 2-5
    print(x)
for x in range(2,10,3): #loop starting from 2 but increments by 3 until the limit of 10 is reached
    print(x)
x = 0
while(x < 5): #While loop, variable declaration, print to console, and incrementing x 
    print(x)
    x += 1

pizza_toppings.pop() #takes off the last item in the array
pizza_toppings.pop(1) #takes off 'Sausage' from the array

print(person) #prints to console the person dictionary
person.pop('eye_color') #removes the eye_color object from the person dictionary
print(person) 

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue #continues going through the objects in pizza_toppings if 'Pepperoni is present
    print('After 1st if statement') #print statement
    if topping == 'Olives': #conditional if
        break #stops reading the line of code after 'Olives' is read

def print_hello_ten_times(): #function declaration, for loop starts at 0 goes up to 10
    for num in range(10):
        print('Hello')
#prints hello
print_hello_ten_times()
#calls function
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#prints hello
print_hello_x_times(4)
#prints hello with the amount given by the argument
def print_hello_x_or_ten_times(x = 10): #function declaration with default parameter
    for num in range(x): #for loop until x
        print('Hello')
#prints hello
print_hello_x_or_ten_times() #prints hello by default 10 times
print_hello_x_or_ten_times(4) #prints hello 4 times


"""
Bonus section
"""

# print(num3) num 3 should be above the print command
# num3 = 72
# fruit[0] = 'cranberry' fruit has already been declared must append or change the original array
# print(person['favorite_team']) there is no favorite team for the object person
# print(pizza_toppings[7]) index starts at 0 with a max of 4
#   print(boolean)  just remove the space between the print function
# fruit.append('raspberry') tuples are an immutable property
# fruit.pop(1) tuples are an immutable property