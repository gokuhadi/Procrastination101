original_num = num
    reverse_num = 0
    
    while num > 0:
        # Extract the last digit of the number
        digit = num % 10
        
        # Build the reverse number
        reverse_num = reverse_num * 10 + digit      
        # Remove the last digit from the number
        num = num // 10
    
    # Check if the original number is equal to its reverse
    return original_num == reverse_num
