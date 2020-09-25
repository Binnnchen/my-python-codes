"""输入数据异常处理"""
print("Input two numbers, and I'll give you their adding")
print("Enter 'f' to quite.")
while True:
    
    first_number=input("\nFirst number: ")
    if first_number =='f':
        break
    second_number=input("Second number: ")
    if second_number =='f':
        break
    try:
        sum=int(first_number)+int(second_number)
    except ValueError:
        print("\nPlease input numbers, not the strings.")
    else:
        print(sum)
    