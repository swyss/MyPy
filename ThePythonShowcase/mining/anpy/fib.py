
# Naive rekursive Implementierung von fib(n)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Funktion zur Zählung der Funktionsaufrufe
def count_fib_calls(n, count_dict=None):
    if count_dict is None:
        count_dict = {'count': 0}
    count_dict['count'] += 1

    if n <= 1:
        return n, count_dict['count']
    else:
        fib_n_1, _ = count_fib_calls(n-1, count_dict)
        fib_n_2, calls = count_fib_calls(n-2, count_dict)
        return fib_n_1 + fib_n_2, calls

# Effiziente iterative Implementierung von fib(n)
def fib_efficient(n):
    if n <= 1:
        return n
    fib_0, fib_1 = 0, 1
    for i in range(2, n + 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

# Messung der Ausführungszeit (Beispiel)
import time

# Für die naive rekursive Implementierung
start_time = time.time()
fib_result = fib(10)  # Beispiel für n=10
end_time = time.time()
print(f"Die Ausführung von fib(10) dauerte {end_time - start_time} Sekunden.")

# Für die effiziente Implementierung
start_time_efficient = time.time()
fib_efficient_result = fib_efficient(100)  # Beispiel für n=10
end_time_efficient = time.time()
print(f"Die Ausführung von fib_efficient(10) dauerte {end_time_efficient - start_time_efficient} Sekunden.")
