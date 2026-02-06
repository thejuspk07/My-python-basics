a=1
while a<5:
    print("hello")
    a+=1
print("end")

b=100
while b>=0:
    print(b)
    b-=1

    111
    1
    1

    1
    1

    11
    11
    1
    1


    def diagonalDifference(arr):
        # Write your code here
        ldiag = 0
        rdiag = 0
        n - len(arr)
        for i in range(n):

            for j in range(n):
                if i == j:
                    ldiag += arr[i][j]
                if i + j == n - 1:
                    rdiag += arr[i][j]
                print(j, end=" ")
        return abs(ldiag - rdiag)