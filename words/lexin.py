import json
import urllib.request

def get_translation(original_word, strict=False):
    if strict:
        operator = "baseformC"
    else:
        operator = "wfC"
    url = f"https://ws.spraakbanken.gu.se/ws/karp/v4/query?q=extended||and|{operator}|equals|" \
          f"{original_word.replace(' ', '%20')}|&resource=lexin"
    url = url.encode('ascii', 'ignore').decode('ascii')

    try:
        raw_json = urllib.request.urlopen(url)
        parsed_json = json.load(raw_json)

        # Loop through the hits in the JSON response
        for hit in parsed_json["hits"]["hits"]:
            # Check if the language is Russian
            if "lang" in hit["_source"]["FormRepresentations"][1] and hit["_source"]["FormRepresentations"][1]["lang"] == "rus":
                # Return the translation to Russian
                return hit["_source"]["FormRepresentations"][1]["baseform"]

        # If translation not found
        return "Translation not found"
        
    except Exception as e:
        print(f"Error fetching translation for term {original_word}: {e}")
        return "Error"
