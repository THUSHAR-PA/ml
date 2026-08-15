# Central Limit Theorem (CLT)

## 1. Definition

The **Central Limit Theorem (CLT)** states that when sufficiently large random samples are taken from a population with a finite mean and variance, the **sampling distribution of the sample mean** becomes approximately normally distributed, regardless of the original shape of the population distribution.

The key point is:

> The population does NOT become normal. The distribution of the sample means becomes approximately normal.

---

# 2. Important Terms

## Population

The complete group we are interested in.

Examples:

* All students in a university
* All customers of a company
* All houses in a city
* All IPL matches

---

## Sample

A smaller group selected from the population.

Example:

```text
Population = 100,000 students
Sample = 100 students
```

---

## Population Mean

The true average of the population.

Symbol:

```text
μ
```

---

## Sample Mean

The average calculated from one sample.

Symbol:

```text
x̄
```

Formula:

```text
x̄ = Σxᵢ / n
```

---

# 3. The Core Idea of CLT

Suppose we have a population.

We repeatedly:

1. Take a random sample.
2. Calculate its mean.
3. Store the mean.
4. Repeat thousands of times.

Example:

```text
Sample 1 → mean = 51.2
Sample 2 → mean = 48.7
Sample 3 → mean = 50.8
Sample 4 → mean = 52.1
Sample 5 → mean = 49.9
...
```

These sample means form a new distribution.

This is called the:

**Sampling Distribution of the Sample Mean**

According to the CLT, this distribution becomes approximately normal as the sample size becomes sufficiently large.

---

# 4. Population Does Not Become Normal

Suppose the original population is highly skewed:

```text
██████████████████
██████████
██████
███
██
█
```

The population remains skewed.

However, if we repeatedly take sufficiently large samples and calculate their means, the distribution of those means becomes approximately:

```text
             █
           ███
         ███████
       ███████████
     ███████████████
   ███████████████████
```

Therefore:

```text
Population distribution
        ≠
Sampling distribution
```

---

# 5. Mathematical Form

If observations have:

```text
Population mean = μ
Population standard deviation = σ
Sample size = n
```

then for sufficiently large `n`:

```text
x̄ ≈ Normal(μ, σ/√n)
```

The mean of the sampling distribution is:

```text
E(x̄) = μ
```

The standard deviation of the sampling distribution is:

```text
σ_x̄ = σ / √n
```

This is called the:

**Standard Error of the Mean (SE or SEM)**

---

# 6. Standard Error

Formula:

```text
SE = σ / √n
```

Example:

```text
σ = 20
```

For:

```text
n = 4
```

```text
SE = 20 / √4
   = 10
```

For:

```text
n = 25
```

```text
SE = 20 / √25
   = 4
```

For:

```text
n = 100
```

```text
SE = 20 / √100
   = 2
```

Therefore:

```text
Sample size increases
        ↓
Standard error decreases
        ↓
Sample means become more concentrated
        ↓
Sampling distribution becomes narrower
```

---

# 7. Sample Size vs Number of Samples

These are different.

## Sample Size

The number of observations in one sample.

Example:

```text
n = 30
```

means each sample contains 30 observations.

---

## Number of Samples

The number of times we repeat the experiment.

Example:

```text
Number of samples = 5000
```

means we take 5000 different samples.

For example:

```text
5000 samples
×
30 observations per sample
```

The CLT experiment might therefore use:

```text
Sample size = 30
Number of samples = 5000
```

---

# 8. Why Does Increasing Sample Size Help?

When we average many observations, unusually high and low values tend to balance each other.

For example:

```text
Small sample:

10, 90
Mean = 50
```

Another sample:

```text
20, 30
Mean = 25
```

The means can vary considerably.

With a larger sample:

```text
10, 90, 45, 50, 55, 40, 60, 48, 52, 50
```

the extreme values have less influence on the overall average.

As sample size increases, sample means tend to cluster around the population mean.

---

# 9. Standardized Form of CLT

The sample mean can be standardized using:

```text
Z = (x̄ - μ) / (σ / √n)
```

where:

```text
x̄ = sample mean
μ = population mean
σ = population standard deviation
n = sample size
```

For sufficiently large samples:

```text
Z ≈ N(0, 1)
```

where:

```text
N(0, 1)
```

is the standard normal distribution.

---

# 10. Example of Z-Score

Suppose:

```text
μ = 100
σ = 20
n = 100
```

First calculate the standard error:

```text
SE = 20 / √100
   = 2
```

Suppose:

```text
x̄ = 104
```

Then:

```text
Z = (104 - 100) / 2
  = 2
```

The sample mean is therefore:

```text
2 standard errors above the population mean.
```

---

# 11. CLT and Confidence Intervals

Suppose:

```text
Sample mean = 72
σ = 10
n = 100
```

Then:

```text
SE = 10 / √100
   = 1
```

For an approximate 95% confidence interval:

```text
x̄ ± 1.96 × SE
```

Therefore:

```text
72 ± 1.96
```

Giving:

```text
70.04 to 73.96
```

When the population standard deviation is unknown, the t-distribution is commonly used instead.

---

# 12. CLT and Hypothesis Testing

CLT helps us determine how unusual a sample mean is under an assumed population mean.

Example:

```text
μ = 100
σ = 15
n = 225
```

Standard error:

```text
SE = 15 / √225
   = 1
```

If:

```text
x̄ = 102
```

then:

```text
Z = (102 - 100) / 1
  = 2
```

The sample mean is approximately two standard errors above the population mean.

This idea is fundamental to many statistical hypothesis tests.

---

# 13. Conditions for CLT

The CLT requires appropriate assumptions.

Important considerations include:

### Random sampling

Observations should generally be randomly sampled.

### Independence

Observations should be independent, or the dependence must be appropriately handled.

