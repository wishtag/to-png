import os
from pathlib import Path

inputDir = os.listdir("img")
for i in range(0, len(inputDir)):
    p = Path(f"img/{inputDir[i]}")
    p.rename(p.with_suffix(".png"))