# Confidence Intervals — Complete Notes

## 1. What is a Confidence Interval?

A **confidence interval (CI)** is a range of values that we use to estimate an unknown population parameter.

Instead of saying:

```text
The average height of the population is 170 cm.
```

we can say:

```text
The estimated average height is 170 cm,
with a 95% confidence interval of
168 cm to 172 cm.
```

The interval tells us about the **uncertainty in our estimate**.

---

# 2. Why Do We Need Confidence Intervals?

Imagine that a university has:

```text
100,000 students
```

You want to know their average height.

You cannot measure all 100,000 students.

So you randomly select:

```text
100 students
```

and calculate:

```text
Sample mean = 170 cm
```

But is the true population mean exactly 170?

Probably not.

Maybe the true mean is:

```text
169.7
170.2
170.8
```

We don't know.

Therefore, instead of giving only:

```text
170 cm
```

we give a range:

```text
168.5 cm to 171.5 cm
```

This is a confidence interval.

---

# 3. The Basic Idea

Think of it like this:

```text
Population
     ↓
Take a sample
     ↓
Calculate sample mean
     ↓
Estimate population mean
     ↓
Add uncertainty
     ↓
Confidence Interval
```

The confidence interval is therefore:

```text
Estimate ± Margin of Error
```

---

# 4. Basic Formula

For a population mean when the population standard deviation is known:

```text
CI = x̄ ± z × SE
```

where:

```text
x̄ = sample mean

z = critical value

SE = standard error
```

and:

```text
SE = σ / √n
```

Therefore:

```text
CI = x̄ ± z × (σ / √n)
```

---

# 5. What is the Margin of Error?

The **margin of error** tells us how far we extend from the sample estimate.

Formula:

```text
Margin of Error = Critical Value × Standard Error
```

For example:

```text
Sample mean = 170
Margin of error = 2
```

Then:

```text
Confidence Interval:

170 - 2  → 168
170 + 2  → 172
```

So:

```text
CI = [168, 172]
```

---

# 6. Understanding Confidence Level

Common confidence levels are:

```text
90%
95%
99%
```

A higher confidence level means we want to be more confident that our interval procedure captures the true population parameter.

But there is a trade-off:

```text
Higher confidence
       ↓
Larger critical value
       ↓
Wider confidence interval
```

For a two-sided normal-based interval, common critical values are approximately:

| Confidence Level | z-value |
| ---------------- | ------: |
| 90%              |   1.645 |
| 95%              |   1.960 |
| 99%              |   2.576 |

---

# 7. Why Does 95% Appear So Often?

Suppose we repeatedly take random samples and construct a 95% confidence interval from each sample.

Imagine we create:

```text
100 confidence intervals
```

Under the assumptions of the method, approximately:

```text
95 intervals
```

will contain the true population parameter, while approximately:

```text
5 intervals
```

will not.

This is the meaning of the **95% confidence level** in frequentist statistics.

---

# 8. VERY IMPORTANT: What 95% Confidence Does NOT Mean

A common mistake is saying:

> "There is a 95% probability that the true mean is inside this particular interval."

That is not the standard frequentist interpretation.

After the interval has been calculated, the population parameter is treated as fixed.

The interval is random because it depends on the random sample.

A better interpretation is:

> **If we repeatedly used the same procedure to construct 95% confidence intervals, approximately 95% of those intervals would contain the true population parameter.**

For practical communication, people often say:

> "We are 95% confident that the population mean lies between these values."

This is acceptable shorthand, provided you understand the repeated-sampling meaning.

---

# 9. Simple Example

Suppose:

```text
Sample mean = 100
Population standard deviation = 20
Sample size = 100
Confidence level = 95%
```

First calculate the standard error:

```text
SE = σ / √n

SE = 20 / √100

SE = 2
```

For 95% confidence:

```text
z = 1.96
```

Margin of error:

```text
ME = 1.96 × 2

ME = 3.92
```

