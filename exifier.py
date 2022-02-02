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


def bullshitifier(deg, mint, sec):
    return ((deg, 1), (mint, 1), (sec * 1000000, 1000000))


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
    camera_vendor = None
    camera = None
    directory = None

    def set_directory(self):
        self.directory = input('Enter the directory location: ')

    def exify(self):
        if not self.directory:
            print('SPECIFY THE DIRECTORY NEXT TIME!')
            return
        filenames = os.listdir(self.directory)

        camera_vendor_input = input('Enter the camera vendor name: ')
        if camera_vendor_input != 'no':
            self.camera_vendor = camera_vendor_input

        camera_input = input('Enter the camera name: ')
        if camera_input != 'no':
            self.camera = camera_input

        for filename in filenames:
            with Image.open(self.directory + filename) as pidor_in_question:
                exif_dict = piexif.load(pidor_in_question.info['exif'])

                date_input = input(f'Enter the date of capture. Previous is {self.capture_date}: ')

                if date_input == 'no':
                    date_to_insert = None
                elif date_input == 'pr':
                    date_to_insert = self.capture_date
                else:
                    date_to_insert = date_input
                    self.capture_date = date_to_insert

                time_input = input(f'Enter the time of capture. Previous is {self.capture_time}: ')

                if time_input == 'no':
                    time_to_insert = None
                elif date_input == 'pr':
                    time_to_insert = self.capture_time
                else:
                    time_to_insert = time_input
                    self.capture_time = time_to_insert

                location_input = input(f'Enter the place of capture. Previous is {self.location}: ')

                if location_input == 'no':
                    location_to_insert = None
                elif location_input == 'pr':
                    location_to_insert = self.location
                else:
                    latitude, longitude = location_to_insert.split(',')

                    deg, mint, sec = shit_defiler(latitude)
                    converted_lat = bullshitifier(deg, mint, sec)

                    deg, mint, sec = shit_defiler(longitude)
                    converted_long = bullshitifier(deg, mint, sec)
                    location_to_insert = (converted_lat, converted_long)
                    self.location = location_to_insert


