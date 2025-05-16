import numpy as np
import matplotlib.pyplot as plt

# Given parameters
mu = 5  # ⟨x⟩ = 5
sigmas = [0.5, 1, 2.5]

# Create x values around the mean
x = np.linspace(mu - 10, mu + 10, 1000)

# Plot Gaussian distributions for each sigma
plt.figure(figsize=(10, 6))

for sigma in sigmas:
    rho = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    plt.plot(x, rho, label=f'σ = {sigma}')

plt.title('Gaussian Distributions with ⟨x⟩ = 5')
plt.xlabel('x')
plt.ylabel('ρ(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()