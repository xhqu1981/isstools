
from bluesky.callbacks import CallbackBase
from xas.process import process_interpolate_bin


class ScanProcessingCallback(CallbackBase):
    def __init__(self, db, draw_func_interp, draw_func_bin):
        self.db = db
        self.draw_func_interp = draw_func_interp
        self.draw_func_bin = draw_func_bin
        super().__init__()

    def stop(self, doc):
        process_interpolate_bin(doc, self.db, self.draw_func_interp, self.draw_func_bin)
