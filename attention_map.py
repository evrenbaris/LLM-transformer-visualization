import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example sentence
tokens = ["The", "quick", "brown", "fox"]
num_tokens = len(tokens)
embedding_dim = 4  # Embedding vector size

# Random embedding vectors
np.random.seed(0)
embeddings = np.random.rand(num_tokens, embedding_dim)

# Query, Key, Value matrices
W_q = np.random.rand(embedding_dim, embedding_dim)
W_k = np.random.rand(embedding_dim, embedding_dim)
queries = embeddings @ W_q
keys = embeddings @ W_k

# Dot-product attention
attention_scores = queries @ keys.T
attention_scores /= np.sqrt(embedding_dim)  # Scaling
attention_weights = np.exp(attention_scores)
attention_weights /= np.sum(attention_weights, axis=1, keepdims=True)

# Visualization
plt.figure(figsize=(8, 6))
sns.heatmap(attention_weights, annot=True, xticklabels=tokens, yticklabels=tokens, cmap="Blues")
plt.title("Self-Attention Mechanism Visualization")
plt.xlabel("Key Tokens")
plt.ylabel("Query Tokens")
plt.show()
