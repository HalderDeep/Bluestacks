
#defing a method which accepts n as the height of tower and returns the count of towers.
def findNumOfTower(n):
    
#initializing the blocks with height
    Block1=1
    Block2=2
    Block3=4
    res=0
    
#if the height is 1 then only 1
    if(n==1):
        res=1;
#if the height is 2 then only 2 towers
    elif(n==2):
        res=2;
#if the height is 3 then only 4 towers
    elif(n==3):
        res=4
#for the height is 4 oor greater
    else:
#initalizing the block4 value               
        Block4=0
                    
        for i in range(4,n+1):
#We run a loop for the value of i in the range 4 to n+1
            Block4=Block1+Block2+Block3
            Block1=Block2
            Block2=Block3
            Block3=Block4
#the result returns the no of blocks can be created
        res=Block4
    return res
#Method Ends here-----------------



#Takes input from user
#Code excepts only integers
for i in range(0,10):
    while True:
        try:
            num=int(input('Enter the height n'))
            #The function is called and printed

            print(findNumOfTower(num))
            break
        except ValueError:
            print ("Please Enter integer only")
            continue
        except FloatingPointError:
            print ("Please Enter integer only")
            continue
    break        

    
    
