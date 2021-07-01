import libtorrent as lt
import time
import sys

ses = lt.session()
ses.listen_on(6881, 6891)
#ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})
downloads = []

params = {'save_path': (sys.argv + ['/home/proxzima/Downloads'])[1]}

while True:
    magnet_link = input('Enter Magnet Link Or Type Exit: ')
    if magnet_link.lower() == 'exit':
        break
    downloads.append(lt.add_magnet_uri(ses, magnet_link, params))


for _, download in enumerate(downloads):
    print('Starting :', download.name())
    while (not download.is_seed()):
        s = download.status()

        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, s.state), end=' ')
        sys.stdout.flush()

    else:
        print('Completed :', download.name())


#magnet:?xt=urn:btih:D2B1F83B8C8CC776EA5FF77D32739E15673350D2&dn=Big+collection+of+m3u+files+1-2-2020+%5Btested+%26ndash%3B+working%5D+%5B4allapps%5D&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce

#magnet:?xt=urn:btih:AACE50568D236922D532C736931B84C746E7E6F4&dn=Big+collection+of+m3u+files+30-1-2020+%5Btested+%26ndash%3B+working%5D+%5B4allapps%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2790%2Fannounce&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.vanitycore.co%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce
