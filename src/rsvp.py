from typing import List, Tuple


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Return a new list with duplicate emails removed, preserving first seen.

    Treat emails case-insensitively ("ALICE@x.com" == "alice@x.com").
    Keep the first form you saw.

    Ignore entries that do not contain an '@' character.
    """
    seen = set()
    result = []
    for e in emails:
        if '@' not in e:
            continue
        key = e.lower()
        if key not in seen:
            seen.add(key)
            result.append(e)
    return result


def first_with_domain(emails: List[str], domain: str) -> int | None:
    """Return the index of the first email whose domain matches `domain`.

    Comparison is case-insensitive.
    """
    target = domain.lower()
    for i, e in enumerate(emails):
        if '@' not in e:
            continue
        _, dom = e.rsplit('@', 1)
        if dom.lower() == target:
            return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Return (domain, count) pairs sorted by domain (A..Z), case-insensitive.

    Skip malformed entries without an '@'.
    """
    counts = {}
    for e in emails:
        if '@' not in e:
            continue
        _, dom = e.rsplit('@', 1)
        key = dom.lower()
        counts[key] = counts.get(key, 0) + 1

    # Sort by domain case-insensitive
    return sorted(counts.items(), key=lambda x: x[0].lower())
