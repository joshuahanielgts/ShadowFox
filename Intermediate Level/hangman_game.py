import random
def hangman():
    word_list = ['python', 'internship', 'development', 'programming', 'shadowfox']
    word = random.choice(word_list)
    guessed = set()
    attempts = 6
    hint = word[0] + "*" * (len(word)-2) + word[-1]
    print("🎮 Welcome to Hangman!")
    print("Hint:", hint)
    while attempts > 0:
        display = "".join([letter if letter in guessed else "_" for letter in word])
        print("Word:", display)

        if display == word:
            print("🎉 You guessed the word!")
            return
        guess = input("Enter a letter: ").lower()
        if guess in guessed:
            print("You already guessed that.")
        elif guess in word:
            guessed.add(guess)
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong! Attempts left:", attempts)
    print("💀 Game over! The word was:", word)
if __name__ == "__main__":
    hangman()
