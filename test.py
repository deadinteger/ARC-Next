from youtube_search import YoutubeSearch
import pprint
import json

results = YoutubeSearch("Darkness Within", max_results=1).to_json()
y = json.loads(results)
pp = pprint.PrettyPrinter()
pp.pprint(f'{y["videos"]}')