Therefore:

```text
CI = 100 ± 3.92
```

Lower limit:

```text
100 - 3.92 = 96.08
```

Upper limit:

```text
100 + 3.92 = 103.92
```

Therefore:

```text
95% CI = [96.08, 103.92]
```

---

# 10. Visualizing the Interval

The previous example can be represented as:

```text
96.08                 100                 103.92
  |--------------------|---------------------|
        Margin             Margin
        of Error           of Error

              Sample Mean
```

The center is the sample mean.

The distance from the center to either boundary is the margin of error.

---

# 11. Confidence Interval and CLT

This connects directly to what you just learned about the Central Limit Theorem.

CLT tells us that:

```text
Sampling distribution of x̄
            ↓
Approximately normal
```

So we can use the normal distribution to determine how far sample means are expected to vary.

That gives us:

```text
Sample Mean
     ±
Critical Value × Standard Error
```

which gives the confidence interval.

Therefore:

```text
CLT
 ↓
Sampling distribution
 ↓
Standard error
 ↓
Critical value
 ↓
Confidence interval
```

This is one of the most important connections in introductory statistics.

---

# 12. What is a Critical Value?

The critical value tells us how many standard errors we need to move away from the estimate.

For example:

```text
90% → z = 1.645

95% → z = 1.96

99% → z = 2.576
```

For a 95% interval:

```text
             95%
        <------------>
             |
      -1.96  |  +1.96
             |
```

Approximately 95% of a standard normal distribution lies between:

```text
-1.96 and +1.96
```

---

# 13. Why Does Higher Confidence Give a Wider Interval?

Suppose:

```text
Sample mean = 100
SE = 2
```

### 90% confidence

```text
z = 1.645

ME = 1.645 × 2
   = 3.29
```

Interval:

```text
96.71 to 103.29
```

---

### 95% confidence

```text
z = 1.96

ME = 1.96 × 2
   = 3.92
```

Interval:

```text
96.08 to 103.92
```

---

### 99% confidence

```text
z = 2.576

ME = 2.576 × 2
   = 5.152
```

Interval:

```text
94.848 to 105.152
```

Therefore:

```text
90% → Narrower

95% → Wider

99% → Widest
```

Remember:

```text
More confidence
      ↓
Need more coverage
      ↓
Wider interval
```

---

# 14. Effect of Sample Size

Remember:

```text
SE = σ / √n
```

Therefore, when `n` increases:

```text
n ↑
 ↓
√n ↑
 ↓
SE ↓
 ↓
Margin of Error ↓
 ↓
Confidence Interval becomes narrower
```

Example:

Suppose:

```text
σ = 20
95% confidence
```

### n = 25

```text
SE = 20 / √25
   = 4

ME = 1.96 × 4
   = 7.84
```

Interval around a mean of 100:

```text
92.16 to 107.84
```

---

### n = 100

```text
SE = 20 / √100
   = 2

ME = 1.96 × 2
   = 3.92
```

Interval:

```text
96.08 to 103.92
```

---

### n = 400

```text
SE = 20 / √400
   = 1

ME = 1.96 × 1
   = 1.96
```

Interval:

```text
98.04 to 101.96
```

So:

```text
Larger sample
      ↓
Smaller uncertainty
      ↓
Narrower confidence interval
```

---

# 15. Three Ways to Make a Confidence Interval Narrower

Suppose:

```text
CI = x̄ ± z × σ/√n
```

To make it narrower:

### 1. Increase sample size

```text
n ↑
```

This reduces standard error.

### 2. Reduce variability

```text
σ ↓
```

This reduces standard error.

### 3. Reduce confidence level

For example:

```text
99% → 95% → 90%
```

This reduces the critical value.

But reducing confidence is usually not desirable simply to get a narrower interval.

---

# 16. What if Population Standard Deviation is Unknown?

In real-world problems, we usually don't know:

```text
σ
```

