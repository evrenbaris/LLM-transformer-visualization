import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Positional Encoding Function
def positional_encoding(max_len, d_model):
    pos_enc = np.zeros((max_len, d_model))
    for pos in range(max_len):
        for i in range(0, d_model, 2):
            pos_enc[pos, i] = np.sin(pos / (10000 ** (2 * i / d_model)))
            if i + 1 < d_model:
                pos_enc[pos, i + 1] = np.cos(pos / (10000 ** (2 * i / d_model)))
    return pos_enc

# Parameters
max_len = 10  # Sentence length
d_model = 8   # Embedding dimension

# Calculate Positional Encoding
pos_enc = positional_encoding(max_len, d_model)

# Visualization
plt.figure(figsize=(10, 6))
sns.heatmap(pos_enc, cmap="viridis", annot=False)
plt.title("Positional Encoding Visualization")
plt.xlabel("Embedding Dimension")
plt.ylabel("Word Position")
plt.show()
