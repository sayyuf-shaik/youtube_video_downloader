import pytube
import helpers.global_vars as global_obj


class Download(object):
    """
    Class for Download videos
    """

    def __init__(self, instance):
        self.video = ""
        self.ui = instance

    def get_streams(self):
        """
        Gets the possible streams from the url
        :return streams: Streams
        :author: Sayyuf Shaik
        """
        yt = pytube.YouTube(global_obj.DOWNLOAD_URL, on_progress_callback=self.progress_callback)
        return yt.streams.first()

    def download_the_stream(self):
        """
        Downloads the streams
        :return file_name: Downloaded file name
        :author: Sayyuf Shaik
        """
        self.video = self.get_streams()
        return self.video.download()

    def progress_callback(self, stream, chunk, file_handle, bytes_remaining):
        """
        Progress callback function for progress bar
        :param stream:
        :param chunk:
        :param file_handle:
        :param bytes_remaining:
        :return:
        """
        size = self.video.filesize
        progress = (float(abs((bytes_remaining - size ) / size) * float(100)))
        self.ui.progress.setValue(progress)
