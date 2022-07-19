q1='''1. Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom
'''
q2='''2. Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned
'''
q3='''3. Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned
'''
q4='''
4. Which of the following is the correct extension of the Python file?
a) .python
b) .pl
c) .py
d) .p
'''
q5='''
5. Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted
'''

questions={q1:'c',q2:'d',q3:'a',q4:'c',q5:'b'}
score=0
for i in questions:
    print(i)
    # print(questions[i])
    
    skip = input("if you want to skip this questions (yes/no)): ")
    if skip=="y":
        continue
    ans=input("enter the answer (a/b/c/d)")
    if ans==questions[i]:
        print("correct answer,you got 1 point")
        score+=1
        print("current Score is : ",score)
    else:
        print("wrong answer,you lose 1 point")
        score-=1
        print("current Score is : ",score)
    quit = input("do you want to Quit(y/n)")
    if quit=='y':
        break
print("Total Score is : ",score)