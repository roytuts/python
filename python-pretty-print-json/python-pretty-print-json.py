import json

#jsn = '{"one":"AAA","two":["BBB","CCC"],"three":{"four":"DDD","five":["EEE","FFF"]}}'
jsn = "{\"one\":\"AAA\",\"two\":[\"BBB\",\"CCC\"],\"three\":{\"four\":\"DDD\",\"five\":[\"EEE\",\"FFF\"]}}"

parsed_json = json.loads(jsn)
prettify_json = json.dumps(parsed_json, indent=4)
#prettify_json = json.dumps(parsed_json, indent=4, sort_keys=True)

print(prettify_json)


with open('input.json', 'r') as inf:
    parsed_json = json.load(inf)
    prettify_json = json.dumps(parsed_json, indent=4)
    
    with open('output.json', 'w') as ouf:
        ouf.write(prettify_json)
