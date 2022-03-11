from pathlib import Path
from PIL import Image
import argparse


def png2ico(pngs, ico):
    data = bytes((0, 0, 1, 0, len(pngs), 0))
    offset = 6 + len(pngs) * 16

    for png in pngs:
        img = Image.open(png)
        data += bytes((img.width, img.height, 0, 0, 1, 0, 32, 0, ))
        bytesize = Path(png).stat().st_size
        data += bytesize.to_bytes(4, byteorder="little")
        data += offset.to_bytes(4, byteorder="little")
        offset += bytesize

    for png in pngs:
        data += Path(png).read_bytes()

    Path(ico).write_bytes(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converting multiple .PNG files to one multisize .ICO file')
    parser.add_argument('files', nargs='+', type=str, help='Input .PNG files')
    parser.add_argument('-o', '--output', default='icon.ico', type=str, help='Output .ICO file')
    args = parser.parse_args()
    png2ico(args.files, args.output)