import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Encoder components
G.add_edge("Input Embedding", "Positional Encoding")
G.add_edge("Positional Encoding", "Self-Attention (Encoder)")
G.add_edge("Self-Attention (Encoder)", "Feed-Forward (Encoder)")
G.add_edge("Feed-Forward (Encoder)", "Encoder Output")

# Decoder components
G.add_edge("Target Embedding", "Positional Encoding (Decoder)")
G.add_edge("Positional Encoding (Decoder)", "Masked Self-Attention (Decoder)")
G.add_edge("Masked Self-Attention (Decoder)", "Encoder-Decoder Attention")
G.add_edge("Encoder-Decoder Attention", "Feed-Forward (Decoder)")
G.add_edge("Feed-Forward (Decoder)", "Decoder Output")

# Encoder-Decoder connection
G.add_edge("Encoder Output", "Encoder-Decoder Attention")

# Draw the diagram
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=3000, font_size=10, font_weight="bold")
plt.title("Transformer Architecture Flow Diagram")
plt.show()
