f = open("golf.txt","a")

while(True):
    fname = input("Your First Name : ")
    lname = input("Your Last Name : ")
    score = input("Golf Score or Player : ")
    
    
    f.write(fname +" " + lname + " " + score +  "\n")
    
    c = input("\nDo you want to enter more{y/n} : ") #asking weather want to enter more or not
    c = c.lower()  #to convert value of c to lowercase  
    
    if c=='n':
        break  #if user donot want to enter more then break the loop
     
f.close()
        

