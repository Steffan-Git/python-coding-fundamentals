# if, else, elifs.

# if condition:
#     code to run if true
# else:
#     code to run if false. 

# import dis

# def disExample():
#     x = 0
#     while x < 3:
#         print("something")
#         x += 1

# dis.dis(disExample)

# on_holiday = True
# is_verified = False
# is_admin = True
#                             f
#                 t                       f
# if (is_admin or is_verified) and not on_holiday:
#     print("access granted")
# else:
#     print("access denied")

# temp = 5

# if temp > 30:
#     print("its hot")
# elif temp > 20:
#     print("its warm")
# elif temp >10"
#     print("mild")
# else:
#     print("its ok")

# user = "admin"

# if user not in ("admin", "user", "root"):
#     print("welcome")
# else:
#     print("denied")

# deposit = 100
# password = "password"

# if (0 < deposit < 100) and password != "password":

# EXERCISE:
# - weight converter
# - input for weight
# - input for unit (KGS or LBS)
# - logic: checking the entered unit
# - logic: calculate the converted value. 
# - print the result (nice formatting)
# - Error handling for invalid unit type 
# - optional stretch: error handle for weight input/conversion. 


# try:
#     result = 10/0
#     print(resultz)
# except ZeroDivisionError as e:
#     print(f"[ERROR] - cant divide by zero: {str(e)}")
# except NameError as e:
#     print("name error caught")
# except:
#     print(f"[ERROR] - generic error caught")
# finally: 
#     print("always gets triggered - use for clean up + logging")
     
# result = 10/0

# import sys

# while True:
#     try:
#         weight = float(input("Enter weight: ")).abs()
#         break
#     except ValueError:
#         print(f"[ERROR] - invalid input pls enter a numeric value for weight")
#         sys.exit()

# while True:
#     unit = input("ENter the unti K or L: ").upper()
#     if unit == "K":
#         x = weight * 2.2
#         print(f"converted weight is {x}")
#         break
#     elif unit == "L":
#         x = weight / 2.2
#         print(f"converted weight is {x}")
#         break
#     else:
#         print("ENTER L OR K!!!!")







