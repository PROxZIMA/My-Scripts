import subprocess, sys

timeStamp = '''name of song1 00:00:00
​name of song2 00:50:00
​name of song2 01:00:00
01:50:00'''.split('\n') # last line indicates ending time.

song = sys.argv[1]

def toSec(t):
    t = t.split(':')[::-1]
    sec = 0
    for i in range(len(t)):
        sec += int(t[i].replace('\u200b', '')) * (60 ** i)
    return sec

for i in range(len(timeStamp) - 1):
    name, t1 = timeStamp[i].rsplit(' ', 1)
    t2 = timeStamp[i + 1].rsplit(' ', 1)[-1]
    t1, t2 = map(toSec, (t1, t2))
    # print('/home/proxima/Music/' + name)

    output = subprocess.run(['ffmpeg', '-i', song, '-ss', str(t1), '-to', str(t2), '-metadata', f'title={name}', '-c', 'copy', f'{name}.mp3'], stdout=subprocess.PIPE)
