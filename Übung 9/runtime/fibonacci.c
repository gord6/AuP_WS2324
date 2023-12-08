#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long function_calls = 0;

long long fibonacci(int n) {
    function_calls++;

    if (n <= 1)
        return n;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <n>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);

    clock_t start_time = clock();

    long long result = fibonacci(n);

    clock_t end_time = clock();

    printf("%lld\n", result);
    printf("%lld\n", function_calls); 
    printf("%f\n", ((double) (end_time - start_time)) / CLOCKS_PER_SEC);

    return 0;
}
