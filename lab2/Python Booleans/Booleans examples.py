#1 Example
print("1 Example")

print(10>9) #will print True
print(10 == 9)#will print False
print(10 < 9) #will print false


#2 Example
print("2 Example")


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")#is true

print(bool("Hello"))#print true
print(bool(15))#print true

#3 example
print("3 Example")

x = "Hello"
y = 15

print(bool(x))#true
print(bool(y))#true

#4 example
print("4 Example")

bool("abc")#print true because isnt empty str
bool(123)#print true any number. except 0
bool(["apple", "cherry", "banana"])#print true any lists, except empty ones

#5 example
print("5 Example")

bool(False)#all will be False
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

#example 6
print("6 Example")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

#example 7
print("7 Example")

def myFunction() :
  return True

print(myFunction())

#example 8
print("8 Example")

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 

#example 9
print("9 Example")

x = 200
print(isinstance(x, int)) 