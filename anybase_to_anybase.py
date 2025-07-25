data="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def anybase_to_decimal(data):
    number=input("Enter the number: ").upper()
    base=int(input("enter the base: "))
    f=0
    dec=0
    for digit in number[::-1]:
        if data.index(digit)>base:
            return print("you have entered wrong number or base")
        dec=dec+data.index(digit)*(base**f)
        f+=1
    return dec

decimal=(anybase_to_decimal(data))
end_base=int(input("enter the base you want to convert this number to: "))
def decimal_to_anybase(data,decimal,end_base):
    desired_number=""
    while decimal>0:
        rem=decimal%end_base
        desired_number=desired_number+data[rem]
        decimal=decimal//end_base
      
    return desired_number[::-1]
    
print(f"your desired number in base {end_base} is : {decimal_to_anybase(data,decimal,end_base)}")

