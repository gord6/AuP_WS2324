# Variablen
CC = gcc
CFLAGS=-std=c99 -Wall -Wpedantic -Werror -g

# Regel für die Erstellung der ausführbaren Datei
main: myfunction.o main.o
	$(CC) myfunction.o main.o -o main

# Regel für die Erstellung der Objektdatei myfunction
myfunction.o: myfunction.c
	$(CC) $(CFLAGS) -c myfunction.c -o myfunction.o

# Regel für die Erstellung der Objektdatei myfunction
main.o: main.c
	$(CC) $(CFLAGS) -c main.c -o main.o

# Regel zum Aufräumen der generierten Dateien
clean:
	rm -f *.o main