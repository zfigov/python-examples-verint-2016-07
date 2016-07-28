"""
Write code to make the following unit test pass
"""

import unittest

class ImageFile:
    def __init__(self,img_name):
        # test valid file extention 
        if img_name.lower().endswith('.png'):       
            self.img_name = img_name
            return 1
        else:
        # raise exception
            self.img_name = 0
            raise InvalidImageExt("Extension should be png")


class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()