### Finite variance

The standard classical CLT assumes a finite population variance.

### Sufficient sample size

The required sample size depends on the population.

A common classroom rule is:

```text
n ≥ 30
```

but this is only a rule of thumb.

There is no universal magic value of 30.

Highly skewed distributions or distributions with extreme outliers may require much larger samples.

---

# 14. CLT Does Not Mean "Everything Becomes Normal"

Incorrect:

```text
CLT says all data becomes normal.
```

Correct:

```text
CLT says the sampling distribution of the
sample mean becomes approximately normal
for sufficiently large samples under suitable
conditions.
```

---

# 15. CLT vs Law of Large Numbers

These concepts are related but different.

## Law of Large Numbers

Focuses on where the sample mean goes.

```text
n increases
    ↓
x̄ approaches μ
```

## Central Limit Theorem

Focuses on the shape of the distribution of sample means.

```text
n increases
    ↓
Sampling distribution of x̄
approaches a normal distribution
```

Easy way to remember:

```text
LLN → WHERE does the mean go?

CLT → WHAT does the distribution look like?
```

---

# 16. Python Demonstration

Install:

```bash
pip install numpy matplotlib
```

Python code:

```python
import numpy as np
import matplotlib.pyplot as plt

# Create a strongly skewed population
population = np.random.exponential(
    scale=2,
    size=100000
)

# User inputs
sample_size = int(
    input("Enter sample size: ")
)

number_of_samples = int(
    input("Enter number of samples: ")
)

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
standard_error = (
    population_std / np.sqrt(sample_size)
)

# Results
print("\n========== CLT RESULTS ==========")

print(
    f"Population Mean       : "
    f"{population_mean:.4f}"
)

print(
    f"Population Std Dev    : "
    f"{population_std:.4f}"
)

print(
    f"Sample Size            : "
    f"{sample_size}"
)

print(
    f"Number of Samples      : "
    f"{number_of_samples}"
)

print(
    f"Mean of Sample Means   : "
    f"{np.mean(sample_means):.4f}"
)

print(
    f"Theoretical Mean       : "
    f"{population_mean:.4f}"
)

print(
    f"Std Dev of Means       : "
    f"{np.std(sample_means):.4f}"
)

print(
    f"Theoretical Std Error  : "
    f"{standard_error:.4f}"
)

# Original population
plt.figure(figsize=(10, 5))

plt.hist(
    population,
    bins=60,
    density=True
)

plt.title(
    "Original Population Distribution"
)

plt.xlabel("Population Values")
plt.ylabel("Density")

plt.show()

# Sampling distribution
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
```

---

# 17. What to Experiment With

Run:

```text
Sample size = 2
Number of samples = 5000
```

Then:

```text
Sample size = 5
Number of samples = 5000
```

Then:

```text
Sample size = 30
Number of samples = 5000
```

Then:

```text
Sample size = 100
Number of samples = 5000
```

Observe the second graph.

You should see approximately:

```text
n = 2
→ More skewed

n = 5
→ Beginning to become regular

n = 30
→ More bell-shaped

n = 100
→ Very close to normal
```

---

# 18. What the Python Program Is Actually Doing

The important loop is:

```python
for _ in range(number_of_samples):

    sample = np.random.choice(
        population,
        size=sample_size,
        replace=False
    )

    sample_mean = np.mean(sample)

    sample_means.append(sample_mean)
```

If:

```text
sample_size = 30
number_of_samples = 5000
```

then:

```text
Sample 1
30 values → mean

Sample 2
30 values → mean

Sample 3
30 values → mean

...

Sample 5000
30 values → mean
```

At the end:

```text
sample_means
```

contains 5000 sample means.

The histogram of these means is the **sampling distribution**.

---

# 19. Why Use an Exponential Population?

The exponential distribution is strongly skewed.

This is intentional.

We want to start with a population that is clearly not normal.

Then we can observe:

```text
Non-normal population
        ↓
Repeated sampling
        ↓
Calculate sample means
        ↓
Sampling distribution
        ↓
Approximately normal
```

That makes the CLT easier to understand visually.

---

# 20. Real-World Applications

CLT is used in:

### Medicine

Estimating average patient measurements.

### Finance

Estimating average returns.

### Manufacturing

Quality control and average product measurements.

### Polling

Estimating population characteristics from samples.

### Economics

Estimating population-level economic quantities.

### Data Science

Statistical inference and uncertainty estimation.

### Machine Learning

Understanding sampling and statistical estimation.

---

# 21. Most Important Formulas

### Sample Mean

```text
x̄ = Σxᵢ / n
```

### Standard Error

```text
SE = σ / √n
```

### Standardized Sample Mean

```text
Z = (x̄ - μ) / (σ / √n)
```

### Sampling Distribution

```text
x̄ ≈ Normal(μ, σ/√n)
```

---

# 22. The Mental Model to Remember

Remember this:

```text
             POPULATION
                  ↓
          Take random sample
                  ↓
             SAMPLE
                  ↓
          Calculate average
                  ↓
            SAMPLE MEAN
                  ↓
          Repeat thousands
             of times
                  ↓
       MANY SAMPLE MEANS
                  ↓
       SAMPLING DISTRIBUTION
                  ↓
       Approximately NORMAL
       when n is sufficiently
             large
```

And:

```text
Mean of sampling distribution = μ

Standard error = σ / √n
```

---

# 23. One-Line Exam Definition

> The Central Limit Theorem states that the sampling distribution of the sample mean approaches a normal distribution as the sample size becomes sufficiently large, with mean μ and standard error σ/√n, provided the required assumptions are satisfied.

---

# 24. One-Line Intuition

> **Take many sufficiently large samples, calculate their means, and those means form an approximately bell-shaped distribution centered around the true population mean.**
