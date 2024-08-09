# Enter your code here. Read input from STDIN. Print output to STDOUT

num1 = int(input())
eng = set(map(str, input().split()))
num2 = int(input())

fre = set(map(str, input().split()))

print(len(eng.difference(fre)))



