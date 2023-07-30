# Run this first to generate your input text file

def main():
    # Get user input
    user_input = input("Enter the text you want to write to the file:\n")

    # Write the user input to the 
    with open("input.txt", "w") as file:
        file.write(user_input)

    print("Text has been written to input.txt")

if __name__ == "__main__":
    main()
