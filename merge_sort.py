#Arrays
A = [1,3,5,7,9]
B = [2,4,6,8]
C = [0] * (len(A)+len(B))

#Pointers
i=0
j=0
k=0

#sizes
m = (len(A) - 1)
n = (len(B) - 1) 
o = (len(C) - 1)

print(C)
#print(C)


while(i<=m and j<=n):
    if(A[i] < B[j]):
       C[k] = A[i]
       i=i+1
       k=k+1
       print(C)
       #print(f"i = {i}")
       
    if(A[i] > B[j]):
        C[k] = B[j]
        j=j+1
        k=k+1
        print(C)
        #print(f"i = {i}")
        
    if(i>m):
        break
    
    if(j>n):
        break
        
while(i>m):
    C[k] = B[j]
    j=j+1
    k=k+1
    ##print(f"i = {i}")
    
    if(j>n):
        break
    
while(j>n):
    #print(i)
    C[k] = A[i]
    i=i+1
    k=k+1 
    ##print(f"i = {i}")
    print(C)
    
    if(i>m):
        break
    
print(C)   
        
    
       
       
           
    
