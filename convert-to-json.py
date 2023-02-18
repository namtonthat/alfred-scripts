import json
import clipboard
import yaml

last_item = clipboard.paste()

dict_last_item = json.loads(json.loads(last_item))

yaml_last_item = yaml.dump(dict_last_item, Dumper=yaml.SafeDumper)

clipboard.copy(yaml_last_item)