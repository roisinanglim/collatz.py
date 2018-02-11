# Requests user to enter an interger
i = int(input("input integer ")) 
print(i) 
#Do this when I is not equal to one
while i != 1: 
#When I even number
     if i %2 ==0: 
         i= i/2
         print(int(i))   
#When I uneven number      
   elif i %2 ==1:
        i= i*3+1
        print(int(i))
