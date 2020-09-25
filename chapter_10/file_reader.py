file_path=r'C:\Users\你哥cb\Desktop\pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())