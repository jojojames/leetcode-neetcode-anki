# leetcode-neetcode-anki
[Anki](https://apps.ankiweb.net/) flashcards for the whole set of [LeetCode](https://leetcode.com/) problems + [NeetCode150](https://neetcode.io/) as a subdeck. NeetCode topic subdecks have numbered prefixes so new questions follow an order that respects the roadmap prerequisites. The package retains its original scheduling information; it does not contain the maintainer's personal study history.

## Card structure
Front                            |Hint                           |Back
:-------------------------------:|:-----------------------------:|:-----------------------------:
![Card front](img/card-front.png)|![Card hint](img/card-hint.png)|![Card back](img/card-back.png)

Each card contains the following fields:
* title
* id
* slug
* difficulty
* topics
* paid

which is only a subset of what <sup>[[1]](#1)</sup> scrapes.

## Deck structure
Study **LeetCode::NeetCode150** to include all topic subdecks. They are
numbered as follows:

```text
LeetCode
└── NeetCode150
    ├── 01 Arrays & Hashing
    ├── 02 Two Pointers
    ├── 03 Stack
    ├── 04 Binary Search
    ├── 05 Sliding Window
    ├── 06 Linked List
    ├── 07 Trees
    ├── 08 Tries
    ├── 09 Heap / Priority Queue
    ├── 10 Backtracking
    ├── 11 Graphs
    ├── 12 1-D DP
    ├── 13 Intervals
    ├── 14 Greedy
    ├── 15 Advanced Graphs
    ├── 16 2-D DP
    ├── 17 Bit Manipulation
    └── 18 Math & Geometry
```

The roadmap branches, so it does not define a single total order. This
sequence respects its prerequisite arrows. The previous unnumbered names
sorted alphabetically and introduced DP before Arrays & Hashing.

In Anki's deck options for **NeetCode150**, use **New card gather order →
Deck** and **New card sort order → Order gathered**. Reviews continue to
follow Anki's scheduler; the prefixes control introduction of new topics.
See [Anki's display-order documentation](https://docs.ankiweb.net/deck-options.html#display-order).

New imports of `LeetCode.apkg` include these numbered decks. Existing users
should rename their current topic decks to match the list above; doing so
preserves their cards and review history. Reimporting an updated package
is not a substitute for renaming existing decks.

To apply the same ordering to a fresh copy of the original package:

```sh
python3 tools/order_neetcode_decks.py LeetCode.apkg
```

The script changes only the embedded collection's deck names, keeps deck
and card IDs intact, and leaves cards, notes, media, and scheduling data
unchanged. It is safe to run again on an already-numbered package.

## Scheduling
![Scheduling daily](img/scheduling-daily.png)
![Scheduling new](img/scheduling-new.png)
![Scheduling lapses](img/scheduling-lapses.png)

## [NeetCode roadmap](https://neetcode.io/roadmap)
![NeetCode roadmap](img/neetcode-roadmap.png)

## References
<sup><a id="1">[1]</a></sup> The flashcards were generated using https://github.com/fspv/leetcode-anki.
