import re

ip = input('Enter the IP/Введите IP (Default - 10.1.192.38): ')
if ip == '':
    ip = '10.1.192.38'

sid = []
with open('log.txt', 'r') as inf:
    for line in inf:
        txt = line.strip()
        if ip in txt:
            log = re.findall('sid=/(.*?)/&', txt)
            sid.append(log[0])

output = input('Вывести на экран (y), иначе сохранить в log-out.txt: (y/n) ')
if output == 'y':
    for i in range(len(sid)):
        print(f'{ip} - sid={sid[i]}')
    input('Press ENTER to exit')
else:
    with open('log-out.txt', 'w') as ouf:
        for i in range(len(sid)):
            ouf.write(f'{ip} - sid={sid[i]}\n')
