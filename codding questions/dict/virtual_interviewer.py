# list - > 
# trick ->c,p,{q},r,s
# i->3 - insert(),indexr()
# c->3 - copy(),clear(),count()
# p->1 - pop()
# r->2 - reverrse() , remove()
# s->1 - sort()
questions = {
    'q1 ' : '1. Difference Between List and Tuple',
    'q2 ' : '2. What is Decorator? Explain With Example.',
    'q3 ' : '3. Difference Between List and Dict Comprehension',
    'q4 ' : '4. How Memory Managed In Python?',
    'q5 ' : '5. Difference Between Generators And Iterators',
    'q6 ' : '6. What is ‘init’ Keyword In Python?',
    'q7 ' : '7. Difference Between Modules and Packages in Python',
    'q8 ' : '8. Difference Between Range and Xrange?',
    'q9 ' : '9. What are Generators. Explain it with Example.',
    'q10' : '10. What are in-built Data Types in Python OR Explain Mutable and Immutable Data Types',
    'q11' : '11. Explain Ternary Operator in Python?',
    'q12' : '12. What is Inheritance In Python',
    'q13' : '13. Difference Between Local and Global Variable in Python',
    'q14' : '14. Explain Break, Continue and Pass Statement',
    'q15' : '15. What is "self" Keyword in python?',
    'q16' : '16. Difference Between Pickling and Unpickling?',
    'q17' : '17. Explain Function of List, Set, Tuple And Dictionary?',
    'q18' : '18. What are Python Iterators?',
    'q19' : '19. Explain Type Conversion in Python. [(int(), float(), ord(), oct(), str() etc.)]',
    'q20' : '20. What does *args and **kwargs mean? Expain',
    'q21' : '21. What is "Open" and "With" statement in Python?',
    'q22' : '22. Different Ways To Read And Write In A File In Python?',
    'q23' : '23. What is Pythonpath?',
    'q24' : '24. How Exception Handled In Python?',
    'q25' : '25. Difference Between Python 2.0 & Python 3.0',
    'q26' : '26. What is ‘PIP’ In Python',
    'q27' : '27. Where Python Is Used?',
    'q28' : '28. How to use F String and Format or Replacement Operator?',
    'q29' : '29. Difference Between Abstraction and Encapsulation.',
    'q30' : '30. How to Get List of all keys in a Dictionary?',
    'q31' : '31. Does python support multiple inheritnce. (Diamond Problem)',
    'q32' : '32. How to initialize empty list, tuple, dict or set?',
    'q33' : '33. Diff btw .py and .pyc',
    'q34' : '34. How slicing works in string manupulation. i.e [::-1] explain.',
    'q35' : '35. How can you concatenate two tuples',
    'q36' : '36. Diff btw Python Arrays and Lists',
    'q37' : '37. Diff btw _abc, __abc, ___abc___ in python?',
    'q38' : '38. How to read multiple value from single input? --- By Split()',
    'q39' : '39. How to copy and delete a dictionary',
    'q40' : '40. Diff Btw Anonymous and Lambda function'
}

score=0
for i in questions:
    # print(i)
    print(questions[i])
    
    skip = input("")
    if skip=="y":
        continue