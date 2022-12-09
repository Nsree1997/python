print("navyasree")
print('navyasree')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "hi,navyasree!"
print(a[1])

for x in "banana":
  print(x) 

a = "Hello, World!"
print(len(a))

txt = "i am navya sree!"
print("sree" in txt)

txt = "i am navya sree!"
if "sree" in txt:
    print("yes,sree is present")

age = 36
txt = "My name is John, I am {}"
print(txt.format (age))   

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
