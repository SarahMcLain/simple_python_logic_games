#create function fizzbuzz
def fizzBuzz(n):
    for i in range(1, n+1): #create the for loop
        if i % 3 == 0 and i % 5 == 0: #if i can be divided by 3 and 5
            print('fizzbuzz') #print fizzbuzz
        elif i % 3 == 0: #if only divisible by 3 
            print('fizz') #print fizz
        elif i % 5 == 0: #if only divisible by 5 
            print('buzz') #print buzz
        else:
            print(i)
        
fizzBuzz(25)