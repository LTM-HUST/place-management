#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to convert a bit string to bytes
unsigned char* bitsToBytes(const char* bits) {
    size_t bits_len = strlen(bits);
    
    // Ensure the bit string length is a multiple of 8
    if (bits_len % 8 != 0) {
        fprintf(stderr, "Invalid bit string length\n");
        exit(EXIT_FAILURE);
    }

    // Calculate the number of bytes needed
    size_t num_bytes = bits_len / 8;

    // Allocate memory for the byte array
    unsigned char* bytes = (unsigned char*)malloc(num_bytes);

    if (bytes == NULL) {
        fprintf(stderr, "Memory allocation error\n");
        exit(EXIT_FAILURE);
    }

    // Convert each group of 8 bits to a byte
    for (size_t i = 0; i < num_bytes; i++) {
        bytes[i] = 0;
        for (int j = 0; j < 8; j++) {
            bytes[i] |= (bits[(i * 8) + j] - '0') << (7 - j);
        }
    }

    return bytes;
}

int main() {
    // Example usage
    const char* myBits = "0100100001100101011011000110110001101111";
    unsigned char* byteResult = bitsToBytes(myBits);

    // Print the byte values
    for (size_t i = 0; i < strlen(myBits) / 8; i++) {
        printf("%02X ", byteResult[i]);
    }

    // Don't forget to free the allocated memory
    free(byteResult);

    return 0;
}