
# AI Data Analyst Agent & Personal Language Model

An evolving Python project that combines data analysis automation with the development of a small language model built from scratch using PyTorch.

The long-term goal is to build an AI agent that can understand business questions, analyze structured datasets, generate useful insights, and explain its findings.

Rather than relying entirely on prebuilt language models or hosted LLM APIs, this project explores how language models work internally, from tokenization and embeddings to neural network training and transformer architecture.

## Project Goals

- Build an AI-powered data analyst that answers questions about business datasets.
- Develop a small language model from the ground up using Python and PyTorch.
- Understand tokenization, vocabulary creation, and numerical representations.
- Explore embeddings and neural network architecture.
- Implement next-token prediction and model training.
- Learn loss functions, backpropagation, and gradient descent.
- Eventually integrate the trained language model with the data analyst agent.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyTorch | Neural network development and training |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| VS Code | Development environment |
| Git & GitHub | Version control |

## Project Structure

```text
ai-data-analyst/
│
├── data/
│   ├── transactions.csv
│   └── monthly_revenue.csv
│
├── model/
│   ├── data/
│   ├── training_data.txt
│   ├── tokenizer.py
│   ├── sequence_experiment.py
│   ├── context_window.py
│   ├── embedding_experiment.py
│   └── neural_network.py
│
├── analysis_tools.py
├── generate_data.py
├── main.py
├── .gitignore
└── README.md
```

## Current Development Progress

### Part 1: AI Data Analyst Agent

The initial version uses Python-based analysis functions to answer questions about business transaction data.

Current capabilities include:

- Calculate total revenue.
- Calculate average transaction value.
- Identify top-performing products.
- Analyze revenue across products.

The project uses a synthetic dataset containing 1,000 transactions.

### Part 2: Building a Language Model From Scratch

This section focuses on understanding and implementing the fundamental components of a language model.

| Component | Status |
|---|---|
| Vocabulary creation | Completed |
| Basic tokenization | Completed |
| Token-to-ID conversion | Completed |
| Next-token prediction examples | Completed |
| Context windows | Completed |
| Embedding layer | Completed |
| Basic neural network architecture | Completed |
| Loss function and training | In progress |
| Backpropagation and gradient descent | Planned |
| Transformer and self-attention | Planned |
| Instruction tuning | Planned |
| Integration with data analyst agent | Planned |

## Understanding the Language Model

The current experimental model uses:

- A vocabulary of 58 unique tokens.
- An embedding dimension of 8.
- A context window of 3 tokens.
- A hidden layer with 16 neurons.
- An output layer that produces scores for all 58 vocabulary tokens.

The current neural network contains 1,850 trainable parameters.

**Important:** The model is currently an untrained experimental neural network. Its purpose at this stage is to understand the architecture and training process. It is not yet capable of reliable natural-language understanding.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SKULL1313/ai-data-analyst.git
```

### 2. Navigate into the project

```bash
cd ai-data-analyst
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install pandas numpy torch
```

### 6. Run the language model experiments

```bash
python model/tokenizer.py
```

```bash
python model/sequence_experiment.py
```

```bash
python model/context_window.py
```

```bash
python model/embedding_experiment.py
```

```bash
python model/neural_network.py
```

## Long-Term Vision

The ultimate objective is to combine a self-developed language model with analytical Python tools.

For example, a user could ask:

"What was our total revenue last month, and which product generated the most revenue?"

The language model would eventually learn to interpret the question, identify the appropriate analytical operation, use Python tools to process the dataset, and communicate the results in natural language.

This project is being developed incrementally, with an emphasis on understanding the mathematics, architecture, and engineering behind modern language models.

## Author

Ryan Kemajou

GitHub: [SKULL1313](https://github.com/SKULL1313)