from pathlib import Path

# Locating the training data
data_path = Path(__file__).parent / "training_data.txt"

# Read the training data
text = data_path.read_text(encoding="utf-8")

# Split the text into individual words
tokens = text.lower().split()

# Creating a vocabulary of unique words
vocabulary = sorted(set(tokens))

# Assigning a unique number to every word
word_to_id = {
    word: index
    for index, word in enumerate(vocabulary)
}

# converting text into numerical IDs
numerical_tokens = [
    word_to_id[word]
    for word in tokens
]

# Displaying the results
print("Original text:")
print(text)

print("\nVocabulary:")
print(word_to_id)

print("\nNumerical representation:")
print(numerical_tokens)

print("\nVocabulary size:", len(vocabulary))