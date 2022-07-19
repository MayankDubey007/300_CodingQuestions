# # In the latest update of python now we can use “|” operator to merge two dictionaries. It is a very convenient method to merge dictionaries.
# def Merge(dict1, dict2):
# 	res = dict1 | dict2
# 	return res
	
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}
# dict3 = Merge(dict1, dict2)
# print(dict3)
# # ...............................................
# # def Merge(dict1, dict2):
# # 	return(dict2.update(dict1))
	
# # dict1 = {'a': 10, 'b': 8}
# # dict2 = {'d': 6, 'c': 4}

# # print(Merge(dict1, dict2))
# # print(dict2)
# print(ord("hello"))
# ........................................................
dict_1={'John': 15, 'Rick': 10, 'Misa': 12}
dict_2={'Bonnie': 18, 'Rick': 20, 'Matt': 16}
dict_3={k:v for d in (dict_1,dict_2) for k,v in d.items()}
print (dict_3)
# # In the latest update of python now we can use “|” operator to merge two dictionaries. It is a very convenient method to merge dictionaries.
# def Merge(dict1, dict2):
# 	res = dict1 | dict2
# 	return res
	
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}
# dict3 = Merge(dict1, dict2)
# print(dict3)
# # ...............................................
# # def Merge(dict1, dict2):
# # 	return(dict2.update(dict1))
	
# # dict1 = {'a': 10, 'b': 8}
# # dict2 = {'d': 6, 'c': 4}

# # print(Merge(dict1, dict2))
# # print(dict2)
# print(ord("hello"))
# ........................................................
# dict_1={'John': 15, 'Rick': 10, 'Misa': 12}
# dict_2={'Bonnie': 18, 'Rick': 20, 'Matt': 16}
# dict_3={k:v for d in (dict_1,dict_2) for k,v in d.items()}
# print (dict_3)
# ........................................................
dic1={'John': 15, 'Rick': 10, 'Misa': 12}
dic2={'Jasmine' : 19,'Maria' : 26, 'Helena' : 30  }
for k,v in dic2.items():
    dic1[k] = v
print(dic1)

