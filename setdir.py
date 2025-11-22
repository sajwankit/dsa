import json5
import json
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python setup_folder.py <category>")
    sys.exit(1)

category = sys.argv[1]

settings_path = os.path.expanduser('~/Library/Application Support/Code/User/settings.json')
with open(settings_path, 'r') as f:
    settings = json5.load(f)

settings['labuladong-leetcode.workspaceFolder'] = f"/Users/ankitsajwan/tech/dsa/{category}/problems"

with open(settings_path, 'w', encoding='utf-8') as f:
    json.dump(settings, f, indent=4, ensure_ascii=False)

print(f"Updated workspaceFolder to /Users/ankitsajwan/tech/dsa/{category}/problems in settings.json")