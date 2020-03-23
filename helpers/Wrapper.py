"""
Wrapper for youtube-dl.
"""
# imports
import subprocess
__author__ = "Sayyuf Shaik"


class Execute(object):

    def __init__(self):
        pass

    def execute_command(self, cmd):
        """
        Executes the command passed and returns the return code, std out and std err.
        :param cmd: ``Command to be executes``
        :return bool: ``True/False``
        :return _proc_std_out: ``Process std out``
        :return _proc_std_err: ``Process std err``
        """
        try:
            _proc = subprocess.Popen(cmd)
            _proc_std_out, _proc_std_err = _proc.communicate()
            if _proc.returncode is 0:
                return False, _proc_std_out, _proc_std_err
            return True, _proc_std_out, _proc_std_out
        except Exception as _exp:
            print(_exp)


class Wrapper(Execute):
    """
    Wrapper class for executing command line arguments of youtube-dl
    """
    def __init__(self):
        super().__init__()

    def download(self, url):
        """
        Downloads the video of the provided url
        :param url:
        :return:
        """
        try:
            Execute.execute_command()
        except Exception as _exp:
            print(_exp)
