import torch
import torch.nn as nn

# Defining the vocabulary size
vocab_size = 58

# Defining embedding dimensions
embedding_dim = 4

# Creating an embedding layer
embedding = nn.Embedding(
    num_embeddings=vocab_size,
    embedding_dim=embedding_dim
)

# Select three token IDs
token_ids = torch.tensor([54, 51, 27])

# Convert token IDs into embeddings
vectors = embedding(token_ids)

# Displaying the results
print("Token IDs:")
print(token_ids)

print("\nEmbedding vectors:")
print(vectors)

print("\nEmbedding shape:")
print(vectors.shape)

# Display the complete embedding table
print("\nComplete embedding table:")
print(embedding.weight)

# Count the trainable parameters
print("\nNumber of trainable parameters:")
print(embedding.weight.numel())