from deep_sort_realtime.deepsort_tracker import DeepSort

class DeepSORTTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def track_objects(self, detections):
        tracks = self.tracker.update_tracks(detections, frame=None)
        return [track.to_dict() for track in tracks if track.is_confirmed()]
