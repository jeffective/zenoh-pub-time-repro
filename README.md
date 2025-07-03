# zenoh first pub reproducer

1. clone this repo
2. have docker installed
3. run `docker compose up --attach client-pub`
4. observe behavior of first pub takes longer than subsequent pubs

```
client-pub-1  | Opening session...
client-pub-1  | first pub took: 0.026115057 s
client-pub-1  | second pub took: 0.002108434 s
client-pub-1  | third pub took: 0.001744916 s
```

more info about system that produced this result:

```
$ docker compose version
Docker Compose version v2.36.2
$ docker --version
Docker version 28.2.2, build e6534b4
$ uname -a
Linux jeff-debian 6.1.0-37-rt-amd64 #1 SMP PREEMPT_RT Debian 6.1.140-1 (2025-05-22) x86_64 GNU/Linux
```