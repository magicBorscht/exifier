import piexif
from PIL import Image
import os
import datetime


def shit_defiler(dd):
    is_positive = dd >= 0
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    degrees = degrees if is_positive else -degrees
    return degrees, minutes, seconds


with Image.open("img.jpg") as pidor_in_question:
    exif_dict = piexif.load(pidor_in_question.info['exif'])
    # print(exif_dict)
    lat = exif_dict["GPS"][piexif.GPSIFD.GPSLatitude]
    long = exif_dict["GPS"][piexif.GPSIFD.GPSLongitude]
    print(exif_dict["Exif"].get(piexif.ImageIFD.Model))
    print(lat)
    print(long)
    pringle = lat[0][0] + (lat[1][0] / 60) + ((lat[2][0] / lat[2][1]) / 3600)
    print(pringle)

a = 59.9303732
[d, m, s] = shit_defiler(a)
print(d, m, int(s * 1000000))


class Exifier:
    capture_date = None
    capture_time = None
    location = None
    camera = None
    directory = None

    def exify(self):
        if not self.directory:
            print('SPECIFY THE DIRECTORY NEXT TIME!')
            return
        filenames = os.listdir(self.directory)

        for filename in filenames:
            with Image.open(self.directory + filename) as pidor_in_question:
                exif_dict = piexif.load(pidor_in_question.info['exif'])
