#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <sys/socket.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <libgen.h>

#define BUFF_SIZE 2048

/**
 * @fn inputString
 * @brief a warpper for string input using fgets
 * @param buff: a pointer to a string contains input from keyboard (stdin)
*/
void inputString(char* buff) {
    memset(buff, '\0', (strlen(buff)));
    fflush(stdin);
    fgets(buff, BUFF_SIZE, stdin);
    buff[strcspn(buff, "\n")] = 0;
}

/**
 * @fn mergeString
 * @brief Merge command (e.g. USER) and user input (e.g. admin) into a string in order to send to server later
 * @param command: a pointer to a string contains command (e.g. USER)
 * @param input: a pointer to a string contains user input (e.g. admin)
*/
void mergeString(char* buff, char* command, char* input) {
    strcpy(buff, command);
    strcat(buff, " ");
    strcat(buff, input);
}

/**
 * @fn showMenu
 * @brief Show user-friendly input menu for client
*/
void showMenu() {
    printf("\n*********************************************");
    printf("\nChoose your option by enter the number below (1-3):");
    printf("\n1. Login");
    printf("\n2. Post article");
    printf("\n3. Logout");
    printf("\n4. Exit");
    printf("\nEnter your option (1-3): ");
}


/**
 * @fn codeToMessage
 * @brief Convert received code from server to corresponding message using a converter text file
 * @param responseCode: a pointer to a string contains received code from server
 * @param responseMessage: a pointer to a string contains corresponding message converted from responseCode
*/
void codeToMessage(char *responseCode, char* responseMessage) {
    char code[BUFF_SIZE];

    FILE *f;
    f = fopen("response_code.txt","r");

    if (f != NULL) {
        // Read code and message from response_code.txt. Using %[^\n\t] to read string included space
        while(fscanf(f,"%s %[^\n\t]", code, responseMessage) != EOF) {
            if (strcmp(code, responseCode) == 0) {
                fclose(f);
                return;
            }
        }
        fclose(f);
        strcpy(responseMessage, responseCode);
        return;
    }
    strcpy(responseMessage, "Response code decoding file not found.");
}

int main(int argc, char **argv) {
    // There are only 3 arguments (./client, ip address and port number)
    if (argc != 3) {
        return 1;
    }

    int client_sock;
    char buff[BUFF_SIZE], receivedMessage[BUFF_SIZE];
    struct sockaddr_in server_addr;
    int msg_len, sent_bytes, received_bytes;

    char command[BUFF_SIZE], input[BUFF_SIZE];
    int option;

    // Construct TCP socket
    if ((client_sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("\nError: ");
        exit(EXIT_FAILURE);
    }

    int server_port = atoi(argv[2]);

    // Specify server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port);
    server_addr.sin_addr.s_addr = inet_addr(argv[1]);

    // Request to connect server
    if (connect(client_sock, (struct sockaddr*) &server_addr, sizeof(struct sockaddr)) < 0) {
        perror("\nError: ");
        exit(EXIT_FAILURE);
    }

    memset(buff, '\0', (strlen(buff)+1));
    received_bytes = recv(client_sock, buff, BUFF_SIZE, 0);
    if (received_bytes < 0) {
        perror("\nError: ");
    }
    else if (received_bytes == 0) {
        printf("Connection closed\n");
        exit(EXIT_FAILURE);
    }
    else {
        buff[received_bytes] = '\0';
        printf("%s\n", receivedMessage); // Print welcome message
    }

    // Communicate with server
    FILE *f;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    f = fopen("testing_send.txt","r");
    if (f == NULL) exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, f)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);

        msg_len = strlen(line);
        sent_bytes = send(client_sock, line, msg_len, 0);

        if (sent_bytes < 0) {
            perror("\nError: ");
            exit(EXIT_FAILURE);
        }
        if (sent_bytes == 0) {
            printf("Connection closed\n");
            exit(EXIT_FAILURE);
        }

        received_bytes = recv(client_sock, buff, BUFF_SIZE, 0);
        if (received_bytes < 0) {
            perror("\nError: ");
            exit(EXIT_FAILURE);
        }
        if (received_bytes == 0) {
            printf("Connection closed\n");
            exit(EXIT_FAILURE);
        } 

        buff[received_bytes] = '\0';
        // codeToMessage(buff, receivedMessage);
        printf("%s\n", buff);

    }

    // msg_len = strlen(buff);
    // sent_bytes = send(client_sock, buff, msg_len, 0);

    // if (sent_bytes < 0) {
    //     perror("\nError: ");
    //     exit(EXIT_FAILURE);
    // }
    // if (sent_bytes == 0) {
    //     printf("Connection closed\n");
    //     exit(EXIT_FAILURE);
    // }

    // received_bytes = recv(client_sock, buff, BUFF_SIZE, 0);
    // if (received_bytes < 0) {
    //     perror("\nError: ");
    //     exit(EXIT_FAILURE);
    // }
    // if (received_bytes == 0) {
    //     printf("Connection closed\n");
    //     exit(EXIT_FAILURE);
    // } 

    // buff[received_bytes] = '\0';
    // codeToMessage(buff, receivedMessage);
    // printf("%s\n", receivedMessage);     

    // Close socket
    close(client_sock);
    return 0;
}