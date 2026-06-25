"""
Run this from your GitHub repo root:
  python download-fonts.py

Downloads the exact fonts used by focus.html and names them to match fonts.css
Works on Windows, Mac, and Linux — no pip installs needed.
"""
import urllib.request, re, os

os.makedirs("fonts", exist_ok=True)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120"
CSS_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400"
    "&family=DM+Sans:wght@300;400"
    "&display=swap"
)

req = urllib.request.Request(CSS_URL, headers={"User-Agent": UA})
css = urllib.request.urlopen(req).read().decode()

# Parse each @font-face block to get family, style, weight, and url together
blocks = re.findall(
    r"@font-face\s*\{([^}]+)\}",
    css, re.DOTALL
)

def extract(block, prop):
    m = re.search(prop + r"\s*:\s*([^;]+);", block)
    return m.group(1).strip() if m else ""

downloaded = []
for block in blocks:
    family  = extract(block, "font-family").strip("'\"").lower().replace(" ", "-")
    style   = extract(block, "font-style")    # normal / italic
    weight  = extract(block, "font-weight")   # 300 / 400 / 500
    url_m   = re.search(r"url\((https://fonts\.gstatic\.com/[^)]+\.woff2)\)", block)
    if not url_m:
        continue
    url = url_m.group(1)

    suffix = weight + ("italic" if style == "italic" else "")
    filename = f"fonts/{family}-{suffix}.woff2"

    if filename in downloaded:
        continue  # skip duplicates (Google sometimes repeats for unicode subsets)

    print(f"Downloading: {filename}")
    r = urllib.request.Request(url, headers={"User-Agent": UA})
    data = urllib.request.urlopen(r).read()
    with open(filename, "wb") as f:
        f.write(data)
    print(f"  ✓ {len(data)//1024} KB")
    downloaded.append(filename)

print(f"\nAll done! Downloaded {len(downloaded)} font files to ./fonts/")
print("Files created:")
for f in downloaded:
    print(f"  {f}")