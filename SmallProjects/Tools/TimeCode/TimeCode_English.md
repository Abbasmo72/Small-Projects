## Execution Time Measurement for Code Sections in Python
This program is designed to measure the execution time of a specific section of code in Python. Here's an explanation of its functionality:
1. Start Timing: The program first records the start time of the execution using the time.time() function. This gives the time in seconds, measured with high precision.
2. Code Section to Measure: The section of code whose execution time we want to measure is placed here. In this example, a simple loop with 1 million iterations is used. This loop is just for testing, but you can replace it with any code whose performance you want to analyze.
3. End Timing: After the code finishes executing, the program records the end time using time.time() again.
4. Calculate Execution Time: The execution time is calculated by subtracting the start time from the end time.
5. Display Execution Time: Finally, the program prints the execution time in seconds, formatted to 4 decimal places.

## Use Case:
This program is useful for measuring and optimizing the performance of code. Especially when comparing the speed of different algorithms or parts of code, this method helps you analyze execution times and make necessary optimizations.

## Python Code
```python
import time  # Import the time module to measure execution time

# Start timing
start_time = time.time()

# Code section to measure

# ------------------------------------
# Insert your code here
for i in range(1000000):  # A simple loop to test execution time
    pass  # Sample code to measure execution time
# ------------------------------------

# End timing
end_time = time.time()

# Calculate and display execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")  # Display execution time in seconds

```
