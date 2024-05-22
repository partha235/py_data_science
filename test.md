To understand correlation statistics through an example, we will calculate the Pearson correlation coefficient between two sets of data and explain how the correlation is derived using the sum of their deviations from the mean. Let's break down the steps and calculations involved.

### Data
Consider the following two sets of data:

- \( X = [1, 2, 3, 4, 5] \)
- \( Y = [2, 4, 5, 4, 5] \)

### Steps to Calculate Pearson Correlation Coefficient

1. **Calculate the Mean of X and Y:** <br>
   $
   \text{mean}(X) = \frac{1+2+3+4+5}{5} = 3
   $<br>
   $
   \text{mean}(Y) = \frac{2+4+5+4+5}{5} = 4
   $

2. **Calculate the Deviations from the Mean:**
   $
   X' = X - \text{mean}(X) = [1-3, 2-3, 3-3, 4-3, 5-3] = [-2, -1, 0, 1, 2]
   $
   $
   Y' = Y - \text{mean}(Y) = [2-4, 4-4, 5-4, 4-4, 5-4] = [-2, 0, 1, 0, 1]
   $

3. **Calculate the Sum of the Products of Deviations:**
   $
   \sum (X'Y') = (-2 \cdot -2) + (-1 \cdot 0) + (0 \cdot 1) + (1 \cdot 0) + (2 \cdot 1) = 4 + 0 + 0 + 0 + 2 = 6
   $

4. **Calculate the Sum of the Squared Deviations:**
   $
   \sum (X'^2) = (-2)^2 + (-1)^2 + 0^2 + 1^2 + 2^2 = 4 + 1 + 0 + 1 + 4 = 10
   $
   $
   \sum (Y'^2) = (-2)^2 + 0^2 + 1^2 + 0^2 + 1^2 = 4 + 0 + 1 + 0 + 1 = 6
   $

5. **Calculate the Pearson Correlation Coefficient:**
   $
   r = \frac{\sum (X'Y')}{\sqrt{\sum (X'^2) \cdot \sum (Y'^2)}} = \frac{6}{\sqrt{10 \cdot 6}} = \frac{6}{\sqrt{60}} = \frac{6}{\sqrt{60}} = \frac{6}{7.746} \approx 0.7746
   $

### Interpretation

The Pearson correlation coefficient $r \approx 0.7746$ indicates a strong positive linear relationship between the variables  X and Y.

