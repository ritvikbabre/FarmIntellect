from productivity_optimizer import ProductivityOptimizer

# Test with sample input
optimizer = ProductivityOptimizer()

# Define test input
sample_input = {
    'Rainfall_mm': 897.08,
    'Temperature_Celsius': 27.68,
    'Fertilizer_Used': 1,
    'Irrigation_Used': 1,
    'Days_to_Harvest': 122
}

# Get optimization results
result = optimizer.optimize(sample_input)
print("Productivity Optimization:", result)
