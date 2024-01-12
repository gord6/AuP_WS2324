# Variablen
CC = gcc
CFLAGS=-std=c99 -Wall -Wpedantic -Werror -g

# Regel für die Erstellung der ausführbaren Datei
main: main.o libmyfunction.a
	$(CC) -o $@ $< -L. -lmyfunction

# Regel für die Erstellung der Bibliothek
libmyfunction.a: myfunction.o
	ar rcs $@ $^
	
# Musterregel für die Erstellung der Objektdateien
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Regel zum Aufräumen der generierten Dateien
clean:
	rm -f *.o main libmyfunction.a