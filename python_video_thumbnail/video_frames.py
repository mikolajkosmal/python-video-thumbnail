import cv2
import io


class VideoCapture(object):
    def __init__(self, source):
        self.source = source
        self.cap = None

    def __enter__(self):
        self.cap = cv2.VideoCapture(self.source)
        if self.cap is None or not self.cap.isOpened():
            self.cap = None
            raise FileNotFoundError(
                "No such file or directory or url: '{}'".format(self.source)
            )
        return self.cap

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cap:
            self.cap.release()
            return True
        return False


class VideoFrames(object):
    """A class that represents video with frame_numbers to capture

    Args:
        source (str): File path or url.
        frame_numbers (list[int]/int): Representing frame number(s) to capture.
        img_options (dict, optional): Image processing options(resizing).
        format (str, optional): OpenCV encode format. Defaults to ".jpeg".
    """

    def __init__(
        self, source, frame_numbers, img_options=None, format=".jpeg"
    ):
        """
        Args:
            source (str): File path or url.
            frame_numbers (list[int]/int): Representing frame number(s) to capture. # noqa
            img_options (dict, optional): Image processing options(resizing).
            format (str, optional): OpenCV encode format. Defaults to ".jpeg".
        """
        self.source = source
        self.frame_numbers = frame_numbers
        self.img_options = img_options
        self.format = format

        if type(self.frame_numbers) == int:
            self.frame_numbers = [self.frame_numbers]

        if not self.img_options:
            self.img_options = {"height": None, "width": None}

    def _resize_frame(self, frame):
        """Resizes frame if `height` or `width` is specified in img_options
          if one of `height` or `width` is specified it will try
          to resize proportionaly

        Args:
            frame (numpy.ndarray): Frame to resize

        Returns:
            numpy.ndarray: Resized frame
        """
        height = self.img_options.get("height", None)
        width = self.img_options.get("width", None)

        frame_height, frame_width = frame.shape[:2]

        if height and not width:
            ratio = height / float(frame_height)
            frame = cv2.resize(
                frame,
                (int(frame_width * ratio), height),
                interpolation=cv2.INTER_AREA,
            )
        elif width and not height:
            ratio = width / float(frame_width)
            frame = cv2.resize(
                frame,
                (width, int(frame_height * ratio)),
                interpolation=cv2.INTER_AREA,
            )
        elif height and width:
            frame = cv2.resize(
                frame,
                (width, height),
                interpolation=cv2.INTER_AREA,
            )

        return frame

    def _process_frame(self, frame):
        """Takes frame and runs it through all processing functions
        Args:
            frame (numpy.ndarray): Frame to process
        Returns:
            numpy.ndarray: Processed frame
        """
        frame = self._resize_frame(frame)
        return frame

    def _capture_frame(self, cap, frame_number):
        """Takes cv2.VideoCapture and captures specified frame
        Args:
            cap (cv2.VideoCapture): cv2.VideoCapture
            frame_number (int): Frame number

        Returns:
            io.BytesIO: Captured frame in bytes
        """
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        res, frame = cap.read()
        if not res:
            raise Exception("Can't capture frame")

        frame = self._process_frame(frame)

        res, buffer = cv2.imencode(self.format, frame)
        if not res:
            raise Exception("Can't encode frame")

        captured_frame = io.BytesIO(buffer)
        return captured_frame

    def capture(self):
        """Captures frames specified at class initialization

        Returns:
            list[io.BytesIO]: Captured frames
        """
        captured_frames = []
        with VideoCapture(self.source) as cap:
            for frame_number in self.frame_numbers:
                captured_frames.append(self._capture_frame(cap, frame_number))
        return captured_frames

    def capture_frame(self, frame_number):
        """Captures specified frame

        Args:
            frame_number (int): Frame number

        Returns:
            io.BytesIO: Captured frame
        """
        with VideoCapture(self.source) as cap:
            return self._capture_frame(cap, frame_number)
