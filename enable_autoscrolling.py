import subprocess, re, os

output = subprocess.run(['xinput', 'list'], stdout=subprocess.PIPE).stdout.decode('utf-8')

mouse_id = re.findall(r'Compx 2\.4G Receiver\s+id=(\d+)', output)[0]

cmd = f'xinput set-prop {mouse_id} "libinput Scroll Method Enabled" 0, 0, 1\nxinput set-prop {mouse_id} "libinput Button Scrolling Button" 2'

with open('/home/proxzima/.xsessionrc', 'w') as f:
    f.write(cmd)

os.system(cmd)
