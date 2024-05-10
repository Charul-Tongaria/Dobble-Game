import random

def generate_symbols():
    """Generate a list of symbols."""
    symbols = [chr(i) for i in range(33, 127)]  # ASCII symbols from '!' to '~'
    return symbols

def generate_card():
    """Generate a single card with symbols."""
    symbols = generate_symbols()
    card = random.sample(symbols, 8)  # Each card has 8 symbols
    return card

def find_matching_symbol(cards):
    """Find the matching symbol between two cards."""
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            matching_symbol = set(cards[i]) & set(cards[j])
            if matching_symbol:
                return cards[i], cards[j], matching_symbol.pop(), i, j

def print_cards(cards, matching_symbol, index1, index2):
    """Print the cards."""
    design = [

        # "+-----+ {card[0][0]} +-----+" 
        # "|                          |"
        # "+-----+ {card[1][0]} +-----+"
    
        
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][0]}  |  |  {cards[1][0]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][1]}  |  |  {cards[1][1]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][2]}  |  |  {cards[1][2]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][3]}  |  |  {cards[1][3]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][4]}  |  |  {cards[1][4]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][5]}  |  |  {cards[1][5]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][6]}  |  |  {cards[1][6]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
        "|     |  |     |",
        f"|  {cards[0][7]}  |  |  {cards[1][7]}  |",
        "|     |  |     |",
        "+-----+  +-----+",
    ]
    for line in design:
        print(line)
    
    

def main():
    print("Generating two random cards...")
    cards = [generate_card(), generate_card()]
    print("Generated Cards:")
    matching_card, _, matching_symbol, index1, index2 = find_matching_symbol(cards)
    print_cards(cards, matching_symbol, index1, index2)
    
    user_input = input("\nEnter the matching symbol: ")
    
    if user_input == matching_symbol:
        print("Correct! The symbol matches.")
        print("\nMatching Symbol:", matching_symbol)
        print("Index position in Card 1:", index1)
        print("Index position in Card 2:", index2)
    else:
        print(f"Incorrect! The correct matching symbol is '{matching_symbol}'.")
        print("\nMatching Symbol:", matching_symbol)
        print("Index position in Card 1:", index1)
        print("Index position in Card 2:", index2)
    
if __name__ == "__main__":
    main()
