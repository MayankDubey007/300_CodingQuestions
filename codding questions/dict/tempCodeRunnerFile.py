import random
questions = {
  
    'q1 ' : 'Q.01) Write a program to reverse an integer in Python.',
    'q2 ' : 'Q.02) Write a program in Python to check whether an integer is Armstrong number or not.',
    'q3 ' : 'Q.03) Write a program in Python to check given number is prime or not.',
    'q4 ' : 'Q.04) Write a program in Python to print the Fibonacci series using iterative method.',
    'q5 ' : 'Q.05) Write a program in Python to print the fibonacci series using recursive method.',
    'q6 ' : 'Q.06) Write a program in Python to check whether a number is palindrome or not using iterative method.',
    'q7 ' : 'Q.07) Write a program in Python to check whether a number is palindrom or not using recursive method.',
    'q8 ' : 'Q.08) Write a program in Python to find greatest among three integers.',
    'q9 ' : 'Q.09) Write a program in Python to check if a number is binary.',
    'q10' : 'Q.10) Write a program in Python to find sum of digits of a number using recursion.',
    'q11' : 'Q.11) Write a program in Python to swap two numbers without using third variable.',
    'q12' : 'Q.12) Write a program in Python to swap two numbers using third variable.',
    'q13' : 'Q.13) Write a program in Python to find prime factors of a given integer.',
    'q14' : 'Q.14) Write a program in Python to add two integer without using arithmetic operator.',
    'q15' : 'Q.15) Write a program in Python to find given number is perfect or not.',
    'q16' : 'Q.16) Python Program to find the Average of numbers with explanations.',
    'q17' : 'Q.17) Python Program to calculate factorial using iterative method.',
    'q18' : 'Q.18) Python Program to calculate factorial using recursion.',
    'q19' : 'Q.19) Python Program to check a given number is even or odd.',
    'q20' : 'Q.20) Python program to print first n Prime Number with explanation.',
    'q21' : 'Q.21) Python Program to print Prime Number in a given range.',
    'q22' : 'Q.22) Python Program to find Smallest number among three.',
    'q23' : 'Q.23) Python program to calculate the power using the POW method.',
    'q24' : 'Q.24) Python Program to calculate the power without using POW function.(using for loop.',
    'q25' : 'Q.25) Python Program to calculate the power without using POW function.(using while loop)..',
    'q26' : 'Q.26) Python Program to calculate the square of a given number.',
    'q27' : 'Q.27) Python Program to calculate the cube of a given number.',
    'q28' : 'Q.28) Python Program to calculate the square root of a given number.',
    'q29' : 'Q.29) Python program to calculate LCM of given two numbers.',
    'q30' : 'Q.30) Python Program to find GCD or HCF of two numbers.',
    'q31' : 'Q.31) Python Program to find GCD of two numbers using recursion.',
    'q32' : 'Q.32) Python Program to Convert Decimal Number into Binary.',
    'q33' : 'Q.33) Python Program to convert Decimal number to Octal number.',
    'q34' : 'Q.34) Python Program to check the given year is a leap year or not.',
    'q35' : 'Q.35) Python Program to convert Celsius to Fahrenheit.',
    'q36' : 'Q.36) Python Program to convert Fahrenheit to Celsius.',
    'q37' : 'Q.37) Python program to calculate Simple Interest with explanation.',
    'q38' : 'Q.38) Python program to remove given character from String.',
    'q39' : 'Q.39) Python Program to count occurrence of a given characters in string.',
    'q40' : 'Q.40) Python Program to check if two Strings are Anagram.',
    'q41' : 'Q.41) Python program to check a String is palindrome or not.',
    'q42' : 'Q.42) Python program to check given character is vowel or consonant.',
    'q43' : 'Q.43) Python program to check given character is digit or not.',
    'q44' : 'Q.44) Python program to check given character is digit or not using isdigit() method.',
    'q45' : 'Q.45) Python program to replace the string space with a given character.',
    'q46' : 'Q.46) Python program to replace the string space with a given character using replace() method.',
    'q47' : 'Q.47) Python program to convert lowercase char to uppercase of string.',
    'q48' : 'Q.48) Python program to convert lowercase vowel to uppercase in string..',
    'q49' : 'Q.49) Python program to delete vowels in a given string.',
    'q50' : 'Q.50) Python program to count Occurrence Of Vowels & Consonants in a String.',
    'q51' : 'Q.51) Python program to print the highest frequency character in a String.',
    'q52' : 'Q.52) Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.',
    'q53' : 'Q.53) Python program to count alphabets, digits and special characters.',
    'q54' : 'Q.54) Python program to separate characters in a given string.',
    'q55' : 'Q.55) python program to remove blank space from string.',
    'q56' : 'Q.56) python program to concatenate two strings using join() method.',
    'q57' : 'Q.57) Python program to concatenate two strings using join() method.',
    'q58' : 'Q.58) Python program to remove repeated character from string.',
    'q59' : 'Q.59) python program to calculate sum of integers in string.',
    'q60' : 'Q.60) python program to print all non repeating character in string.',
    'q61' : 'Q.61) Python program to copy one string to another string.',
    'q62' : 'Q.62) Python Program to sort characters of string in ascending order.',
    'q63' : 'Q.63).Python Program to sort character of string in descending order.',
    'q64' : 'Q.64).Write a program in Python for, In array 1-100 numbers are stored, one number is missing how do you find it.',
    'q65' : 'Q.65).Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.',
    'q66' : 'Q.66).Write a program in Python for, How to find all pairs in array of integers whose sum is equal to given number.',
    'q67' : 'Q.67).Write a program in Python for, How to compare two array is equal in size or not.',
    'q68' : 'Q.68).Write a program in Python to find largest and smallest number in array.',
    'q69' : 'Q.69).Write a program in Python to find second highest number in an integer array.',
    'q70' : 'Q.70).Write a program in Python to find top two maximum number in array?',
    'q71' : 'Q.71).Write a program in Python to remove duplicate elements form array.',
    'q72' : 'Q.72).Python program to find top two maximum number in array.',
    'q73' : 'Q.73).Python program to print array in reverse Order.',
    'q74' : 'Q.74).Python program to reverse an Array in two ways.',
    'q75' : 'Q.75).Python program to insert an element at end of an Array.',
    'q76' : 'Q.76).Python Program to calculate length of an array.',
    'q77' : 'Q.77).Python program to insert element at a given location in Array.',
    'q78' : 'Q.78).Python Program to delete element at end of Array.',
    'q79' : 'Q.79).Python Program to delete given element from Array.',
    'q80' : 'Q.80).Python Program to delete element from array at given index.',
    'q81' : 'Q.81).Python Program to find sum of array elements.',
    'q82' : 'Q.82).Python Program to lamda Functions.',
    'q83' : 'Q.83).Python Program to print all even numbers in array.',
    'q84' : 'Q.84).Python Program to print all odd numbers in array.',
    'q85' : 'Q.85).Python program to perform left rotation of array elements by two positions.',
    'q86' : 'Q.86).Python program to perform right rotation in array by 2 positions.',
    'q87' : 'Q.87).Python Program to merge two arrays.',
    'q88' : 'Q.88).Python Program to find highest frequency element in array.',
    'q89' : 'Q.89).Python Program to add two number using recursion.',
    'q90'  :'Q.90).python Program to find sum of digit of number using recursion.',
    'q91' : '''Q.91).  star pattern
                                   *
                                   * * 
                                   * * * 
                                   * * * * ''',
    'q92' : '''Q.92).  star pattern
                                        *
                                      * * 
                                    * * * 
                                  * * * *  ''',
    'q93' : '''Q.93).  star pattern
                                   * * * * 
                                   * * * 
                                   * * 
                                   *       ''',
    'q94' : '''Q.94).  star pattern
                                  * * * * 
                                    * * * 
                                      * * 
                                        *  ''',
    'q95' : '''Q.95).  star pattern
                                          *
                                        * * * 
                                      * * * * * 
                                    * * * * * * *  ''',
    'q96' : '''Q.96).  star pattern
                                    * * * * * * *  
                                      * * * * * 
                                        * * * 
                                          *        ''', 
    'q97' : '''Q.97).  star pattern
                                    * * * * * * *  
                                    * * *   * * *  
                                    * *       * *  
                                    *           * ''',
    'q98' : '''Q.98).  star pattern
                                   1
                                   1 2 
                                   1 2 3 
                                   1 2 3 4 ''',
    'q99' : '''Q.99).  star pattern
                                   5 4 3 2 1 
                                   4 3 2 1
                                   3 2 1
                                   2 1  
                                   1  ''',
    'q100':''''.100).  star pattern
                                   *
                                   * * 
                                   * * * 
                                   * * * * ''',
    'q101' : 'Q.).Python Program to List To String.',
    'q102' : 'Q.).Python Program to a2z & A2Z value a->97 z->122 || A->65 Z->90.',
    'q103' : 'Q.).Python Program to List in Sort Method.',
    'q104' : 'Q.).Python Program to date diffrence.',
    'q105' : 'Q.).Python Program to merge 2 Dictionary.',
    'q106' : 'Q.).Python Program to month diffrence.',
    'q107' : 'Q.).Python Program to reverse loop.',
    'q108' : 'Q.).Python Program to password genrator.',
    'q108' : 'Q.).Python Program to string to list.',
    'q109' : 'Q.).Python Program to list to string.',
    'q110' : 'Q.).Python Program to sort list with any method.',
}
ls = list(questions.values())
random.shuffle(ls)
# print(ls)
s=0
for i in range(11):
  print(i+1)
  print(ls[i])
  # print(questions[i]) 
  skip = input("")
  if skip=="y":
    continue