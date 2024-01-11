# Variablen
CC = gcc
CFLAGS=-std=c99 -Wall -Wpedantic -Werror -g

# Regel für die Erstellung der ausführbaren Datei
main: myfunction.o main.o
	$(CC) $^ -o $@

# Regel für die Erstellung der Objektdatei myfunction
myfunction.o: myfunction.c
	$(CC) $(CFLAGS) -c $< -o $@

# Regel für die Erstellung der Objektdatei main
main.o: main.c
	$(CC) $(CFLAGS) -c $< -o $@

# Regel zum Aufräumen der generierten Dateien
clean:
	rm -f *.o main