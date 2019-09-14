# TOR control w/ Python stem

This is a quick proof of concept to show how to change the path (therefore the end-node public IP) of a TOR/Privoxy container.

More simply put: change your public IP address with Python while hiding yo' tracks.

## Walkthrough

```
pip install requirements.txt
python change-ip.py
```

## Docker
Easy enough with docker-compose:
```
docker-compose up
```

Manual single docker creation if you don't want to use docker-compose:
```
docker run -it \
       -p 8118:8118 \
       -p 9050:9050 \
       -p 9051:9051 \
       --name tor-test \
       -d dperson/torproxy \
       -p password
```

Change "password" in docker and the scripts for production.
