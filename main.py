from pathlib import Path
from PIL import Image

input_dir = Path("img")

for file_path in input_dir.iterdir():
    if file_path.is_file():
        try:
            with Image.open(file_path) as img:
                rgb_img = img.convert("RGB")
                png_path = file_path.with_suffix(".png")
                rgb_img.save(png_path, "PNG")
            file_path.unlink()
            print(f"Converted and replaced: {file_path.name} -> {png_path.name}")
        except Exception as e:
            print(f"Failed to convert {file_path.name}: {e}")