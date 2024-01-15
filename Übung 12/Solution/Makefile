CFLAGS=-std=c99 -Wall -Wpedantic -Werror -g

main: main.o libmyfunctions.a
	$(CC) -o $@ $< -L. -lmyfunctions

libmyfunctions.a: myfunction_number.o myfunction_string.o 
	ar -rcs $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f *.o main libmyfunctions.a