import pytube
import helpers.global_constants as global_obj


class Download(object):
    """
    Class for Download videos
    """

    def __init__(self):
        pass

    @staticmethod
    def get_streams():
        """
        Gets the possible streams from the url
        :return streams: Streams
        :author: Sayyuf Shaik
        """
        yt = pytube.YouTube(global_obj.DOWNLOAD_URL)
        return yt.streams.all()

    @staticmethod
    def download_the_stream():
        return Download.get_streams()[0].download()
