#!/usr/bin/env python3
"""Number NeetCode topic decks in an existing APKG, preserving card data.

Usage: python3 tools/order_neetcode_decks.py [LeetCode.apkg]
Uses only the standard library; never opens an installed Anki profile.
"""
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import zipfile

TOPICS = (
    'Arrays & Hashing', 'Two Pointers', 'Stack', 'Binary Search',
    'Sliding Window', 'Linked List', 'Trees', 'Tries',
    'Heap / Priority Queue', 'Backtracking', 'Graphs', '1-D DP',
    'Intervals', 'Greedy', 'Advanced Graphs', '2-D DP',
    'Bit Manipulation', 'Math & Geometry',
)
ROOT = 'LeetCode::NeetCode150'


def order_package(path):
    """Update only deck names in the package's original SQLite collection."""
    path = Path(path)
    with tempfile.TemporaryDirectory(prefix='neetcode-order-') as directory:
        database = Path(directory) / 'collection.anki21'
        output = Path(directory) / 'ordered.apkg'
        with zipfile.ZipFile(path) as source:
            database.write_bytes(source.read('collection.anki21'))
            with sqlite3.connect(database) as collection:
                decks = json.loads(collection.execute('select decks from col').fetchone()[0])
                names = {deck['name']: deck for deck in decks.values()}
                actual = {name for name in names if name.startswith(ROOT + '::')}
                expected = set()
                for index, topic in enumerate(TOPICS, 1):
                    old = ROOT + '::' + topic
                    new = ROOT + '::' + f'{index:02d} ' + topic
                    matches = [name for name in (old, new) if name in names]
                    if len(matches) != 1:
                        raise ValueError('Expected exactly one deck for ' + topic)
                    expected.add(matches[0])
                    names[matches[0]]['name'] = new
                if actual != expected:
                    raise ValueError('Unexpected NeetCode subdecks; inspect before updating')
                collection.execute('update col set decks=?', (json.dumps(decks),))
                if collection.execute('pragma integrity_check').fetchone()[0] != 'ok':
                    raise ValueError('Collection integrity check failed')
            with zipfile.ZipFile(output, 'w') as target:
                for entry in source.infolist():
                    target.writestr(entry, database.read_bytes() if entry.filename == 'collection.anki21' else source.read(entry.filename))
        # Preserve the repository file's permissions and replace its contents.
        path.write_bytes(output.read_bytes())


if __name__ == '__main__':
    order_package(sys.argv[1] if len(sys.argv) > 1 else 'LeetCode.apkg')
