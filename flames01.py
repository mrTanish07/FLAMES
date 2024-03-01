def calculate_flames(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Create a list of unique characters from both names
    combined_characters = list(set(name1 + name2))

    # Count the total number of unique characters
    total_characters = len(combined_characters)

    # Calculate the number of common characters
    common_characters = 0
    for char in combined_characters:
        if char in name1 and char in name2:
            common_characters += 1

    # Calculate Flames result
    flames_result = (total_characters - common_characters) % 6

    # Define Flames result categories
    flames_categories = ["Friends", "Lovers", "Admirers", "Marriage", "Enemies", "Siblings"]

    return flames_categories[flames_result - 1]

def main():
    print("Welcome to the Flames Game!")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    result = calculate_flames(name1, name2)

    print(f"\nResult: {name1} and {name2} are {result}")

if __name__ == "__main__":
    main()
