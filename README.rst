======================
Python Video Thumbnail
======================


.. image:: https://img.shields.io/pypi/v/python_video_thumbnail.svg
        :target: https://pypi.python.org/pypi/python_video_thumbnail

.. image:: https://img.shields.io/travis/mikolajkosmal/python_video_thumbnail.svg
        :target: https://travis-ci.com/mikolajkosmal/python_video_thumbnail


Python package for capturing frames from video.
Written as replacement of https://github.com/radek-senfeld/ffvideo package,
and to help with transition of Python 2.7 projects that relay on FFVideo, to Python 3.


Features
--------
* Supports file paths and urls
* Supports image resizing

Usage ::

        from python_video_thumbnail import VideoFrames

        vf = VideoFrames(
                source="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
                frame_numbers=[6000],
                img_options={"width": 128},
                format=".png"
        )

        captured_frames = vf.capture()

        with open("captured_frame.png", "wb") as f:
                f.write(captured_frames[0].getvalue())



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
