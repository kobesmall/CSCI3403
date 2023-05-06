#include "stdio.h"

void vuln();
void login(int);

int main() {
    vuln();
    return 0;
}

void vuln() {
    char buf[20];

    printf("Enter password: ");
    gets(buf);

    printf("Invalid password\n");
}

void login(int is_admin) {
    if (is_admin == 1) {
        puts("Welcome, admin!\n");
    }
    else {
        puts("Welcome, user!\n");
    }
}

