import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# Central Limit Theorem Demonstration
# ------------------------------------------------

# Create a non-normal population
population = np.random.exponential(scale=2, size=100000)

# User inputs
sample_size = int(input("Enter sample size (e.g. 5, 30, 100): "))
number_of_samples = int(input("Enter number of samples (e.g. 5000): "))

# Population statistics
population_mean = np.mean(population)
population_std = np.std(population)

# Store sample means
sample_means = []

for _ in range(number_of_samples):
    sample = np.random.choice(
        population,
        size=sample_size,
        replace=False
    )

    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

sample_means = np.array(sample_means)

# Theoretical standard error
standard_error = population_std / np.sqrt(sample_size)

# ------------------------------------------------
# Results
# ------------------------------------------------

print("\n========== CENTRAL LIMIT THEOREM ==========")

print(f"Population Mean        : {population_mean:.4f}")
print(f"Population Std Dev     : {population_std:.4f}")

print(f"\nSample Size             : {sample_size}")
print(f"Number of Samples       : {number_of_samples}")

print(f"\nMean of Sample Means    : {np.mean(sample_means):.4f}")
print(f"Theoretical Mean        : {population_mean:.4f}")

print(f"\nStd Dev of Sample Means : {np.std(sample_means):.4f}")
print(f"Theoretical Std Error   : {standard_error:.4f}")

# ------------------------------------------------
# Original Population
# ------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    population,
    bins=60,
    density=True
)

plt.title("Original Population Distribution")
plt.xlabel("Population Values")
plt.ylabel("Density")

plt.show()

# ------------------------------------------------
# Sampling Distribution
# ------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    sample_means,
    bins=50,
    density=True
)

plt.axvline(
    population_mean,
    linestyle="--",
    linewidth=2,
    label="Population Mean"
)

plt.title(
    f"Sampling Distribution of Sample Means\n"
    f"Sample Size = {sample_size}"
)

plt.xlabel("Sample Mean")
plt.ylabel("Density")

plt.legend()

plt.show()