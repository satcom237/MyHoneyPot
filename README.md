# My Honey Pot

Run ``` python mhp.py {your ip} {port} ``` to start honeypot server 

In another shell, run ``` telnet {your ip} {port} ``` to test connection 

A file called "log.txt" will be created with information on the connections 

Configure your email username/password in the config file, then run: 
```
python mhp.py {your ip} {port} m
```
to send alert to specified email
