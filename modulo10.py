def luhn(credit):
    credit_list = list(credit)
    
    even_index = credit_list[-2::-2]
    odd_index = credit_list[::-2]
    size = len(even_index)

    doubled = []
    total = 0
    for i in range(0,size):
        num = ord(even_index[i]) - 48
        num = 2 * num


        digit_2 = 0
        if num > 9:
            digit_1 = num // 10
            digit_2 = num % 10
        else: 
            digit_1 = num 
        doubled.append(digit_1 + digit_2)
    print(doubled)
        
    size = len(doubled)    
    for i in range(0,size):
        total = total + doubled[i]
        #total is now the sum of the doubled numbers in the even index and the numbers which have been doubled and then added together.
            
    size = len(odd_index)
    for i in range(0,size):
        
        total = total + ord(odd_index[i]) - 48
        #total is now the sum of the doubled and added and numbers in an odd index
    if total % 10 == 0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    credit = input("Please enter your credit card number. Please note this number will not be shared with anyone ")