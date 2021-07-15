def Lucky(a,l):
    s=[]
    s=a
    count=0
    for i in a:
        for j in s:
            if (j-i)==l:
                count+=1
    return count
def main():
    a=[]
    s=int(input("Enter the Number of products : ")) #Types of products
    for i in range(s):
        a.append(int(input(f"Enter {i+1} product prices : "))) #price of products
        i+=1
    a.sort()
    l=int(input("Enter the Value to to win a gift basket : ")) #Given value K to determine winners
    v=Lucky(a,l)
    print(f"There are {v} Lucky customers who will win a gift basket.")

if __name__=="__main__":
    main()


