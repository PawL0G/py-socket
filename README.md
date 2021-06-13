## Core of Event Log REST Service

in Python, without any REST interface itself or so, just _core_ (sockets, threading, typing)

### Functionality:

- Pushing new event to the top of the stream. Service
consumes events in the form of a string like just won a lottery
- '#update @all Object format and stores in memory
- Getting 10 last events from the top of the stream
    * by category (#update, #poll, #warn)
    * by person (@all, @john, @all-friends)
    * by time
