from pathlib import Path

# Load the training data
data_path = Path(__file__).parent / "training_data.txt"
text = data_path.read_text(encoding="utf-8")

# Tokenize text
tokens = text.lower().split()

# Create vocabulary
vocabulary = sorted(set(tokens))

# Convert words into numerical IDs
word_to_id = {
    word: index
    for index, word in enumerate(vocabulary)
}

numerical_tokens = [
    word_to_id[word]
    for word in tokens
]

# Defining context window size
context_size = 3

# Generate training examples
for i in range(context_size, len(numerical_tokens)):
    
    # Previous three tokens
    input_sequence = numerical_tokens[i-context_size:i]
    
    # The next token
    target = numerical_tokens[i]
    
    # Convert IDs back to words for display
    input_words = [
        vocabulary[token_id]
        for token_id in input_sequence
    ]
    
    target_word = vocabulary[target]
    
    print(f"{input_words} -> {target_word}")