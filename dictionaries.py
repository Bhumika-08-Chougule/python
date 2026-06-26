dict = {'name':'zara','Age':7,'name':'manni'}
print("dict['name']:",dict['name'])

dict = {'name':'zara','Age':7,'class':'Frist'}
print("dict['name']:",dict['name'])
dict['Age'] = 8

del dict['name']
dict.clear

del dict

print(len(dict))
str(dict)
dict1 = dict.copy()
dict2 = dict.items()
dict3 = dict.keys()
dict.update(dict2)

print(dict.values())
