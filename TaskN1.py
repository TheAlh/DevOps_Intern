import re

ip = input('Enter the IP (Default - 10.1.192.38): ') #Choose the desired IP
if ip == '':
    ip = '10.1.192.38'

sid = []
with open('log.txt', 'r') as inf: #We output a line and if it contains the desired IP, then copy sid from this line to the list
    for line in inf:
        txt = line.strip()
        if ip in txt:
            log = re.findall('sid=/(.*?)/&', txt)
            sid.append(log[0])

output = input('Print to screen (y), otherwise save to log-out.txt: (y/n) ') #We display the received sid on the screen, or in the file log-out.txt
if output == 'y':
    for i in range(len(sid)):
        print(f'{ip} - sid={sid[i]}') #Here you can change the output method and output, for example, only sid. ( ouf.write(f'{sid[i]}\n'))
    input('Press ENTER to exit')
else:
    with open('log-out.txt', 'w') as ouf:
        for i in range(len(sid)):
            ouf.write(f'{ip} - sid={sid[i]}\n') #Here you can change the output method and output, for example, only sid. ( ouf.write(f'{sid[i]}\n') )
