
from pathlib import Path
from PIL import Image


path = Path(r"img")
converted_path = path / 'ConvertedFiles'
converted_path.mkdir(exist_ok=True)

extensions = [".png", ".jpg", ".jpeg", ".bmp"]

for ext in extensions:
    for file in path.glob("*"+ext):
        img = Image.open(file)
        img = img.convert("RGB")
        new_file = converted_path / file.name
        new_file = new_file.with_suffix('.jpg')
        img.save(new_file, "JPEG", quality=90)
