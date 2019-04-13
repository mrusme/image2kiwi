image2kiwi
----------

Converter from Images (JPEG, PNG, GIF, ...) into [Kiwi](https://mrusme.github.io/kiwi) `frames` JSON-arrays.

## Installation

```sh
$ # Optional
$ mkvirtualenv -p python3 image2kiwi
$ # Install Pillow
$ pip3 install pillow
```

## Usage

```sh
$ python3 ./image2kiwi <imagefile> ...
```

E.g.

```sh
$ python3 ./image2kiwi ~/Desktop/rainbow.gif
```

Output:

```json
[{"keys": {"key_1_in_row_1": {"red": 70, "green": 81, "blue": 184}, "key_1_in_row_2": {"red": 116, "green": 204, "blue": 138}, "key_1_in_row_3": {"red": 82, "green": 185, "blue": 173}, "key_2_in_row_1": {"red": 49, "green": 117, "blue": 205}, "key_2_in_row_2": {"red": 127, "green": 128, "blue": 127}, "key_2_in_row_3": {"red": 205, "green": 136, "blue": 49}, "key_3_in_row_1": {"red": 172, "green": 69, "blue": 82}, "key_3_in_row_2": {"red": 136, "green": 49, "blue": 118}, "key_3_in_row_3": {"red": 185, "green": 172, "blue": 69}}, "sleep": 250}, {"keys": {"key_1_in_row_1": {"red": 82, "green": 185, "blue": 173}, "key_1_in_row_2": {"red": 205, "green": 137, "blue": 49}, "key_1_in_row_3": {"red": 185, "green": 172, "blue": 69}, "key_2_in_row_1": {"red": 117, "green": 204, "blue": 137}, "key_2_in_row_2": {"red": 127, "green": 128, "blue": 127}, "key_2_in_row_3": {"red": 136, "green": 49, "blue": 119}, "key_3_in_row_1": {"red": 70, "green": 81, "blue": 184}, "key_3_in_row_2": {"red": 49, "green": 117, "blue": 205}, "key_3_in_row_3": {"red": 172, "green": 70, "blue": 82}}, "sleep": 250}, {"keys": {"key_1_in_row_1": {"red": 185, "green": 172, "blue": 69}, "key_1_in_row_2": {"red": 136, "green": 49, "blue": 118}, "key_1_in_row_3": {"red": 172, "green": 69, "blue": 82}, "key_2_in_row_1": {"red": 205, "green": 136, "blue": 49}, "key_2_in_row_2": {"red": 127, "green": 128, "blue": 127}, "key_2_in_row_3": {"red": 50, "green": 117, "blue": 205}, "key_3_in_row_1": {"red": 82, "green": 185, "blue": 173}, "key_3_in_row_2": {"red": 116, "green": 204, "blue": 138}, "key_3_in_row_3": {"red": 70, "green": 81, "blue": 184}}, "sleep": 250}, {"keys": {"key_1_in_row_1": {"red": 172, "green": 69, "blue": 82}, "key_1_in_row_2": {"red": 49, "green": 117, "blue": 205}, "key_1_in_row_3": {"red": 70, "green": 81, "blue": 184}, "key_2_in_row_1": {"red": 136, "green": 49, "blue": 119}, "key_2_in_row_2": {"red": 127, "green": 128, "blue": 127}, "key_2_in_row_3": {"red": 117, "green": 204, "blue": 137}, "key_3_in_row_1": {"red": 185, "green": 172, "blue": 69}, "key_3_in_row_2": {"red": 205, "green": 136, "blue": 49}, "key_3_in_row_3": {"red": 82, "green": 185, "blue": 172}}, "sleep": 250}]
```

This output can be used to set Kiwi key animations. Please refer to the [Kiwi documentation](https://mrusme.github.io/kiwi) for more info.

### Multiple images

If you don't have a GIF but still want an animation, you can simply select mulitple images and have image2kiwi generate you an animation from them:

```sh
$ python3 ./image2kiwi ~/Desktop/image1.jpg ~/Desktop/image2.jpg ~/Desktop/image3.jpg
```

### Customize animation speed

You can use the parameter `--show-frame-for-ms <number>` to customize the animation playback speed. `--show-frame-for-ms` takes one argument which is the number of milliseconds each frame should be visible for. `--show-frame-for-ms 1000` would make each frame be visible for 1 full second for example. You can use the flag like this:

```sh
$ python3 ./image2kiwi --show-frame-for-ms 1000 ~/Desktop/image1.jpg ~/Desktop/image2.jpg ~/Desktop/image3.jpg
```

## Notice

- image2kiwi converts GIFs into multiple frames, meaning that you'd end up with a constantly moving Kiwi animation!
- image2kiwi converts RGBA into RGB - you can use transparent PNGs, but obviously the transparent parts won't make your keys transparent :-)
- image2kiwi scales images down to a maximum of 3x4px while keeping their aspect ratio. This means: If you supply a 300x300px image, you will end up with a 3x3px animation. In that case the bottom keys row won't be triggered by the animation at all. You need to supply an image that's 3x4px or has an aspect ratio of 3:4.

## "Let me tell you..."

Sure, [tell me](https://twitter.com/intent/tweet?text=@mrusme%20regarding%20image2kiwi,%20let%20me%20tell%20you%20that...)!
