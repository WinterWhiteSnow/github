def add_to_dict(a,b,c=None):
    if type(a) == str:
        print(f"You need to send a dictionary. you sent: {type(a)}")
    elif not a:  
        print("You need to send a word and a definition.")
        a[b] ="" 
        return a   
    elif a[b] =="" and type(c)==str:
        a[b]=c
        print(f"{b} has been added.")
        return a
    elif a[b] != c:
        print(f"{b} is already on the dictionary. Won't add.")

def get_from_dict(a,b=None,c=None):
    if type(a) == str:
        print(f"You need to send a dictionary. you sent: {type(b)}")
    elif b == None:
        print("You need to send a word to search for.")
    elif b not in a:
        print(f"{b} was not found in this dict.")
    else:
        print(f"{b} : {a[b]}") 

def update_word(a,b,c=None):
    if type(a) == str:
        print(f"You need to send a dictionary. you sent: {type(b)}")
    elif b in a and c==None:
        print("You need to send a word and a definition to update.")
    elif b not in a:
        print(f"{b} is not on the dict. Can't update non-existing word.")        
    elif a[b] != c:
        a[b] = c
        print(f"{b} has been updated to: {c}")

def delete_from_dict(a,b=None):
    if type(a) == str:
        print(f"You need to send a dictionary. you sent: {type(b)}")
    elif a != None and b==None:
        print("You need to specify a word to delete.")
    elif b not in a:
        print(f"{b} is not in this dict. Won't delete.")
    else:
        del a[b]
        print(f"{b} has been deleted.")
    
    

my_english_dict = {}


# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")

##################################################################################################

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

##################################################################################################

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

###################################################################################################

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")