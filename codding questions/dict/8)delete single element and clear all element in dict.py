# cheak key in exising or not in dict
# print(key_name in dict_name)

dicA={'a':1,'b':2,'c':3}
dicA['d'] = 4
dicA['e'] = 5
dicA['f'] = 6
print("before\n",dicA)
# deleting element
del dicA['a']
del dicA['b']
print("after\n",dicA)
dicA.clear()
print("after\n",dicA)
