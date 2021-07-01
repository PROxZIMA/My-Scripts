# My Scripts :)

These are some random scripts which I made and use (almost) daily.<br>Some of them work only on linux though.

### animeRelease.py
Check your watch status of airing anime. Only if you are registered on (Anilist)[https://anilist.co/]. Change `PROxZIMA` in `userName` to your default name so usage command won't require an extra argument everytime you run.

Usage: `python animeRelease.py [userName]`

### enableAutoscrolling.py
Enables autoscrolling by clicking mouse middle button. Works only on linux. Set it as startup script so you won't need to run it everytime you plugin a receiver.

Usage: `python enableAutoscrolling.py`

### nameToTitle.py
Replaces a mp3 file name using the file's inbuilt meta-tags. Requires `ffprobe`. Just run this in the folder having the mp3 files. I made this while making my playlist.

Usage: `python nameToTitle.py`

### pdfCrop.py
Crops a pdf according to given percentages. Won't reduce file size. Works only on linux as it's a commandline tool.

Usage: `python pdfCrop.py infile left% bottom% right% top% outfile`

### pdfShrink.sh
A simple shell script to reduce pdf size using ghostscript.

Usage: `pdfShrink infile [outfile] [resolution_in_dpi]`

### timestampSplit.py
Cuts a long mp3 file based on the timeStamp provided. Requires `ffmpeg`.

Usage: `python timestampSplit.py song.mp3`

### torrentDownload.py
Simple downloader for magnet links. Results in some damm high CPU usage. So better use this script on Google Colab.

Usage: `python torrentDownload.py [Download Path]`
