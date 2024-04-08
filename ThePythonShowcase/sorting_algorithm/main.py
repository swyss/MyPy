import time
import random
import matplotlib.pyplot as plt

class SortingAlgorithm:
    def sort(self, data):
        raise NotImplementedError("This method must be overridden by a subclass.")

    def measure_time(self, data):
        start_time = time.time()
        self.sort(data)
        end_time = time.time()
        return end_time - start_time

class BubbleSort(SortingAlgorithm):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class InsertionSort(SortingAlgorithm):
    def sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            while j >=0 and key < data[j]:
                    data[j+1] = data[j]
                    j -= 1
            data[j+1] = key
        return data

class QuickSort(SortingAlgorithm):
    def sort(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data.pop()
            lesser_elements, greater_elements = [], []
            for element in data:
                if element > pivot:
                    greater_elements.append(element)
                else:
                    lesser_elements.append(element)
            return self.sort(lesser_elements) + [pivot] + self.sort(greater_elements)
class MergeSort(SortingAlgorithm):
    def sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            L = data[:mid]
            R = data[mid:]

            self.sort(L)
            self.sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1
        return data

class HeapSort(SortingAlgorithm):
    def heapify(self, data, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and data[i] < data[l]:
            largest = l

        if r < n and data[largest] < data[r]:
            largest = r

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self.heapify(data, n, largest)

    def sort(self, data):
        n = len(data)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(data, n, i)

        for i in range(n-1, 0, -1):
            data[i], data[0] = data[0], data[i]
            self.heapify(data, i, 0)
        return data
# Function to generate data sets
def generate_data(size, max_val=1000):
    return [random.randint(1, max_val) for _ in range(size)]

# Analyzing the algorithms
algorithms = {
    "Bubble Sort": BubbleSort(),
    "Insertion Sort": InsertionSort(),
    "Quick Sort": QuickSort(),
    "Merge Sort": MergeSort(),
    "Heap Sort": HeapSort()
}

data_sizes = [100, 200, 300, 400, 500, 600]
results = {name: [] for name in algorithms}

for size in data_sizes:
    data = generate_data(size)
    for name, alg in algorithms.items():
        data_copy = data.copy()
        time_taken = alg.measure_time(data_copy)
        results[name].append(time_taken)
        print(f"{name} took {time_taken:.5f} seconds to sort {size} elements.")

# Plotting the results
for name, times in results.items():
    plt.plot(data_sizes, times, label=name)

plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance Analysis')
plt.legend()
plt.show()
