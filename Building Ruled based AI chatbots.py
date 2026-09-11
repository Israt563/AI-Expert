import random
import re
from colorama import Fore, init

# Autoreset ensures each print resets color formatting automatically
init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket", "Santorini"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Banff"],
    "cities": ["Tokyo", "Paris", "New York", "London"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!",
    "What do you call a beach that keeps losing things? A shore loser!"
]


def normalize_input(text: str) -> str:
    """Normalize input by removing extra spaces and forcing lowercase."""
    return re.sub(r"\s+", " ", text.strip().lower())


def recommend():
    """Provides travel recommendations iteratively instead of recursively."""
    while True:
        print(Fore.CYAN + "TravelBot: What vibe are you looking for? (beaches, mountains, cities)")
        preference = normalize_input(input(Fore.YELLOW + "You: "))

        if preference in destinations:
            # Copy list so we can remove rejected options during this session
            available_spots = destinations[preference].copy()
            
            while available_spots:
                suggestion = random.choice(available_spots)
                print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
                answer = normalize_input(input(Fore.CYAN + "TravelBot: Do you like it? (yes/no): "))

                if answer in ["yes", "y"]:
                    print(Fore.GREEN + f"TravelBot: Awesome! Enjoy your trip to {suggestion}!")
                    return
                elif answer in ["no", "n"]:
                    available_spots.remove(suggestion)
                    if available_spots:
                        print(Fore.RED + "TravelBot: No problem, let's try another one.")
                    else:
                        print(Fore.RED + "TravelBot: That's all the spots I have for that category!")
                else:
                    print(Fore.RED + "TravelBot: Please answer with 'yes' or 'no'.")
            return
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have recommendations for that category.")
            retry = normalize_input(input(Fore.CYAN + "TravelBot: Try another category? (yes/no): "))
            if retry not in ["yes", "y"]:
                return


def packing_tips():
    """Offers dynamic packing advice based on trip duration and category."""
    print(Fore.CYAN + "TravelBot: Where are you traveling to?")
    location = input(Fore.YELLOW + "You: ").strip()

    # Validate integer input for trip duration
    while True:
        print(Fore.CYAN + f"TravelBot: How many days will you be in {location}?")
        days_input = input(Fore.YELLOW + "You: ").strip()
        if days_input.isdigit() and int(days_input) > 0:
            days = int(days_input)
            break
        print(Fore.RED + "TravelBot: Please enter a valid number of days (e.g., 5).")

    print(Fore.GREEN + f"\nTravelBot: Packing checklist for {days} days in {location}:")
    print(Fore.GREEN + f"- Pack {days + 1} pairs of underwear and socks.")
    print(Fore.GREEN + "- Multi-voltage wall adapter & portable power bank.")
    
    if days > 7:
        print(Fore.GREEN + "- Travel-sized laundry detergent (for trips over a week).")
    
    print(Fore.GREEN + "- Universal essentials: Toiletries, travel documents, medications.\n")


def tell_joke():
    """Displays a random joke."""
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")


def show_help():
    """Displays command options."""
    print(Fore.MAGENTA + "\nI can assist you with:")
    print(Fore.GREEN + "- Destination ideas (say 'recommend' or 'suggest')")
    print(Fore.GREEN + "- Custom packing lists (say 'pack' or 'packing')")
    print(Fore.GREEN + "- Travel humor (say 'joke')")
    print(Fore.CYAN + "- Exit conversation (say 'exit' or 'bye')\n")


def chat():
    """Main conversational loop."""
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "What's your name? ").strip()
    name = name if name else "Traveler"
    
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))

        if any(word in user_input for word in ["recommend", "suggest", "destination", "place"]):
            recommend()
        elif any(word in user_input for word in ["pack", "packing", "list"]):
            packing_tips()
        elif any(word in user_input for word in ["joke", "funny", "laugh"]):
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif any(word in user_input for word in ["exit", "bye", "quit"]):
            print(Fore.CYAN + f"TravelBot: Safe travels, {name}! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: I didn't quite catch that. Type 'help' to see what I can do.")


if __name__ == "__main__":
    chat()