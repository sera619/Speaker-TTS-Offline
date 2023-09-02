from PySide6.QtCore import QRunnable, Slot, QThreadPool, QObject, Signal
import time

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

        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress
        
    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            print("Somewith wrong with Worker")
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
