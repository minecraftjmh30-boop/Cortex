#AI-Generated Function
import json


def try_file(filename):
    path = f"settings/storage/{filename}.json"
    needs_reset = False
    data = None
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if filename == "lights" and "lights" not in data:
                needs_reset = True
            elif filename == "credentials" and "credentials" not in data:
                needs_reset = True
            elif filename == "record_player" and "record_player" not in data:
                needs_reset = True
    except (FileNotFoundError, json.JSONDecodeError):
        needs_reset = True

    if needs_reset:
        with open(path, "w") as f:
            if filename == "lights":
                json.dump({"lights": []}, f)
                data = {"lights": []}
            elif filename == "credentials":
                json.dump({"credentials": {"email": "", "password": ""}}, f)
                data = {"credentials": {"email": "", "password": ""}}
            elif filename == "record_player":
                json.dump({"record_player": []}, f)
                data = {"record_player": []}
            else:
                json.dump({}, f)
                data = {}

    return data
