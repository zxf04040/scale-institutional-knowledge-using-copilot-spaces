#!/usr/bin/env python3
"""Update the issue template dropdown options from files in `docs/`.

This script finds files in `docs/` that match `*.md` and updates the
`.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml` dropdown
options for `process_doc` so maintainers don't have to edit the template by hand.
"""
from pathlib import Path
import sys

try:
    import yaml
except Exception:
    print("PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


TEMPLATE = Path('.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml')
DOCS_DIR = Path('docs')

if not TEMPLATE.exists():
    print(f"Template not found: {TEMPLATE}")
    sys.exit(1)

docs = sorted([p.name for p in DOCS_DIR.glob('*.md') if p.name != 'index.md'])
options = docs + ['<new document>']

data = yaml.safe_load(TEMPLATE.read_text())

body = data.get('body', [])
updated = False
for entry in body:
    if entry.get('type') == 'dropdown' and entry.get('id') == 'process_doc':
        entry_attrs = entry.setdefault('attributes', {})
        entry_attrs['options'] = options
        updated = True
        break

if not updated:
    print('Dropdown `process_doc` not found in template body', file=sys.stderr)
    sys.exit(1)

TEMPLATE.write_text(yaml.safe_dump(data, sort_keys=False))
print(f'Updated {TEMPLATE} with {len(options)} options')
