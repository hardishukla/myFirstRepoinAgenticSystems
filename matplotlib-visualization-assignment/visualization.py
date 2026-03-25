import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create epochs (1 to 10)
epochs = np.arange(1, 11)

# Step 2: Generate synthetic training loss
np.random.seed(42)  # for reproducibility
loss = np.exp(-0.3 * epochs) + np.random.normal(0, 0.02, size=len(epochs))

# Step 3: Line Plot (Loss vs Epoch)
plt.figure("Line Plot", figsize=(8, 5))
plt.plot(epochs, loss, marker='o', linestyle='-', label='Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss vs Epoch')
plt.grid(True)
plt.legend()
plt.show()

# Step 4: Scatter Plot (Epoch vs Loss)
plt.figure("Scatter Plot", figsize=(8, 5))
plt.scatter(epochs, loss)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Scatter Plot of Loss vs Epoch')
plt.grid(True)
plt.show()

# Step 5: Bar Chart (Model Accuracy Comparison)
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure("Bar Chart", figsize=(8, 5))
plt.bar(models, accuracy)
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.ylim(0.8, 1.0)
plt.grid(axis='y')
plt.show()