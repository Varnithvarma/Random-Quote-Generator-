import random

def read_quotes_from_file(file_name):
    quotes = []
    with open(file_name, "r") as file:
        for line in file:
            quote = line.strip()
            quotes.append(quote)
    return quotes

def get_random_quote(quotes):
    return random.choice(quotes)

def display_quote(quote):
    print(quote)

def main():
    file_name = "quotes.txt"  # Replace with the path to your quotes file
    quotes = read_quotes_from_file(file_name)
    random_quote = get_random_quote(quotes)
    display_quote(random_quote)

if __name__ == "__main__":
    main()
