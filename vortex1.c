#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//solution for vortex1 network programming challenge
//man fuck C this took us forever just cause of the dumb union thing oh well

int main(int argc, char *argv[]){
    
    int status;
    struct addrinfo hints;
    struct addrinfo *servinfo;  // will point to the results

    memset(&hints, 0, sizeof hints); // make sure the struct is empty
    hints.ai_family = AF_UNSPEC;     // don't care IPv4 or IPv6
    hints.ai_socktype = SOCK_STREAM; // TCP stream sockets
    //hints.ai_socktype = SOCK_DGRAM; 
    
    if (status = getaddrinfo("vortex.labs.overthewire.org", "5842", &hints, &servinfo) != 0) {
        fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
        exit(1);
    }
    
    int s = socket(servinfo->ai_family, servinfo->ai_socktype, servinfo->ai_protocol); //socket, this is the big one

    connect(s, servinfo->ai_addr, servinfo->ai_addrlen); //connect to dis shit
    
    int x = 0;
    uint32_t sum = 0;
    
    //this works dont fucking question why
    for (x = 0; x < 4; x++)
    {
        union {
            char chars[4];
            uint32_t i;
        } data;

        int rec = recv(s, data.chars, 4, 0);
        printf("recieved: %d\n", rec);
        if(rec == 0 || rec == -1){
            fprintf(stderr, "fk %d", rec);
            exit(1);
        }
        printf("%d\n", data.i);
        sum += data.i;
    }
    printf("Sum = %d\n", sum);
    
    int bytes_sent = send(s, &sum, sizeof sum, 0);
    if(bytes_sent == -1){
        fprintf(stderr, "bigfk");
    }
    char buf[100];
    
    int bytes_rec;
    if ((bytes_rec = recv(s, buf, 99, 0)) == -1) {
        perror("recv");
        exit(1);
    }
    buf[bytes_rec] = '\0';

    printf("username and password: '%s'\n", buf);

    close(s);
    freeaddrinfo(servinfo);
    return 0;
}




