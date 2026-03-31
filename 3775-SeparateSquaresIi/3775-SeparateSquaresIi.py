# Last updated: 3/31/2026, 9:28:36 PM
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        sweep_events = []

        for x, y, side in squares:
            sweep_events.append((y,1,x,x+side))        
            sweep_events.append((y+side,-1,x,x+side))  

        sweep_events.sort()

        active_x_intervals = []
        previous_y = sweep_events[0][0]
        total_union_area = 0
        vertical_strips = []

        def merged_x_length(intervals):
            intervals.sort()
            total = 0
            current_end = -10**30

            for start, end in intervals:
                if start > current_end:
                    total += end - start
                    current_end = end
                elif end > current_end:
                    total += end - current_end
                    current_end = end

            return total

        for y, event_type, x_start, x_end in sweep_events:
            if y > previous_y and active_x_intervals:
                height = y - previous_y
                width = merged_x_length(active_x_intervals)
                vertical_strips.append((previous_y, height, width))
                total_union_area += height * width

            if event_type == 1:
                active_x_intervals.append((x_start, x_end))
            else:
                active_x_intervals.remove((x_start, x_end))

            previous_y = y

        half_area = total_union_area / 2
        accumulated_area = 0

        for base_y, height, width in vertical_strips:
            strip_area = height * width
            if accumulated_area + strip_area >= half_area:
                return base_y + (half_area - accumulated_area) / width
            accumulated_area += strip_area

        return 0.0