Instead, we estimate it using the sample standard deviation:

```text
s
```

In that situation, we generally use the **t-distribution**.

The formula becomes:

```text
CI = x̄ ± t × (s / √n)
```

where:

```text
x̄ = sample mean

t = t critical value

s = sample standard deviation

n = sample size
```

This is extremely common in real statistical analysis.

---

# 17. Z vs t

### Use Z-based intervals when:

The population standard deviation `σ` is known and the normal approximation is appropriate.

```text
CI = x̄ ± z × σ/√n
```

### Use t-based intervals when:

The population standard deviation is unknown and we estimate it using `s`.

```text
CI = x̄ ± t × s/√n
```

In many practical situations involving an unknown population standard deviation, the t-interval is the standard choice.

---

# 18. Degrees of Freedom

For a one-sample t confidence interval:

```text
df = n - 1
```

For example:

```text
n = 20
```

then:

```text
df = 19
```

The t critical value depends on:

```text
Confidence level
+
Degrees of freedom
```

As the sample size becomes large, the t-distribution gets closer to the standard normal distribution.

---

# 19. Example Using the t-Distribution

Suppose:

```text
Sample mean = 50
Sample standard deviation = 8
Sample size = 25
Confidence level = 95%
```

Degrees of freedom:

```text
df = 25 - 1
   = 24
```

For a two-sided 95% interval with 24 degrees of freedom:

```text
t ≈ 2.064
```

Standard error:

```text
SE = s / √n

SE = 8 / √25

SE = 1.6
```

Margin of error:

```text
ME = 2.064 × 1.6

ME ≈ 3.302
```

Therefore:

```text
CI = 50 ± 3.302
```

So approximately:

```text
46.698 to 53.302
```

---

# 20. Confidence Intervals for Proportions

Confidence intervals aren't only for means.

Suppose you survey:

```text
1000 people
```

and:

```text
620 say YES
```

Sample proportion:

```text
p̂ = 620 / 1000

p̂ = 0.62
```

or:

```text
62%
```

A common large-sample approximate interval is:

```text
p̂ ± z × √[p̂(1-p̂)/n]
```

So confidence intervals can estimate:

* Means
* Proportions
* Differences in means
* Differences in proportions
* Regression coefficients
* Other population parameters

The exact interval method depends on the statistic and assumptions.

---

# 21. Confidence Interval for a Proportion Example

Suppose:

```text
n = 1000
p̂ = 0.62
```

For 95% confidence:

```text
z = 1.96
```

Standard error:

```text
SE = √[p̂(1-p̂)/n]
```

Therefore:

```text
SE = √[(0.62)(0.38)/1000]
```

Approximately:

```text
SE ≈ 0.01535
```

Margin of error:

```text
ME = 1.96 × 0.01535

ME ≈ 0.0301
```

Therefore:

```text
CI = 0.62 ± 0.0301
```

or approximately:

```text
0.5899 to 0.6501
```

As percentages:

```text
58.99% to 65.01%
```

---

# 22. Confidence Interval vs Point Estimate

A **point estimate** gives one number.

Example:

```text
Population mean estimate = 70
```

A **confidence interval** gives a range:

```text
95% CI = 67 to 73
```

Therefore:

```text
Point estimate
      ↓
One number

Confidence interval
      ↓
Range of plausible values
```

The point estimate is usually the center of the interval.

---

# 23. Confidence Interval vs Prediction Interval

These are NOT the same.

### Confidence Interval

Usually estimates an unknown population parameter.

Example:

```text
What is the population's average height?
```

### Prediction Interval

Predicts an individual future observation.

Example:

```text
What height might the next randomly selected student have?
```

Prediction intervals are generally wider because individual observations have more variability than an estimated population mean.

---

# 24. Common Mistakes

## Mistake 1

"95% of the observations lie inside a 95% confidence interval."

Wrong.

A confidence interval is about an estimated population parameter, not about where 95% of individual observations lie.

