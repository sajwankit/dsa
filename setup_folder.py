import json5
import os

settings_path = os.path.expanduser('~/Library/Application Support/Code/User/settings.json')
with open(settings_path, 'r') as f:
    settings = json5.load(f)

category = "sliding_window"  # Change this to your desired category

settings['labuladong-leetcode.workspaceFolder'] = f"/Users/ankitsajwan/tech/dsa/{category}/problems"

with open(settings_path, 'w') as f:
    f.write(json5.dumps(settings, indent=4))

print(f"Updated workspaceFolder to /Users/ankitsajwan/tech/dsa/{category}/problems in settings.json")