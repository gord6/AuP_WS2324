# Variablen
CC = gcc
CFLAGS=-std=c99 -Wall -Wpedantic -Werror -g

main: myfunction.o main.o
	$(CC) myfunction.o main.o -o main

myfunction.o: myfunction.c
	$(CC) $(CFLAGS) -c myfunction.c -o myfunction.o

main.o: main.c
	$(CC) $(CFLAGS) -c main.c -o main.o

clean:
	rm -f *.o main