---

## Mistake 2

"95% probability that the true mean is inside this interval."

This is not the standard frequentist interpretation.

The population mean is fixed; the interval-producing procedure is random.

Better:

> A 95% confidence interval is produced by a method that captures the true parameter in approximately 95% of repeated samples, assuming the method's conditions hold.

---

## Mistake 3

"Higher confidence means a narrower interval."

Wrong.

```text
Confidence ↑
     ↓
Critical value ↑
     ↓
Margin of error ↑
     ↓
Interval gets wider
```

---

## Mistake 4

"Larger sample means wider interval."

Wrong.

Generally:

```text
n ↑
 ↓
SE ↓
 ↓
Interval narrower
```

---

## Mistake 5

"Confidence interval tells us exactly where the population mean is."

No.

It provides an interval estimate based on sample information and a statistical procedure.

---

# 25. Python Demonstration

Install:

```bash
pip install numpy matplotlib scipy
```

The following program lets you experiment with confidence intervals.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# --------------------------------------------
# Confidence Interval Demonstration
# --------------------------------------------

# User inputs
sample_size = int(input("Enter sample size: "))
confidence_level = float(
    input("Enter confidence level (e.g. 0.90, 0.95, 0.99): ")
)

# Create a population
population = np.random.normal(
    loc=100,
    scale=15,
    size=100000
)

# Take one random sample
sample = np.random.choice(
    population,
    size=sample_size,
    replace=False
)

# Sample statistics
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# Degrees of freedom
df = sample_size - 1

# t critical value
alpha = 1 - confidence_level

t_critical = stats.t.ppf(
    1 - alpha / 2,
    df
)

# Standard error
standard_error = sample_std / np.sqrt(sample_size)

# Margin of error
margin_of_error = (
    t_critical * standard_error
)

# Confidence interval
lower = sample_mean - margin_of_error
upper = sample_mean + margin_of_error


# --------------------------------------------
# Display results
# --------------------------------------------

print("\n========== CONFIDENCE INTERVAL ==========")

print(f"Sample Size        : {sample_size}")
print(f"Confidence Level   : {confidence_level * 100:.1f}%")

print(f"\nSample Mean        : {sample_mean:.4f}")
print(f"Sample Std Dev     : {sample_std:.4f}")

print(f"\nDegrees of Freedom : {df}")
print(f"t Critical Value   : {t_critical:.4f}")

print(f"\nStandard Error     : {standard_error:.4f}")
print(f"Margin of Error    : {margin_of_error:.4f}")

print(
    f"\nConfidence Interval:"
    f" [{lower:.4f}, {upper:.4f}]"
)


# --------------------------------------------
# Visualize the confidence interval
# --------------------------------------------

plt.figure(figsize=(10, 4))

plt.errorbar(
    sample_mean,
    0,
    xerr=margin_of_error,
    fmt='o',
    capsize=10,
    markersize=8
)

plt.axvline(
    100,
    linestyle='--',
    linewidth=2,
    label='True Population Mean'
)

plt.axvline(
    lower,
    linestyle=':',
    linewidth=2
)

plt.axvline(
    upper,
    linestyle=':',
    linewidth=2
)

plt.yticks([])

plt.xlabel("Population Mean Estimate")

plt.title(
    f"{confidence_level * 100:.0f}% Confidence Interval"
)

plt.legend()

plt.show()
```

---

# 26. What the Python Program Does

The program:

```text
Creates population
      ↓
Takes a random sample
      ↓
Calculates sample mean
      ↓
Calculates sample standard deviation
      ↓
Calculates standard error
      ↓
Finds t critical value
      ↓
Calculates margin of error
      ↓
Creates confidence interval
      ↓
