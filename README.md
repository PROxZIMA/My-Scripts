# My Scripts :)

These are some random scripts which I made and use (almost) daily.<br>Some of them work only on linux though.

### `animeRelease.py`
Check your watch status of airing anime. Only if you are registered on [Anilist](https://anilist.co/). 

Usage: `python animeRelease.py [userName]`

### `codium-features.sh`
A simple sed command to use Microsoft marketplace extensions in VSCodium.

Usage: `codium-features.sh`

### `enable_autoscrolling.sh`
Enables autoscrolling by clicking mouse middle button. Works only on linux. Set it as startup script so you won't need to run it everytime you plugin a receiver.

Usage: `enable_autoscrolling.sh`

### `gitDownload.sh`
Simple GitHub folder downloader using SVN.

Usage: `gitDownload.sh [FolderLink]`

### `nameToTitle.py`
Replaces a mp3 file name using the file's inbuilt meta-tags. Requires `ffprobe`. Just run this in the folder having the mp3 files. I made this while making my playlist.

Usage: `python nameToTitle.py`

### `pamic`
Using `pamic` or `pulse audio mic` you can use your android MIC in PC/Laptop. Install [lanmic](https://play.google.com/store/apps/details?id=com.portable.lanmic) and start the server. Use the address as argument in the command line. Requires `ffmpeg` and `pavucontrol`

Usage: `pamic [start [Mic address with port]|stop]`

### `pashare`
`pashare` or `pulse audio share` is a simple but awesome script I found [here](https://superuser.com/a/750324). It basically streams Linux audio output over WI-FI. Then connect to port `8000` on other device to listen to the audio

Usage: `pashare [start|stop]`

### `pdfCrop.py`
Crops a pdf according to given percentages. Won't reduce file size. Works only on linux as it's a commandline tool.

Usage: `python pdfCrop.py infile left% bottom% right% top% outfile`

### `pdfShrink.sh`
A simple shell script to reduce pdf size using ghostscript.

Usage: `pdfShrink infile [outfile] [resolution_in_dpi]`

### `timestampSplit.py`
Cuts a long mp3 file based on the timeStamp provided. Requires `ffmpeg`.

Usage: `python timestampSplit.py song.mp3`

### `torrentDownload.py`
Simple downloader for magnet links. Results in some damm high CPU usage. So better use this script on Google Colab.

Usage: `python torrentDownload.py [Download Path]`
