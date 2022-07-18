def factor(n):
  lfact=[]
  for i in range(1,n+1):
    if n%i==0:
      lfact=lfact+[i]
  return(lfact)

def isprime(p):
  return(factor(p)==[1,p])

def primeproduct(m):
  for i in range(1,m+1):
    if m%i==0:
      if isprime(i) and isprime(m//i):
        return(True)
  return(False)

def delchar(s,c):
  if len(c)==1:
    return(s.replace(c,''))
  else:
    return(s)

def shuffle(l1,l2):
  j=max(len(l1),len(l2))
  k=list()
  for i in range(j):
    try:
      k.append(l1[i])
    except:
      pass
    try:
      k.append(l2[i])
    except:
      pass
  return(k)
