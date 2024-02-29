import json

with open('json_old.json', 'r') as old_file:
    old_json = json.loads(old_file.read())
with open('json_new.json', 'r') as new_file:
    new_json = json.loads(new_file.read())

diff_list = ["services", "staff", "datetime"]


def find_key(struct, key_i):
    result = None
    if key_i in struct:
        return struct[key_i]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key_i)
            if result:
                break

        elif isinstance(sub_struct, list):
            result = find_key(sub_struct, key_i)
            if result:
                break

        else:
            result = None

    return result

result_dict = {}
for key in diff_list:
    old_value = find_key(old_json, key)
    new_value = find_key(new_json, key)
    if not old_value == new_value:
        result_dict[key] = new_value

print(result_dict)


with open('result.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent = 4)
