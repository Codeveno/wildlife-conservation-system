import torch
from deep_sort_realtime.deepsort_tracker import DeepSort

class DeepSORTTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)

    def update(self, detections, img_info):
        tracks = self.tracker.update_tracks(detections, img_info=img_info)
        return [track.to_tlbr() for track in tracks if track.is_confirmed()]
