import time
import random

# List of texts to type
texts = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick waltzing zebras jump",
    "Bright vixens jump; dozy fowl quack",
    "Quick wafting zephyrs vex bold Jim",
    "ikaw at ako ay tao",
    'life is like a pyramid',
    'a big black clock'
]

def calculate_accuracy(input_text, original_text):
    input_words = input_text.split()
    original_words = original_text.split()
    correct_words = sum(1 for i, j in zip(input_words, original_words) if i == j)
    accuracy = correct_words / len(original_words) * 100
    return accuracy

def typing_master():
    print("Welcome to Typing Master!")
    print("Type the following text as accurately and quickly as possible:")

    # Select a random text
    text = random.choice(texts)
    print(text)

    # Start the timer
    start_time = time.time()

    # Get the user's input
    user_input = input("Type here: ")

    # Stop the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Calculate the accuracy
    accuracy = calculate_accuracy(user_input, text)

    # Display the results
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

    # Calculate the words per minute (wpm)
    num_words = len(text.split())
    wpm = num_words / elapsed_time * 60
    print(f"Words per minute: {wpm:.2f} wpm")

if __name__ == "__main__":
    typing_master()