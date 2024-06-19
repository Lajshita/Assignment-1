def string_to_list(input_string):
     
    char_list = list(input_string)
    return char_list

def main():
    input_string = input("Enter a string: ")
    char_list = string_to_list(input_string)
    print(f"The string '{input_string}' converted to a list of characters:")
    print(char_list)

if __name__ == "__main__":
    main()
