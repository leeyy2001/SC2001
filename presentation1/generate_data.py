import random

# We want to create 16 intervals, from 1000 to 10,000, and from 10,000 to 10,000,000.
# The function takes 2 parameters, starting array size and ending array size

def generate_data(start, end):
    min_int = 1
    max_int = 1000  # Change this to your desired maximum value

    # Define the start and end sizes
    # start_size = 1000  # Change this to your desired starting size
    # end_size = 1000000  # Change this to your desired ending size

    # Calculate the step size to create 16 sub-arrays
    step_size = (end - start + 1) // 16
    step_size += 1

    # Create datasets with random integers for each size
    datasets = {}
    current_size = start
    for _ in range(16):
        dataset = [random.randint(min_int, max_int) for _ in range(current_size)]
        datasets[current_size] = dataset
        current_size += step_size

    # Print the sizes of the generated datasets (optional)
    for size, dataset in datasets.items():
        print(f"Size: {size}, Length: {len(dataset)}")

    return datasets

# generate_data(10000, 10000000)
