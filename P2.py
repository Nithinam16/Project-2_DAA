import heapq
import time
import random
import matplotlib.pyplot as plt
import numpy as np

def merge_cost(lists):
    """Compute minimum total merge cost using a heap."""
    heapq.heapify(lists)
    total_cost = 0

    while len(lists) > 1:
        first = heapq.heappop(lists)
        second = heapq.heappop(lists)
        merged = first + second
        total_cost += merged
        heapq.heappush(lists, merged)

    return total_cost

def measure_time(n):
    """Generate random list sizes and measure execution time (ns) and total merge cost."""
    sizes = [random.randint(1, 1000) for _ in range(n)]
    start = time.perf_counter_ns()
    total_cost = merge_cost(sizes)
    end = time.perf_counter_ns()
    elapsed_ns = end - start  # elapsed time in nanoseconds
    return elapsed_ns, total_cost

def main():
    input_sizes = [100, 500, 1000, 2000, 4000, 6000, 8000]
    times_ns = []
    total_costs = []

    # Measure experimental times and total merge cost
    for size in input_sizes:
        elapsed, cost = measure_time(size)
        times_ns.append(float(elapsed))
        total_costs.append(cost)

    # Theoretical O(n log n) in ns (scaled to experimental times)
    n_log_n = [float(n * np.log2(n)) for n in input_sizes]
    scale_factor = np.mean(times_ns) / np.mean(n_log_n)
    theoretical = [x * scale_factor for x in n_log_n]

    total_data_points = len(input_sizes)

    # Print scaling factor and total data points
    print(f"Scaling Constant (scale_factor): {scale_factor:.12f}")
    print(f"Total Data Points: {total_data_points}\n")

    # Print table with experimental, theoretical, and total merge cost
    print(f"{'Input Size':>10} | {'Experimental (ns)':>20} | {'Theoretical (ns)':>20} | {'Total Merge Cost':>18}")
    print("-" * 80)
    for n, t_exp, t_theo, cost in zip(input_sizes, times_ns, theoretical, total_costs):
        print(f"{n:10d} | {t_exp:20.0f} | {t_theo:20.0f} | {cost:18d}")

    # Plot results
    plt.figure(figsize=(8, 5))
    plt.plot(input_sizes, times_ns, 'bo-', label="Actual Execution Time (ns)")
    plt.plot(input_sizes, theoretical, 'r--', label="O(n log n) Theoretical (ns)")
    plt.title("Optimal Merge Pattern: Time Complexity Analysis")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (nanoseconds)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
