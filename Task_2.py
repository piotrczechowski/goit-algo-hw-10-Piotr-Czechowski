import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Defining the function and integration boundary
def f(x):
    return x ** 2

a = 0 # Lower bound
b = 2 # Upper bound

# Monte Carlo integration
def monte_carlo_integration(f, a, b, num_samples=10000):
    x = np.random.uniform(a, b, num_samples)
    y = f(x)
    return (b - a) * np.mean(y)

# Calculate the integral using Monte Carlo method
num_samples = 10000
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)

# Calculate the integral using the quad function from SciPy
quad_result, quad_error = spi.quad(f, a, b)

# Print results
print("Monte Carlo result: ", monte_carlo_result)
print("SciPy quad result: ", quad_result)
print("Quad function error estimate: ", quad_error)

# Plotting the function and the Monte Carlo integration area
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Drawing the function
ax.plot(x, y, 'r', linewidth=2)

# Filling the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Adding random points for Monte Carlo visualization (optional)
# np.random.seed(0)  # For reproducibility
x_random = np.random.uniform(a, b, num_samples)
y_random = np.random.uniform(0, max(y), num_samples)
under_curve = y_random < f(x_random)
ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=1, alpha=0.5)
ax.scatter(x_random[~under_curve], y_random[~under_curve], color='blue', s=1, alpha=0.5)

# Setting up the graph
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Adding integration limits and graph title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Graph of integration of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()
