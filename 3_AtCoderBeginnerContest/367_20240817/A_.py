A, B, C = map(int, input().split())

# A 叫ぶ B 寝る C 起床

if C < A < B:
    print("Yes")

elif C > B:
    if A < B or A > C:
        print("Yes")
    else:
        print("No")

else:
    print("No")