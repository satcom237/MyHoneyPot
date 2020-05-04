import sys
import time
import socket
import smtplib
import config
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

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

def determineMal(source):
    ml_data = [[0, 'Hello how are you'],
            [1, 'Click here to open your new prize'],
            [1, 'Claim your new prize now'],
            [0, 'Please call me when you can'],
            [0, 'Can we meet up today at 3'],
            [1, source]]

    df = pd.DataFrame(np.array(ml_data), columns = ['tag', 'text'])

    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['tag'], random_state = 1)
    count_vector = CountVectorizer()
    training_data = count_vector.fit_transform(X_train)

    testing_data = count_vector.transform(X_test)

    naive_bayes = MultinomialNB()
    naive_bayes.fit(training_data, y_train)

    prediction = naive_bayes.predict(testing_data)
    mal_score = accuracy_score(y_test, prediction)

    print('Prediction: ', prediction)
    print('Accuracy score: ', mal_score)
    return mal_score

def main(host, port, source):
    print('MyHoneyPot has started...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(128)
    while True:
        csock, address = s.accept()
        print (f'Connection from: {address[0]}, {port}')
        writeLog(address, port)
        if determineMal(source) > 0.8:
            print("---MALICIOUS!!!---")
            subject = "MyHoneyPot >> ALERT"
            msg = f"There was an unauthorized attempt from {address}"
            sendEmail(subject, msg)
        csock.close()

if __name__=='__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    source = sys.argv[3]
    main(host, port, source)
exit(1)
