**Come back to "Summary of regression" part in order to understand the ml-pipeline for the regression model once more**

<!-- -------------------------- -->
#         Grounds to cover        #
<!-- -------------------------- -->

**Model**
- Linear regression
- Regularization:
  - Ridge
  - Lasso

*Model can be compared as a Class and a particular fit can be considered as an object of that model*

**Optimization algorithm**
- Gradient descent
- Coordinate descent

**Concept**
- Loss function
- Bias variance tradeoff
- Cross validation
- Sparsity
- Overfitting
- Model selection
- Feature selection

<!-- -------------------------- -->
#             Modules             #
<!-- -------------------------- -->

*Module 1*: Simple regression
  Single feature/input (eg. size of the house) Single output (eg. price of the house)
  - Define *godness of fit* metric for each possible line.
  - Using *Gradient descent algorithm*:
    - get estimated parameters
    - use them to form predictions

*Module 2*: Multiple regression
  - Again single input and single output, but more complex relationship than just a simple line.
  - Also, more inputs and single output.

*Module 3*: Assessing performance of our model
  - Measures of error (define function of model complexity):
    - Training error
    - Testing error
    - *True error* (generalization)
  - Bias Variance Tradeoff:
    Simple models are easy to form but not really flexible, on the other hand complex models are flexible thats why they tend to be overfit. Now the problem is to find the sweet-spot.

*Module 4*: Ridge regression
  A way to handle bias variance trade: *ridge regression*.
  It defines the balance between how much we emphasize the fit to data versus model complexity. For this in ridge regression there's a parameter that balances between these two terms. And to define this parameter we'll use *cross validation*.

  Helps to define:
  - measure of fit
  - measure of model complexity
  + Ridge total cost = measure of fit + measure of model complexity

*Module 5*:
  - Feature selection
  - Lasso regression
  - Coordinate descent algorithm

*Module 6*: Nearest neighbor regression & Kernel regression
