def find_min_max(numbers):
    if not numbers:
        return None, None 
    
    min_num = numbers[0]
    max_num = numbers[0]
    
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    return min_num, max_num

def main():
    
    numbers = [5, 2, 9, 1, 7, 3, 6, 8, 4]
    
   
    min_value, max_value = find_min_max(numbers)
    
    print(f"List of numbers: {numbers}")
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")

if __name__ == "__main__":
    main()
