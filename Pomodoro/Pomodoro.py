from datetime import datetime
from time import sleep
from playsound import playsound

ms = int(datetime.now().strftime('%X')[0:2])

if 22 > ms >= 7:

    while True:
        agora = datetime.now().strftime('%X')
        agoraint = int(agora[3:5])
        if int(agora[3:5]) >= 50:
            print(f'Break time! ({agora})')
            sleep(3000 - agoraint * 60)
            playsound('zells1.wav')
        else:
            print(f'Work time! ({agora})')
            sleep(3600 - agoraint * 60)
            playsound('zells1.wav')

else:
    print("Sleep time... zzz")
    playsound('power-down.wav')
