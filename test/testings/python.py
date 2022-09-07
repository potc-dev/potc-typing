try:
    from typing import TypingMeta
except ImportError:
    is_3_6 = False
else:
    is_3_6 = True

try:
    _ = list[int]
except TypeError:
    is_3_9 = False
else:
    is_3_9 = True
