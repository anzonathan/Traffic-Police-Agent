import cv2
import threading
import time

class Camera:
    def __init__(self, source=0):
        self.source = source
        self.cap = cv2.VideoCapture(self.source)
        self.grabbed, self.frame = self.cap.read()
        self.stopped = False
        self.lock = threading.Lock()

        if not self.cap.isOpened():
            raise ValueError(f"Could not open video source: {self.source}")

    def start(self):
        """Starts the thread to read frames from the video stream."""
        threading.Thread(target=self.update, args=(), daemon=True).start()
        return self

    def update(self):
        """Continuously reads frames from the video stream."""
        while not self.stopped:
            grabbed, frame = self.cap.read()
            with self.lock:
                if grabbed:
                    self.grabbed = grabbed
                    self.frame = frame
                else:
                    # If reading fails (e.g., stream disconnect), we might want to retry or just stop
                    # For now, let's just log and stop, or maybe try to reconnect logic here later
                    # self.stop()
                    pass
            time.sleep(0.005) # Small sleep to prevent CPU hogging

    def read(self):
        """Returns the most recent frame."""
        with self.lock:
            return self.frame if self.grabbed else None

    def stop(self):
        """Stops the camera thread."""
        self.stopped = True
        if self.cap.isOpened():
            self.cap.release()
