#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to convert a string to bits
char* stringToBits(const char* str) {
    size_t str_len = strlen(str);
    
    // Allocate memory for the binary representation (bits)
    char* bits = (char*)malloc((str_len * 8) + 1);  // Each character is 8 bits, plus null terminator

    if (bits == NULL) {
        fprintf(stderr, "Memory allocation error\n");
        exit(EXIT_FAILURE);
    }

    // Convert each character to its binary representation
    for (size_t i = 0; i < str_len; i++) {
        char currentChar = str[i];
        for (int j = 7; j >= 0; j--) {
            bits[(i * 8) + (7 - j)] = ((currentChar >> j) & 1) + '0';
        }
    }

    // Add null terminator
    bits[str_len * 8] = '\0';

    return bits;
}

int main() {
    // Example usage
    const char* myString = "Hello";
    char* bitResult = stringToBits(myString);

    // Print the binary representation
    printf("Binary representation: %s\n", bitResult);

    // Don't forget to free the allocated memory
    free(bitResult);

    return 0;
}