import random 
#PasswwordGenators
letters=['a','b','c''d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#',')','*','+','%','$','&']
print("welcome to the passgenerator")
nbr_letters=int(input("How many letters do you like in your password?\n"))
nbr_symbols=int(input("how many symbols would you like in your password?\n"))
nbr_numbers=int(input("how many numbers would you like in your password?\n"))
password_list=[]
for char in range(1, nbr_letters+1):
   password_list.append(random.choice(letters))
for char in range(1, nbr_symbols+1):
   password_list += random.choice(symbols)
for char in range(1, nbr_numbers+1):
    password_list += random.choice(numbers)
random.shuffle(password_list)
  #print(password_list)
password=""
for char in password_list:
    password += char
print(f"your password is: {password}")