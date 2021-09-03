n = int(input("Please enter the start number: "))

m = int(input("Please enter the end number: "))

count = 0

for i in range(n,m):

    if i > 1:

        for j in range(2,i):

            if(i % j == 0):

                break

        else:

            print(i)

            count = count + 1

print("Total prime numbers between {0} and {1} is {2}".format(n,m,count))