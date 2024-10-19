

#making a dictionary of

dictionary = {
    'Adeel' : 'Gems',
    'Alex' : 'Books',
    'Eleine' : 'Hiking',
    'Jeffrey' : 'Funny guy',
    0 : 'Nothing'
}

#print a specific key
print(dictionary[0])

#printing dict items
print(dictionary.items())

#printing dict values
print(dictionary.values())

#printing dict keys
print(dictionary.keys())

#updating  a dict

dictionary.update({'adeel' : 'Dragons'})


#what if multiple keys

dictionary1 = {
    'Adeel' : 'Gems',
    'Alex' : 'Books',
    'Eleine' : 'Hiking',
    'Eleine' : 'nothing',
    'Jeffrey' : 'Funny guy',
    0 : 'Nothing'
}

print(dictionary1)
#it will overwrite that key's value