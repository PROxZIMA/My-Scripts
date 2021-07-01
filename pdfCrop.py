import sys
from subprocess import Popen, PIPE

try:
    _, inp, l, b, r, t, out = sys.argv
except Exception as e:
    print('Usage: python pdfcrop.py infile left% bottom% right% top% outfile\n' +
          '     % indicates cropping precentage from it\'s respective margin')
    exit()

try:
    cmd = f"pdfinfo '{inp}' | grep -Po '(?<=^Page size:      ).*? x .*? '"
    w, h = map(float, Popen(cmd, stdout=PIPE, stderr=None, shell=True).communicate()[0].decode("utf-8").split(' x '))
    print(f'Pdf dimensions: {w} x {h}\n')
except Exception as e:
    exit()

try:
    l, b, r, t = round(float(l)/100*w, 2), round(float(b)/100*h, 2), round(w-float(r)/100*w, 2), round(h-float(t)/100*h, 2)
except Exception as e:
    print('left% bottom% right% top% should be integer/float')
    exit()

cmd = fr"sed 's;\(Crop\|Media\|Bleed\|Trim\|Art\)Box[^]]*;\1Box[{l} {b} {r} {t};g' < '{inp}' > '{out}'"
Popen(cmd, stdout=PIPE, stderr=None, shell=True).communicate()

if not Popen(f"diff '{inp}' '{out}'", stdout=PIPE, stderr=None, shell=True).communicate()[0]:
    print(f'{inp} can\'t be cropped, doing straight copy....\n')

print(f'{out} exported!!!')
