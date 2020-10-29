import json
import sys
for line in sys.stdin:
    fields = json.loads(line.strip())
    #print(fields['text'])
    if "text" in fields:
        print(" ".join([x for x in fields['text'].strip()]))
    elif "content" in fields:
        print(" ".join([x for x in fields['content'].strip()]))
