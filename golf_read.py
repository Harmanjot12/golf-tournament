f = open("golf.txt","r")
lines = f.readlines()

for i in lines:
    par = 80
    fields = i.split()
    
    score = int(fields[2]) #adding all the marks
    
    if  score == par:
        parcourse = 'Made Par'
        
    elif score < par:
        parcourse = 'Under Par'
         
    elif score > par:
        parcourse = 'Over Par'

    print(fields[0] , fields[1] , fields[2] , parcourse)
        