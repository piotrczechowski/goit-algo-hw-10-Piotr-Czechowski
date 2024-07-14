import pulp

# Create a LP Maximization problem
model = pulp.LpProblem("Maximize_Beverage_Production", pulp.LpMaximize)

# Decision Variables
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Objective Function
model += lemonade + fruit_juice, "Total_Production"

# Constraints
model += 2*lemonade + 1*fruit_juice <= 100, "Water_Constraint"
model += 1*lemonade <= 50, "Sugar_Constraint"
model += 1*lemonade <= 30, "Lemon_Juice_Constraint"
model += 2*fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solve the problem
model.solve()

# Print the results
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade produced: {lemonade.varValue}")
print(f"Fruit Juice produced: {fruit_juice.varValue}")
print(f"Total Production: {pulp.value(model.objective)}")
