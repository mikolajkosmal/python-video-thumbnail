#!/usr/bin/env python

"""Tests for `python_video_thumbnail` package."""

from python_video_thumbnail import VideoFrames

BIG_BUCK_BUNNY_URL = (
    "http://commondatastorage.googleapis.com/"
    "gtv-videos-bucket/sample/BigBuckBunny.mp4"
)


def test_video_frame_capture():
    vf = VideoFrames(BIG_BUCK_BUNNY_URL, 6000)
    frame = vf.capture()[0]
    with open("tests/data_fixtures/6000_frame_orginal.jpg", "rb") as f:
        assert frame.getvalue() == f.read()


def test_video_frame_capture_with_resize():
    vf = VideoFrames(BIG_BUCK_BUNNY_URL, 6000, {"width": 128})
    frame = vf.capture()[0]
    with open("tests/data_fixtures/6000_frame_width_128.jpg", "rb") as f:
        assert frame.getvalue() == f.read()


def test_video_frame_capture_in_png():
    vf = VideoFrames(BIG_BUCK_BUNNY_URL, 6000, {"width": 128}, format=".png")
    frame = vf.capture()[0]
    with open("tests/data_fixtures/6000_frame_width_128.png", "rb") as f:
        assert frame.getvalue() == f.read()


def test_video_frame_capture_in_bmp():
    vf = VideoFrames(BIG_BUCK_BUNNY_URL, 6000, {"width": 128}, format=".bmp")
    frame = vf.capture()[0]
    with open("tests/data_fixtures/6000_frame_width_128.bmp", "rb") as f:
        assert frame.getvalue() == f.read()
