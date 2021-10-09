#!/usr/bin/env sh

ID=$(xinput list | grep -Po 'Logitech Wireless Receiver Mouse\s+id=\K(\d+)');
xinput set-prop $ID "libinput Scroll Method Enabled" 0, 0, 1;
xinput set-prop $ID "libinput Button Scrolling Button" 2;
echo "xinput set-prop ${ID} 'libinput Scroll Method Enabled' 0, 0, 1\nxinput set-prop ${ID} 'libinput Button Scrolling Button' 2" > ~/.xsessionrc;
