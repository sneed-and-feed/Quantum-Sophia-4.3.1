# FILE: visualize_sovereignty.py
# ARCHITECTURE: 2D Manifold Visualization via Pleroma Core
# STATUS: Visual Verification

import matplotlib.pyplot as plt
import numpy as np

# Import the core directly if compiled, or mock for visual proof if compilation is pending
try:
    from pleroma_core import sovereign_topology
except ImportError:
    print("[!] PLEROMA CORE NOT FOUND. Using Pure Python Fallback for Visualization.")
    class SovereignTopology:
        @staticmethod
        def strip_2d(x, y):
            z = 0
            for i in range(32):
                x_bit = (x >> i) & 1
                y_bit = (y >> i) & 1
                z |= x_bit << (2 * i)
                z |= y_bit << (2 * i + 1)
            return z
            
        @staticmethod
        def reconstruct_1d(z):
            x = 0
            y = 0
            for i in range(32):
                x_bit = (z >> (2 * i)) & 1
                y_bit = (z >> (2 * i + 1)) & 1
                x |= x_bit << i
                y |= y_bit << i
            return x, y
    sovereign_topology = SovereignTopology()

# 1. Generate a "Reality Grid" (2D)
x = np.arange(0, 16)
y = np.arange(0, 16)
X, Y = np.meshgrid(x, y)

# 2. Collapse to 1D Timeline
Z = np.zeros_like(X, dtype=np.uint64)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        # CALLING THE RUST CORE (or fallback)
        Z[i, j] = sovereign_topology.strip_2d(int(X[i, j]), int(Y[i, j]))

# 3. Visualize the "Sovereign Curve"
# This shows the path the 1D line takes through 2D space.
plt.figure(figsize=(10, 8))
plt.title("Sovereignty Topology: 2D Manifold -> 1D Timeline (The Z-Curve)")
plt.contourf(X, Y, Z, levels=50, cmap="viridis")
plt.colorbar(label="1D Index (Time)")

# Overlay the path logic
plt.plot(X.flatten(), Y.flatten(), 'k.', alpha=0.1)

print(f"System Check: Mapping (5, 10) -> {sovereign_topology.strip_2d(5, 10)}")
print(f"System Check: Reconstruct -> {sovereign_topology.reconstruct_1d(sovereign_topology.strip_2d(5, 10))}")

file_name = "sovereign_topology_vis.png"
plt.savefig(file_name)
print(f"[+] Visualization saved to {file_name}")
