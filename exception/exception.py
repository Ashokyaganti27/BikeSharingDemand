
import sys

class BikeSharingDemand(Exception):
    def __init__(self,error_message):
        self.error_message=error_message
        _,_,exc_tb=sys.exc_info()

        if exc_tb is not None:

            self.lineno=exc_tb.tb_lineno
            self.filename=exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno="you not written in except block"
            self.filename="unknown"

    def __str__(self):
        return "Error in [{0}] line no [{1}] error_message [{2}]".format(
            self.filename,self.lineno,str(self.error_message)
        )
