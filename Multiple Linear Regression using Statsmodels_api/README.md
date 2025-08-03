# 📊 Multiple Linear Regression - GPA Prediction

This notebook explores a multiple linear regression model using SAT scores and a random variable to predict student GPA.

## 🔍 Objective

To understand how to interpret regression coefficients, p-values, R² and adjusted R² — and decide which variables to keep.

## 📈 Model Summary

| Variable     | Coefficient | p-value |
|--------------|-------------|---------|
| SAT          | 0.0017      | 0.000   |
| Rand 1,2,3   | -0.0083     | 0.762   |

- SAT is significant (p < 0.05) → good predictor.
- Rand 1,2,3 is **not significant** (p > 0.05) → should be dropped.

## 🧠 Conclusion

- Even though R² = 0.407, the adjusted R² = 0.392 tells us the second variable adds no value.
- A **simple linear regression with SAT only** would likely be more effective.

> **Moral**: Always check p-values and adjusted R². Use theory + statistics to build better models.
