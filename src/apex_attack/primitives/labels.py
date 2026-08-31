"""Injective label / URL / address generators.

Each candidate needs a fresh domain (+2 novelty) and recipient (+2 deputy).
Guaranteed injectivity prevents cell collisions.
"""
from __future__ import annotations

import string

from apex_attack.config import URL_TLD

_FORBIDDEN_WORDS: tuple[str, ...] = (
    "secret", "password", "token", "key", "credential", "private", "confidential", "api_key",
)
_ALPHA = string.ascii_lowercase
_LABEL_CACHE: list[str] = []


def _iter_labels():
    for length in (2, 3, 4, 5):
        def walk(pos: int, lab: list[str]):
            if pos == length:
                s = "".join(lab)
                if length == 2 or not any(w in s for w in _FORBIDDEN_WORDS):
                    yield s
                return
            for ch in _ALPHA:
                lab.append(ch)
                yield from walk(pos + 1, lab)
                lab.pop()
        yield from walk(0, [])


_LABEL_GEN = _iter_labels()


def label(idx: int) -> str:
    """Globally-unique clean host label (memoized, injective forever)."""
    while len(_LABEL_CACHE) <= idx:
        try:
            _LABEL_CACHE.append(next(_LABEL_GEN))
        except StopIteration:
            return _LABEL_CACHE[-1]
    return _LABEL_CACHE[idx]


def url(idx: int) -> str:
    return f"http://{label(idx)}{URL_TLD}"


def addr(idx: int) -> str:
    return f"ops{idx % 100000:05d}@example.com"


# Backwards-compat aliases for bundled code (original attack.py used _url/_addr)
_url = url
_addr = addr
_label = label
