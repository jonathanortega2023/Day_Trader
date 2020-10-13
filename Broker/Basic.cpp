include <stdio.h>
include <SQLAPI.h>

int main(int argc, char* argv[]) {
    SQConnection con;

    try{
        con.Connect(_TSA("my_db"), _TSA("jon"), _TSA("password"), SA_Oracle_Client)
        printf("We are connected!\n")
    }
}