import sys
import re

lines = sys.stdin.readlines()
pattern = re.compile("^[\w \-,]+$")
for line in lines:
    line = line.strip()
    ok = pattern.match(line)
    l = len(line)
    if not ok:
        continue
    if l < 15:
        continue
    if l > 36:
        continue
    line = line.upper()
    print(line)
