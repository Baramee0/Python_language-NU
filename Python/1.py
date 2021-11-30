import statistics
input_string = input()
user_list = input_string.split()
A1 = max(user_list)
A2 = min(user_list)
A3 = int(max(user_list)) - int(min(user_list))
print(A1 , A2 , A3)

