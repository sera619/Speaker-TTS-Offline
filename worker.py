from PySide6.QtCore import QRunnable, Slot, QThreadPool, QObject, Signal
import time
from configparser import ConfigParser

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        
    @Slot()
    def run(self):
        self.fn(*self.args, **self.kwargs)



