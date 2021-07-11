import random
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

num_chars = int(input("How many characters would you like password to be: "))

pass_list = []
for _ in range(num_chars):
	rand_chars = random.choice(chars)
	pass_list.append(rand_chars)
random.shuffle(pass_list)
password = "".join(pass_list)
print(f"Here is your password: {password}")