def is_anagram(a,b):
   a=list(a)
   b=list(b)
   if len(a)==len(b):
    for i in a:
      if i in b:
        continue
      else:
        return False
    return True
   return False

def is_anagram(a,b):
   a=list(a)
   b=list(b)
   if a.sort()==b.sort():
    return True
   else:
    return False 

def is_anagram(a,b):
   if len(a)==len(b):
    for i in a:
      if i in b:
        continue
      else:
        return False
    return True
   return False

x=input('Enter the 1st string : ')
y=input('Enter the 2nd string : ')
flag=is_anagram(x,y)
print(flag)

