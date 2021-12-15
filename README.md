# Distributed-Register
## Task 8
Modeling distributed register platform.

The system must support the following functions:
1) creating a record about a new user;
2) deleting an entry for the selected user;
3) search for a record for some selected user and compare his "certificate" with the sample saved in the system;
4) synchronization of the distributed registry systems - updating information about registered users.

User information should be stored in the following format: user ID, "encrypted" password (secure user certificate). Password encryption is performed directly on the distributed register server side.
The procedure for working with a "distributed register" should be performed in a separate thread so as not to block the work of the main program

### Installation
1) Clone this repository:

**Linux**
```
$ git clone https://github.com/Whywolk/Distributed-Register.git
$ cd ./Distributed-Register
```

2) Install all dependencies:

**Linux**
```
$ pip3 install -r requirements.txt
```

### Usage
Running server:

**Linux**
```
$ python3 server.py port <port> db <sqlite_file_name>
```

Running client:

**Linux**
```
$ python3 client.py
```

### Scheme
![See scheme.svg](./scheme.svg)