#!/usr/bin/env python3
# coding=utf8

import os
import sys
import json
import math
from PIL import Image
from PIL import GifImagePlugin

class I2K:
    def __init__(self, argv):
        self._argv = argv
        self._show_frame_for_ms = 250

    def get_key_name_from_xy(self, x, y):
        keys = [
            ["key_1_in_row_1", "key_2_in_row_1", "key_3_in_row_1"],
            ["key_1_in_row_2", "key_2_in_row_2", "key_3_in_row_2"],
            ["key_1_in_row_3", "key_2_in_row_3", "key_3_in_row_3"],
            ["key_1_in_row_4", "key_2_in_row_4", "key_3_in_row_4"],
        ]
        return keys[y][x]

    def convert(self):
        frames = []

        arg_idx = 1
        while arg_idx < len(self._argv):
            if self._argv[arg_idx] == "--show-frame-for-ms":
                self._show_frame_for_ms = int(self._argv[(arg_idx+1)])
                arg_idx = arg_idx + 2
            elif self._argv[arg_idx] == "--split-horizontally":
                image_to_split = self._argv[(arg_idx+1)]
                frames.extend(self.split_convert_image(image_to_split, direction="horizontal"))
                arg_idx = arg_idx + 2
            elif self._argv[arg_idx] == "--split-vertically":
                image_to_split = self._argv[(arg_idx+1)]
                frames.extend(self.split_convert_image(image_to_split, direction="vertical"))
                arg_idx = arg_idx + 2
            else:
                frames.extend(self.convert_image(self._argv[arg_idx]))
                arg_idx = arg_idx + 1
        return frames

    def split_convert_image(self, image_path, direction="horizontal"):
        image_object = Image.open(image_path)
        frames = []

        image_width, image_height = image_object.size

        crop_width = 3
        crop_height = 4

        if direction == "horizontal":
            if image_height > 4:
                image_object.thumbnail((9999, 4), Image.ANTIALIAS)
        elif direction == "vertical":
            if image_width > 3:
                image_object.thumbnail((3, 9999), Image.ANTIALIAS)

        image_width, image_height = image_object.size

        for crop_location in range(0, (math.floor(image_width / 3) if direction == "horizontal" else math.floor(image_height / 4))):
            x = ((crop_location * 3) if direction == "horizontal" else 0)
            y = ((crop_location * 4) if direction == "vertical" else 0)
            area = (
                x,
                y,
                (x + 3),
                (y + 4)
            )
            cropped_image_object = image_object.crop(area)
            frame = self.convert_image_frame(cropped_image_object.convert('RGB'))
            frames.append(frame)

        return frames

    def convert_image(self, image_path):
        image_object = Image.open(image_path)
        frames = []

        if image_object.format == "GIF" and image_object.is_animated == True and image_object.n_frames > 1:
            for frame in range(0, image_object.n_frames):
                image_object.seek(frame)
                frames.append(self.convert_image_frame(image_object.convert('RGB')))
        else:
            frames.append(self.convert_image_frame(image_object.convert('RGB')))

        return frames

    def convert_image_frame(self, frame_object):
        frame = frame_object
        frame_width, frame_height = frame.size
        if frame_width > 3 or frame_height > 4:
            frame = frame_object.copy()
            frame.thumbnail((3, 4), Image.ANTIALIAS)
            frame_width, frame_height = frame.size

        pixels = frame.load()
        return self.build_frame_map(pixels, frame_width, frame_height)

    def build_frame_map(self, pixels, width, height):
        keys = {}

        for x in range(0, width):
            for y in range(0, height):
                key_name = self.get_key_name_from_xy(x, y)
                red, green, blue = pixels[x, y]
                keys[key_name] = self.build_frame_key_map(red, green, blue)

        return {
            "keys": keys,
            "sleep": self._show_frame_for_ms,
        }

    def build_frame_key_map(self, red, green, blue):
        return {
            "red": red,
            "green": green,
            "blue": blue,
        }

i2k = I2K(sys.argv)
frames = i2k.convert()
print(json.dumps(frames))
