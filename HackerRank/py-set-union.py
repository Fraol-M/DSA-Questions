# Enter your code here. Read input from STDIN. Print output to STDOUT

eng = int(input())
roll_1 = set(map(str, input().split()))
french = int(input())
roll_2 = set(map(str, input().split()))

print(len(roll_1.union(roll_2)))