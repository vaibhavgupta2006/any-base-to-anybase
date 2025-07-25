data="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def anybase_to_decimal(data):
    number=input("Enter the number: ").upper()
    base=int(input("enter the base: "))
    power=0
    decimal_number=0
    for digit in number[::-1]:
        if data.index(digit)>base:
            return print("you have entered wrong number or base")
        decimal_number= decimal_number+data.index(digit)*(base**power)
        power+=1
    return decimal_number

decimal_number=(anybase_to_decimal(data))
target_base=int(input("enter the base you want to convert this number to: "))
def decimal_to_anybase(data,decimal_number,target_base):
    desired_number=""
    while decimal_number>0:
        remainder=decimal_number%target_base
        desired_number=desired_number+data[remainder]
        decimal_number=decimal_number//target_base
      
    return desired_number[::-1]
    
print(f"your desired number in base {target_base} is : {decimal_to_anybase(data,decimal_number,target_base)}")
