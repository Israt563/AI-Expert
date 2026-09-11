name = input("Hello! I am AI Bot. What's your name? : ")
print(f"Nice to meet you, {name}!")

mood = input("How are you feeling today? (good/bad) : ").strip().lower()

if mood == "good":
    print("I'm glad to hear that! Keep that positive energy going.")
elif mood == "bad":
    print("I'm sorry to hear that. I hope your day gets much better!")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

# Added a new follow-up interaction
hobby = input("What is your favorite thing to do to relax? : ")
print(f"That sounds wonderful! {hobby.capitalize()} is a great way to recharge.")

print(f"It was nice chatting with you, {name}. Goodbye!")