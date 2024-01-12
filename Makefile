CFLAGS = -c -Wall
CC = gcc
LIBS =  -lm 

all: testing

debug: CFLAGS += -g
debug: testing

testing: testing.o 
	${CC} testing.o -o testing

testing.o: client/testing.c
	${CC} ${CFLAGS} client/testing.c

clean:
	rm -f *.o *~