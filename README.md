# My Honey Pot

A honeypot is a network-based system set up as a decoy to attract hackers and malicious agents to detect, deflect, or study/observe their behavior. This honeypot uses machine learning to identify and log suspected malicious attempts.

Run ``` python mhp.py {your ip} {port} ``` to start honeypot server 

In another shell, run ``` telnet {your ip} {port} ``` to test connection 

A file called "log.txt" will be created with information on the connections 

Configure your email username/password in the config file, then run: 
```
python mhp.py {your ip} {port} {source}
```
to send alerts to specified email

*The provided source can be malicious or not and is used as a proof of concept for this project
