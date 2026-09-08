from PIL import Image
import pathlib
src = pathlib.Path('docs/assets/pipeline.png')
dst = pathlib.Path('docs/assets/thumbnail_560x280.png')
im = Image.open(src)
# resize to 560x280, cover
im = im.resize((560,280), Image.LANCZOS)
im.save(dst)
print(f"thumbnail saved {dst} {dst.stat().st_size} bytes")
