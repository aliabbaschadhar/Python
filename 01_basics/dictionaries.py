chai_types={"Masala":"Spicy","Ginger":"Zesty", "Green":"Mild"}

print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
print(chai_types["Masala"]) #Spicy
print(chai_types["Ginger"]) # Zesty
print(chai_types["Green"]) #Mild

print(chai_types.get("Masala")) #Spicy

#!        Dictionaries are mutable

chai_types["Green"] = "fresh"
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'fresh'}

for chai in chai_types:
    print(chai) 
    # Masala
    # Ginger
    # Green

for chai in chai_types:
    print(chai , " ", chai_types[chai]) 

# We can also use key,value syntax to print keys and values in dictionaries but in that case we consider on key and value as an item so we will use a method .items() with dictionary like chai_types.items()

for key, value in chai_types.items():
    print(key, " ", value)
    # Masala  Spicy
    # Ginger  Zesty
    # Green   fresh

# Conditionals 
if "Masala" in chai_types:
    print("Masala is in chai_types")
else:
    print("Masala is not in chai_types")

# Can also find length of dictionary

print(len(chai_types)) # 3

#Adding to dictionary

chai_types["Earl Gray"] = "Citrus"

print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'fresh', 'Earl Gray': 'Citrus'}

#Removing from dictionary

del chai_types["Earl Gray"]
# del keyword also remove the refrence of item in dictionary from memory  

print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'fresh'}

print(chai_types.pop("Masala")) # Spicy
print(chai_types) # {'Ginger': 'Zesty', 'Green': 'fresh'}

print(chai_types.popitem()) # {'Green': 'fresh'}

# Making Copy of dictionary

chai_types_copy = chai_types.copy() #This has made copy of the dictionary with same values but different reference, the main dictionary and the copy has different refrence

print(chai_types_copy) 

tea_shop = {"chai":{
    "Masala":"Spicy",
    "Ginger":"Zesty",
    "Green":"Mild"
},
"tea":{
    "Earl Gray":"Citrus",
    "Oolong":"Sweet",
    "Black":"Spicy"
}
}

print(tea_shop) # {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}, 'tea': {'Earl Gray': 'Citrus', 'Oolong': 'Sweet', 'Black': 'Spicy'}}
print(tea_shop["chai"]["Masala"]) # Spicy
print (tea_shop["tea"]["Oolong"]) # Sweet

# ! -----Dictionary Comprehension----- ! #

squared_num = {x:x**2 for x in range(6)}
print(squared_num) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(squared_num.clear()) # None

# Creating dictionary from given data

keys = ["Masala","Ginger","Green"]
default_value = "delicious"
new_dict = dict.fromkeys(keys, default_value) # This is used to create dictionary from given keys and default values

print(new_dict) # {'Masala': 'delicious', 'Ginger': 'delicious', 'Green': 'delicious'}

# Creating dictionary from two lists
values = [1,2,3]
dictionary  = dict(zip(keys,values))
print(dictionary) # {'Masala': 1, 'Ginger': 2, 'Green': 3}

