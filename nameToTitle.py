import os, subprocess, re, json, random

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith('mp3'):
        newName = ''
        try:
            dic = json.loads(subprocess.Popen([f"ffprobe -show_entries format_tags=title,artist -i {repr(file)} -of csv='p=0' -v quiet -print_format json"], shell=True, stdout=subprocess.PIPE).communicate()[0])['format']['tags']

            if len(dic) == 2:
                title, artist = dic['title'], dic['artist']
                newName = f'{title.strip()} - {artist.strip()}'
            else:
                newName = file[:-4]
        except:
            newName = file[:-4]

        os.rename(file, newName.replace('/', '')+'.mp3')
# k = [f'/home/proxima/Music/{name}' for name in os.listdir(os.getcwd()) if name.endswith('mp3')]
# random.shuffle(k)
# print('\n'.join(k))