# Check Leap Year
# Check if a year is leap year:
# divisible by 400 → leap
# divisible by 4 and not by 100 → leap
# else → not leap


a = int(input("Ente your like this '2000':  "))

if a % 400 == 0:
    print(f"{a} is a Leap year.")
elif a % 4 == 0 and a % 100 != 0:
    print(f"{a} is a Leap Year.")
else:
    print(f"{a} is not a Leep year.")
# OP:
# Ente your like this '2000':  2004
# 2004 is a Leap Year.


# print("\n-----------------\n")
# print("Leep Year" if (a % 400 == 0 or (a % 4 == 0 and a % 100 != 0)) else "Not Leep Year.")

