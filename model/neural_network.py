import torch
import torch.nn as nn

# Defining model dimensions
vocab_size = 58
embedding_dim = 8
hidden_dim = 16

# Building the neural network
class LanguageModel(nn.Module):
    
    def __init__(self):
        super().__init__()
        
        # Converting token IDs into vectors
        self.embedding = nn.Embedding(
            vocab_size,
            embedding_dim
        )
        
        # First neural network layer
        self.linear1 = nn.Linear(
            embedding_dim * 3,
            hidden_dim
        )
        
        # Activation function
        self.relu = nn.ReLU()
        
        # Output layer
        self.linear2 = nn.Linear(
            hidden_dim,
            vocab_size
        )
        
    def forward(self, x):
        
        # Convert token IDs into embeddings
        x = self.embedding(x)
        
        # Combine the three token embedddings
        x = x.view(x.shape[0], -1)
        
        # Pass through the first layer
        x = self.linear1(x)
        
        # Apply activation function
        x = self.relu(x)
        
        # Produce scores for every vocabulary token
        x = self.linear2(x)
        
        return x
    
# Creating the model
model = LanguageModel()
    
# Testing with three token IDs
sample_input = torch.tensor([[54, 51, 27]])
    
# Make a prediction
output = model(sample_input)
    
# Displaying results
print("Model output:")
print(output)
    
print("\nOutput shape:")
print(output.shape)
    
print("\nTotal trainable parameters:")
print(sum(p.numel() for p in model.parameters()))