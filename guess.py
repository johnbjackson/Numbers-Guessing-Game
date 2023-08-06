import random
num = random.randint( 1 , 20 )
flag = True
guess = 0
print( ' Guess my number 1-20 :' , end = ' ' )
while flag == True :
    guess = input()
    if not guess.isdigit() :
        print( 'That will not work. Enter only digits 1-20' )
        break
    elif int( guess ) < num :
        print( 'Too low, try again : ' , end = ' ')
    elif int ( guess ) > num :
        print( 'Your number is too high, try again : ' , end = ' ' )
    else :
       print( 'You got it right! My number was ' + guess )
    flag = False
                
