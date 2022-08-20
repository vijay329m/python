l=['eat','ate','tea','care','race','rat']
m=[]
for i in l:
    m.append(' '.join(sorted(i)))
#print(m)
#m.sort()
#print(m)
cnt= 1 
p=''
for i in m:
    c=i 
    if p==c:
        cnt+=1 
        p=c 
    else:
        if p!='':
            print(p,cnt)
        cnt=1 
        p=c
print(c,cnt)
    

