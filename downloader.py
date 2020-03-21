#!usr/bin/python3
"""
Youtube Downloader main file
"""
import sys
from PyQt5 import QtWidgets
from GUI.youtube_downlaoder import UiYoutubeDownloader

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    downloader_object = UiYoutubeDownloader()
    downloader_object.show()
    sys.exit(app.exec_())
