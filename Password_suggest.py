import secrets 
import random
#password digits and alphabets
letters = "qwertyupasdfghjkmnbvcxz"
cap_letters = "QWERTYUPKJHGFDSAZXCVBNM"
symbols = "@#£_&-+()/?!;:'~`|×}{=^¢$¥€%✓[]"
nums = "23456789"
#largest possible password 
all_chars = letters + cap_letters + symbols + nums
#getting password length 
while True : 
    try : 
        password_length = int(input("ENTER REQUIRED PASSWORD LENGTH: "))
        if password_length <= 12 : 
            raise Exception("SORRY! PASSWORD LENGTH MUST BE HIGHER THAN 12 ")
        break 
    except ValueError : 
        print("invalid input")
    except Exception as e : 
        print(e)
#generating password 
repeat = int(input("HOW MANY PASSWORDS DO YOU WANT : "))
count = repeat 
while repeat > 0 : 
    password_box = [secrets.choice(letters),secrets.choice(cap_letters),secrets.choice(nums),secrets.choice(symbols)]
    random.shuffle(password_box)
    remaining = password_length - 4
    password= ""
    for k in range(remaining) : 
        password_letter = secrets.choice(all_chars)
        password += password_letter
        password_box.append(password_letter)
    random.shuffle(password_box)
    
    password = ''.join(password_box)
    print(f"{count - repeat + 1} : {password}")
    repeat -= 1

