a="geeks for geeks"
k=2
d={}
for i in a:
    if i in d:
        d[i]=d[i]+1

    else:
        d[i]=1

print(d)
ans=""
for i in a:
        if (d[i]<k):
            ans=ans+i

print(ans)
