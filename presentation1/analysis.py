import matplotlib.pyplot as plt
from statistics import mean 
import csv
import numpy as np
import time

from hybridsort import hybridsort
from insertionsort import insertionSort
from mergesort import mergeSort
from generate_data import generate_data

# Assignment 1: Keep threshold, S, constant plot key comparisons over different sizes of input list, n.
def assign1():
    comparisons = []
    print("Generating datasets")
    datasets = generate_data(10000, 10000000)
    input_sizes = datasets.keys()

    print("Performing hybridsort now")
    for data in datasets.values():
        comparison = hybridsort(data, 5)
        comparisons.append(comparison)

    print("Wrinting to csv")
    with open("assign1_data.csv", 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the integers to the CSV file as a single row
        csv_writer.writerow(comparisons)
    
    print("Plotting data")
    plt.plot(input_sizes, comparisons, marker='o')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Number of Comparisons')
    plt.title('Number of Comparisons vs. Input Size')
    plt.grid(True)
    plt.show()

# assign1()

# Assignment 2: Given a fixed sized input array, n, determine the optimal value of S
# We shall set n to 10000

def assign2():
    print("Generating datasets")
    # datasets = generate_data(1000, 10000)
    # dataset = list(datasets.values())[-1]
    # print("dataset: ", dataset)
    dataset = list(np.random.randint(1, 1000, 10000))
    print("Dataset: ", dataset)

    print("Performing hybridsort")
    comparisons = []
    s_values = []
    time_array = []
    for S in range(1, len(dataset)//2, len(dataset)//2//25):
        s_values.append(S)
        start = time.time()
        comparison = hybridsort(dataset.copy(), S)
        comparisons.append(comparison)
        end = time.time()
        time_array.append(end - start)

    print("Comparisons: ",comparisons)
    print("s_values: ", s_values)
    
    print("Plotting data")
    plt.plot(s_values, time_array, marker='o')
    plt.xlabel('Threshold Size (S)')
    plt.ylabel('Number of Comparisons')
    plt.title('Number of Comparisons vs. Threshold Size')
    plt.grid(True)
    plt.show()
    
# assign2()

# The average time of hybridSort of 10 arrays per input array length, n
def avgTime():
    print("Generating datasets")
    dataset = list(np.random.randint(1, 1000, 10000))
    # print("Dataset: ", dataset)

    print("Performing hybridsort")
    time_per_iter = []
    s_values = []
    time_array = []
    # Optimal range of S is 0 to 20
    for S in range(1, 20):
        s_values.append(S)
        for iteration in range(25):
            dataset = list(np.random.randint(1, 1000, 10000))

            start = time.perf_counter()
            comparison = hybridsort(dataset, S)
            end = time.perf_counter()
            time_per_iter.append(end - start)

        avg_time = mean(time_per_iter)
        time_array.append(avg_time)
        time_per_iter = []

    print("Plotting data")
    plt.plot(s_values, time_array, marker='o')
    plt.xlabel('Threshold Size (S)')
    plt.ylabel('Time')
    plt.title('Time vs. Threshold Size')
    plt.grid(True)
    plt.show()

avgTime()
        

# Find the optimal value for the threshold, S.
def assign3():
    comparisons_insertion = []
    comparisons_merge = []
    time_insertion = []
    time_merge = []
    size = []
    # 0, 10000, 10000//16
    # np.random.randint(1, 1000, 1000 + i)
    for i in range(0, 20, 1 ):
        dataset = list(np.random.randint(1, 1000, i))
        size.append(len(dataset))
        
        start_insertion = time.perf_counter_ns()
        comparison_i, arr = insertionSort(dataset.copy())
        end_insertion = time.perf_counter_ns()
        time_insertion.append(end_insertion - start_insertion)
        print("End Time: ", end_insertion)
        print("Start Time: ", start_insertion)
        comparisons_insertion.append(comparison_i)
        
        start_merge = time.perf_counter_ns()
        comparison_m = mergeSort(dataset.copy())
        end_merge = time.perf_counter_ns()
        time_merge.append(end_merge - start_merge)
        comparisons_merge.append(comparison_m)

    # print(comparions_insertion)
    print(comparisons_merge)

    # print(time_insertion)
    # print(time_merge)

    print("Plotting data")
    plt.plot(size, comparisons_insertion, label="Insertion Sort")
    plt.plot(size, comparisons_merge, label="Merge Sort")
    plt.xlabel('Array Size')
    plt.ylabel('Number of Comparisons')
    plt.title('Number of Comparisons vs. Array Size')
    plt.grid(True)
    plt.legend()
    plt.show()

# assign3()