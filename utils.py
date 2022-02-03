import piexif
from PIL import Image


def shitchecker():
    with Image.open("img2.jpg") as img:
        exif_dict = piexif.load(img.info['exif'])
        for key in piexif.GPSIFD.__dict__.keys():
            eblo = exif_dict['GPS'].get(getattr(piexif.GPSIFD, key))
            if eblo:
                print(f'{key}: {eblo}')
