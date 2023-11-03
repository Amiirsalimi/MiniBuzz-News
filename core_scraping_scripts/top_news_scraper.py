import feedparser
import json
# https://edition.cnn.com/services/rss/
# Parse the RSS feed
feed = feedparser.parse('http://feeds.feedburner.com/com/Yeor')

# Convert the parsed RSS feed to JSON
json_feed = json.dumps(feed, ensure_ascii=False)

# Print the JSON
print(json_feed)
# Open a file in write mode
with open('data.json', 'w') as json_file:
    # Write the JSON data to the file
    json.dump(feed, json_file, ensure_ascii=False, indent=4)