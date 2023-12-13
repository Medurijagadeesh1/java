#for loop
a=100;
for i in range(1,a):
    print(i)
    
#while loop
count = 0   
while count < 10:   
    count= count+ 3
    print("Python Loops")  
    
#break
count=10
while count>5:
    print(count)
    if(count==5):
        break
    count-=1
    
#continue
count=10
while count>5:
    if count%3==0:
        count-=1
        continue
    print(f'pn:{count}')
    count-=1