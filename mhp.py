import sys
import time
import socket
import smtplib
import config

def sendEmail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Email sent successfully")
    except:
        print("Email failed to send")

def writeLog(address, port):
    fopen = open('./log.txt', 'a')
    fopen.write('Time: %s\n IP: %s\n Port: %d\n\n' % (time.ctime(), address, port))
    fopen.close()

def main(host, port, malware):
    print('MyHoneyPot has started...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(128)
    while True:
        csock, address = s.accept()
        print (f'Connection from: {address[0]}, {port}')
        writeLog(address, port)
        if malware == 'm':
            subject = "MyHoneyPot >> ALERT"
            msg = f"There was an unauthorized attempt from {address}"
            sendEmail(subject, msg)
        csock.close()

if __name__=='__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    malware = sys.argv[3]
    main(host, port, malware)
exit(1)
