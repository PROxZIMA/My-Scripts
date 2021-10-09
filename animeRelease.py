from datetime import timedelta as td
import ast, requests, sys

userName = (sys.argv + ['PROxZIMA'])[1]

query = 'query ($username: String) { MediaListCollection(userName: $username, type: ANIME, status: CURRENT) { lists { entries { media { status nextAiringEpisode { episode timeUntilAiring } title { english } episodes } progress } } } }'

try:
    data = [i for i in ast.literal_eval(str(requests.post('https://graphql.anilist.co', json={'query': query, 'variables': {'username':userName}}).json()).replace('None', '0'))['data']['MediaListCollection']['lists'][0]['entries'] if i['media']['status'] == 'RELEASING']
except requests.exceptions.ConnectionError:
    print('Internet unavailable')
    exit()
except TypeError:
    print('Username not found')
    exit()

print('Anime                 On  Next Release')
for i in data:
    print(f"{str(i['media']['title']['english'])[:21]:<22}{i['progress']:<4}{i['media']['nextAiringEpisode']['episode']: >3}/{i['media']['episodes']:<4}{str(td(seconds=i['media']['nextAiringEpisode']['timeUntilAiring']))[:-3]}")
