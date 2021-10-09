import libtorrent as lt
import time
import sys

ses = lt.session()
ses.listen_on(6881, 6891)
#ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})
downloads = []

path = sys.argv[1]
params = {'save_path': path or '/home/proxzima/Downloads'}

while True:
    magnet_link = input('Enter Magnet Link Or Type Exit: ')
    if magnet_link.lower() == 'exit':
        break
    downloads.append(lt.add_magnet_uri(ses, magnet_link, params))

#info = lt.torrent_info(sys.argv[1])
#h = ses.add_torrent({'ti': info, 'save_path': '.'})
#s = h.status()
#print('starting', s.name)

#while (not s.is_seeding):
#    s = h.status()

#    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
#        s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
#        s.num_peers, s.state), end=' ')

#    alerts = ses.pop_alerts()
#    for a in alerts:
#        if a.category() & lt.alert.category_t.error_notification:
#            print(a)

#    sys.stdout.flush()

#    time.sleep(1)

#print(h.status().name, 'complete')

for _, download in enumerate(downloads):
    #bar = download_bars[index + next_shift]
    print('Starting :', download.name())
    #if not download.is_seed():
    while (not download.is_seed()):
        s = download.status()

        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, s.state), end=' ')
        sys.stdout.flush()

    else:
        #ses.remove_torrent(download)
        #downloads.remove(download)
        print('Completed :', download.name())


#magnet:?xt=urn:btih:D2B1F83B8C8CC776EA5FF77D32739E15673350D2&dn=Big+collection+of+m3u+files+1-2-2020+%5Btested+%26ndash%3B+working%5D+%5B4allapps%5D&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce

#magnet:?xt=urn:btih:AACE50568D236922D532C736931B84C746E7E6F4&dn=Big+collection+of+m3u+files+30-1-2020+%5Btested+%26ndash%3B+working%5D+%5B4allapps%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2790%2Fannounce&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.vanitycore.co%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce
