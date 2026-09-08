import time
import tracemalloc

# Large dataset size
N = 10_000_000

print("----- LIST-BASED PROCESSING -----")

# Start memory tracking
tracemalloc.start()

# Start timer
start_time = time.perf_counter()

# Create and process list
numbers_list = [x for x in range(N)]
result_list = sum(x * x for x in numbers_list)

# Stop timer
end_time = time.perf_counter()

# Get memory usage
current, peak = tracemalloc.get_traced_memory()

print("Result:", result_list)
print("Execution Time:", end_time - start_time, "seconds")
print("Peak Memory Usage:", peak / (1024 * 1024), "MB")

tracemalloc.stop()


print("\n----- GENERATOR-BASED PROCESSING -----")

# Start memory tracking
tracemalloc.start()

# Start timer
start_time = time.perf_counter()

# Create and process generator
numbers_generator = (x for x in range(N))
result_generator = sum(x * x for x in numbers_generator)

# Stop timer
end_time = time.perf_counter()

# Get memory usage
current, peak = tracemalloc.get_traced_memory()

print("Result:", result_generator)
print("Execution Time:", end_time - start_time, "seconds")
print("Peak Memory Usage:", peak / (1024 * 1024), "MB")

tracemalloc.stop()