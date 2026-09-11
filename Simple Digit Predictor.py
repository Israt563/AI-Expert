import matplotlib
matplotlib.use('Agg')  # Prevents display engine freezes in terminal

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

print("Loading digits dataset...")
digits = load_digits()
X, y = digits.images, digits.target

# Reshape and normalize pixel values
X_flat = X.reshape((len(X), -1)) / 16.0

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_flat, y, test_size=0.2, random_state=42)

print("Training Neural Network Classifier...")
model = MLPClassifier(hidden_layer_sizes=(128,), max_iter=300, random_state=42)
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)
print(f"\nFinal Test Accuracy: {accuracy * 100:.2f}%\n")

# Save visual predictions
plt.figure(figsize=(10, 4))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[i].reshape(8, 8), cmap='gray')
    
    pred = predictions[i]
    true = y_test[i]
    color = 'green' if pred == true else 'red'
    
    plt.title(f"Pred: {pred}\nTrue: {true}", color=color)
    plt.axis('off')

plt.tight_layout()
plt.savefig("digit_results.png")
print("Success! Output saved to 'digit_results.png'. Open it in VS Code to see results.")