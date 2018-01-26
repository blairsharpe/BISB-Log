import time
import datetime


class Request:

    def __init__(self, line):

        self.request = tuple(line.split(','))

    def time(self):

        x = time.strptime(self.request[0], '%H:%M:%S')

        seconds = datetime.timedelta(hours=0, minutes=x.tm_min,
                                     seconds=x.tm_sec).total_seconds()
        return int(seconds)

    def pin(self):

        """Function to return pin from the request
            Args:
                param1: self
            :rtype  : str
            :return : 8 character pin
            """

        return self.request[2]

    def bytes(self):

        """Function to return number of bytes from the request
            Args:
                param1: self
            :rtype  : int
            :return : Number of bytes from the request
            """
        if int(self.request[3]) < 0:

            return 0

        else:
            return int(self.request[3])

    def valid(self):

        """Function to return if request is valid
            Args:
                param1: self
                param2: pin
                param3: total_bytes
            :rtype  : bool
            :return : True if valid, False otherwise
            """

        if self.pin() != "" or self.pin() == " ":

            return True
        else:

            return False
