""" 
THIS IS THE TUTORIAL FOR SLICING IN STRINGS
SYNTAX- STRING[START:END:STEP]
START:- IT IS THE INDEX OF THE ELEMEMT AT WHICH THE SLICING OPERATION OF THE STRING IS GOING TO START
END:- IT IS THE INDEX OF THE ELEMENT WHERE THE SLICING OPERATION WILL STOP(EXCLUDED)
STEP:- IT IS THE NUMBER OF ELEMENTS TO SHIFT AFTER THE START ELEMENT      
"""
word1 = "HELLO THIS IS THE DEMO OF HOW SLICING WORKS"
print(word1[2:10:1])

word2 = "now lets see another example"
print(word2[2:9:2])

""" 
For Example 1:-
The sliceing is done as following:-
start- index 2 (which is 'l')
end - at index 10, so element at index 9 will be the last index displayed(which is 's')
step - here step is 1 which means the index will shift 1 after another


For Example 2:-
The slicing is done as following:-
start- index 2 (which is 'w')
end- at index 9, so element at index 8 will be the last index displayed(which is 't') 
step - here step is 2 which means the index will shift 2 after another
"""