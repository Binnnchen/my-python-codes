filename=r'text_files\pi_million_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip()

my_birthday=input("Enter your birthday in the form mmddyy: ")

if my_birthday in pi_string:
    print("Your birthay appears in the first million digits of pi!")
else:
    print("Your birthay does not appear in the first million digits of pi!")
