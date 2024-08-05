dict = { 'python': 'data science', 'machine learning' : 'tensorflow' ,'artificial intelligence': 'keras'}
print("dict:",dict)
dict2=dict.copy()                     #copying the dict in dict2
print("dict2:",dict2)
dict2.clear()
print("clear dict2:",dict2)                  #clearing all the elements from the dict
keys=dict.keys()
print(keys)                     #keys printing
values_dict=dict.values()
print(values_dict)                #values printing
for i in dict.keys():
    print(i)                          #tried in interview
pop_dict=dict.pop('python')
print("pop-dict:",pop_dict)      # poping the 1 key pair value from dictionary
print(dict)
get_dict=dict.get('machine learning')
print("get_dict:",get_dict)
dict.update({'apple':1,'grapes':2,'mango':3})
print(dict)
ls=list(dict)
print("converted dict into list:",ls)
dict.update()