Plots the result
```

The most important lines are:

```python
standard_error = sample_std / np.sqrt(sample_size)
```

and:

```python
margin_of_error = t_critical * standard_error
```

and:

```python
lower = sample_mean - margin_of_error
upper = sample_mean + margin_of_error
```

---

# 27. Experiment With Sample Size

Run the program several times.

Try:

```text
Sample size = 10
Confidence = 0.95
```

Then:

```text
Sample size = 30
Confidence = 0.95
```

Then:

```text
Sample size = 100
Confidence = 0.95
```

Then:

```text
Sample size = 500
Confidence = 0.95
```

You should notice that the confidence interval generally becomes narrower as sample size increases.

---

# 28. Experiment With Confidence Level

Keep:

```text
Sample size = 100
```

Try:

```text
Confidence = 0.90
```

Then:

```text
Confidence = 0.95
```

Then:

```text
Confidence = 0.99
```

You should see:

```text
90% → narrower

95% → wider

99% → widest
```

---

# 29. The Complete Formula Map

For a mean with known population standard deviation:

```text
SE = σ / √n

ME = z × SE

CI = x̄ ± ME
```

Therefore:

```text
CI = x̄ ± z(σ/√n)
```

For an unknown population standard deviation:

```text
SE = s / √n

ME = t × SE

CI = x̄ ± ME
```

Therefore:

```text
CI = x̄ ± t(s/√n)
```

---

# 30. The Mental Model

Remember:

```text
               SAMPLE
                  ↓
            Sample Mean
                  ↓
          "How uncertain is it?"
                  ↓
          Calculate Standard Error
                  ↓
        Choose Confidence Level
                  ↓
          Find Critical Value
                  ↓
        Calculate Margin of Error
                  ↓
        Mean ± Margin of Error
                  ↓
        CONFIDENCE INTERVAL
```

---

# 31. The Most Important Relationships

### Sample size

```text
n ↑
→ SE ↓
→ CI narrower
```

### Confidence level

```text
Confidence ↑
→ Critical value ↑
→ Margin of error ↑
→ CI wider
```

### Variability

```text
σ or s ↑
→ SE ↑
→ CI wider
```

---

# 32. Connection to CLT

You can now connect everything you've learned:

```text
CENTRAL LIMIT THEOREM
          ↓
Sampling distribution of x̄
is approximately normal
          ↓
Know/estimate its spread
          ↓
Standard Error
          ↓
Choose confidence level
          ↓
Critical value
          ↓
Margin of Error
          ↓
CONFIDENCE INTERVAL
```

So confidence intervals aren't a completely separate topic from CLT.

They build directly on the idea of the sampling distribution.

---

# 33. Quick Revision

```text
Population
    ↓
Sample
    ↓
Sample Mean
    ↓
Estimate Population Mean
    ↓
Standard Error
    ↓
Critical Value
    ↓
Margin of Error
    ↓
Confidence Interval
```

Main formula:

```text
Confidence Interval

= Estimate ± Margin of Error
```

For a mean with known σ:

```text
CI = x̄ ± z(σ/√n)
```

For a mean with unknown σ:

```text
CI = x̄ ± t(s/√n)
```

---

# 34. One-Line Exam Definition

> A confidence interval is an interval estimate calculated from sample data that, under repeated sampling and the assumptions of the procedure, contains the true population parameter at the stated confidence level.

---

# 35. One-Line Intuition

> **A confidence interval gives us a range around our sample estimate to represent the uncertainty caused by sampling.**

---

# 36. Final Mental Picture

If you remember only this, remember:

```text
          SAMPLE
             ↓
       Sample Mean
             ↓
       "It's only an estimate."
             ↓
       Add uncertainty
             ↓
   ┌─────────────────────┐
   │                     │
 Lower       Mean       Upper
 Bound                  Bound
   │                     │
   └─────────────────────┘
             ↓
    Confidence Interval
```

And:

```text
Bigger sample
     ↓
Less uncertainty
     ↓
Narrower CI
```

while:

```text
Higher confidence
     ↓
Need more coverage
     ↓
Wider CI
```
