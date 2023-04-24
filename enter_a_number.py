print("Enter a number x : ")
x = int(input())
if x >= 100:
    x = "Багато"
elif 50 <= x < 100:
    x = "OK"
elif x < 50:
    x = "Not enough"
print(x)
