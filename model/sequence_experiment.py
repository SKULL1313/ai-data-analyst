from pathlib import Path

# Load the training data
data_path = Path(__file__).parent / "training_data.txt"
text = data_path.read_text(encoding="utf-8")

# Convert text into tokens
tokens = text.lower().split()

# Creating the vocabulary
vocabulary = sorted(set(tokens))

# Assigning each token a numerical ID
word_to_id = {
    word: index
    for index, word in enumerate(vocabulary)
}

# Converting tokens into numbers
numerical_tokens = [
    word_to_id[word]
    for word in tokens
]

# Creating input and target sequences
inputs = numerical_tokens[:-1]
targets = numerical_tokens[1:]

# Displaying the first 10 training examples
print("Input ID -> Target ID")
print("-" * 30)

for i in range(10):
    input_id = inputs[i]
    target_id = targets[i]
    
    input_word = vocabulary[input_id]
    target_word = vocabulary[target_id]

    print(f"{input_word} -> {target_word}")