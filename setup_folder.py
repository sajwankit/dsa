import json5
import json
import os

settings_path = os.path.expanduser('~/Library/Application Support/Code/User/settings.json')
with open(settings_path, 'r') as f:
    settings = json5.load(f)

category = "dp"  # Change this to your desired category

settings['labuladong-leetcode.workspaceFolder'] = f"/Users/ankitsajwan/tech/dsa/{category}/problems"

with open(settings_path, 'w', encoding='utf-8') as f:
    json.dump(settings, f, indent=4, ensure_ascii=False)

print(f"Updated workspaceFolder to /Users/ankitsajwan/tech/dsa/{category}/problems in settings.json")