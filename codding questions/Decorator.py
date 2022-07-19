# # def decor(fun):                     #control ->  02
# #     def inner():                    #control ->       04
# #         print("Before Enhancing")   #control ->         05
# #         fun()                       #control ->           06
# #         print("After  Enhancing")   #control ->                   10
# #     return inner                    #control ->     03
# # def num():                          #control ->             07
# #     print("start-> num Function")   #control ->               08
# #     print("End-> num Function")     #control ->                 09
# #                                     #control ->                     11
# # num = decor(num)                    #control ->01
# # num()                               #control ->                       12

# # ................................................................................
# # you can replace line ->11 with @decor  ->example in line no 26
def decor(fun):                     #control ->  02
    def inner():                    #control ->       04
        print("Before Enhancing")   #control ->         05
        fun()                       #control ->           06
        print("After  Enhancing")   #control ->                   10
    return inner                    #control ->     03
@decor
def num():                          #control ->             07
    print("start-> num Function")   #control ->               08
    print("End-> num Function")     #control ->                 09
                                    #control ->                     11
num()                               #control ->                       12
# ls=[i for i in range(10) if i%2]
# print(ls)
# # vs 
# ls=[]
# for i in range(10):
#     if i%2:
#         ls.append(i)
# print(ls)
 