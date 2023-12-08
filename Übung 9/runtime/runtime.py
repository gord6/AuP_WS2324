import matplotlib.pyplot as plt
import subprocess 

def measure_runtime(n):
    command = f"./fibonacci {n}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    lines = result.stdout.strip().split('\n')

    if len(lines) >= 3:
        result_value = int(lines[0])
        function_calls = int(lines[1])
        runtime = float(lines[2])

        return result_value, function_calls, runtime
    else:
        print(f"Fehler beim Extrahieren der Informationen für n={n}")
        return None


n_values = list(range(1, 45))

results = [measure_runtime(n) for n in n_values]
result_values, function_calls, runtimes = zip(*results)

plt.plot(n_values, runtimes, marker='o')
plt.title('Laufzeit des Fibonacci-Programms für verschiedene n-Werte')
plt.xlabel('n')
plt.ylabel('Laufzeit (Sekunden)')
plt.grid(True)
plt.savefig('fibonacci_runtimes.pdf')