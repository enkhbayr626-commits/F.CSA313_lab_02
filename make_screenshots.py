from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


RESULTS = [
    ("run-05vu.txt", "k6 5 VU result"),
    ("run-30vu.txt", "k6 30 VU result"),
    ("run-100vu.txt", "k6 100 VU result"),
    ("run-stages.txt", "k6 stages result"),
    ("threshold-pass.txt", "k6 threshold PASS"),
    ("threshold-fail.txt", "k6 threshold FAIL"),
]

FONT_PATH = r"C:\Windows\Fonts\consola.ttf"
FONT = ImageFont.truetype(FONT_PATH, 18)
TITLE_FONT = ImageFont.truetype(FONT_PATH, 22)
BG = "#0c0c0c"
FG = "#eeeeee"
ACCENT = "#55d6be"


def render(source_name: str, title: str) -> None:
    text = Path("results", source_name).read_text(encoding="utf-8", errors="replace")
    text = text.replace("✓", "[PASS]").replace("✗", "[FAIL]").replace("█", "=")
    lines = text.strip().splitlines()
    line_height = 25
    width = 1500
    height = 75 + line_height * len(lines) + 35
    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)
    draw.text((30, 20), title, font=TITLE_FONT, fill=ACCENT)
    y = 65
    for line in lines:
        draw.text((30, y), line, font=FONT, fill=FG)
        y += line_height
    output = Path("screenshots", Path(source_name).stem + ".png")
    output.parent.mkdir(exist_ok=True)
    image.save(output)


for source_name, title in RESULTS:
    render(source_name, title)
