
import sys
import time

def get_new_data():
  with open("/home/aluno/trabalho/lista.txt", "r") as file:
    data = file.readlines()

  data = [line.strip() for line in data]
  return data

# Bubble Sort

bubble_sort_data = get_new_data()

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):

            if data[j] > data[j + 1]:
                auxiliary = data[j]
                data[j] = data[j + 1]
                data[j + 1] = auxiliary
    return data


started_at = time.time()

bubble_sort(bubble_sort_data)

finished_at = time.time()

time_bubble = finished_at - started_at

memory_bubble = sys.getsizeof(bubble_sort_data)

print("Bubble Sort:", bubble_sort_data[:10])
print("Tempo do bubble:", time_bubble, "segundos")
print("Memoria do bubble:", memory_bubble, "bytes")

#Selection Sort
selection_sort_data = get_new_data()

def selection_sort(data):
    for i in range(len(data)):
        smaller = i

        for j in range(i + 1, len(data)):
            if data[j] < data[smaller]:
                smaller = j

        auxiliary = data[i]
        data[i] = data[smaller]
        data[smaller] = auxiliary

    return data


started_at = time.time()

selection_sort(selection_sort_data)

finished_at = time.time()

time_selection = finished_at - started_at
memory_selection = sys.getsizeof(selection_sort_data)

print("Selection Sort: ", selection_sort_data[:10])
print("Tempo do selection: ", time_selection, " segundos")
print("Memoria do selection: ", memory_selection, " bytes")

# Insertion Sort

insertion_sort_data = get_new_data()

def insertion_sort(data):

    for i in range(1, len(data)):
        actual = data[i]
        j = i - 1

        while j >= 0 and data[j] > actual:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = actual

    return data


started_at = time.time()

insertion_sort(insertion_sort_data)

finished_at = time.time()

time_insertion = finished_at - started_at
memory_insertion = sys.getsizeof(insertion_sort_data)

print("Insertion Sort: ", insertion_sort_data[:10])
print("Tempo do insertion: ", time_insertion, " segundos")
print("Memoria do insertion: ", memory_insertion, " bytes")
