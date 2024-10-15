
class Point:
  def __init__(self, x,y):
    self.x_ = x
    self.y_ = y

class Box:
  def __init__(self, p1, p2):
    self.lb = Point(p1)
    self.rt = Point(p2) 
  
class Event:
    def __init__(self, x, y1, y2, typ):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.typ = typ  # 1 for start, -1 for end

def overlaps(r1, r2):
    return not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3])

def check_overlapping_rectangles(rectangles):
    events = []
    
    # Create events for the sweep line
    for (x1, y1, x2, y2) in rectangles:
        events.append(Event(x1, y1, y2, 1))  # Start event
        events.append(Event(x2, y1, y2, -1)) # End event

    # Sort events: by x coordinate, then by type
    events.sort(key=lambda e: (e.x, e.typ))

    active_intervals = []

    for event in events:
        if event.typ == 1:  # Starting event
            for (y1, y2) in active_intervals:
                if overlaps((event.x, event.y1, event.x, event.y2), (event.x, y1, event.x, y2)):
                    return True
            active_intervals.append((event.y1, event.y2))
        else:  # Ending event
            active_intervals.remove((event.y1, event.y2))

    return False

# Example usage
rectangles = [
    (1, 1, 3, 3),
    (2, 2, 4, 4),
    (5, 5, 7, 7),
]

print(check_overlapping_rectangles(rectangles))  # Output: True


class Event:
    def __init__(self, x, y1, y2, typ):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.typ = typ  # 1 for start, -1 for end

def overlaps(r1, r2):
    return not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3])

def insert_active_interval(active_intervals, new_interval):
    """ Insert new_interval while maintaining sorted order """
    for i in range(len(active_intervals)):
        if active_intervals[i][0] > new_interval[0]:  # Compare y1
            active_intervals.insert(i, new_interval)
            return
    active_intervals.append(new_interval)  # If it's the largest, add to the end

def remove_active_interval(active_intervals, interval):
    """ Remove the interval from active_intervals """
    active_intervals.remove(interval)

def check_overlapping_rectangles(rectangles):
    events = []
    
    # Create events for the sweep line
    for (x1, y1, x2, y2) in rectangles:
        events.append(Event(x1, y1, y2, 1))  # Start event
        events.append(Event(x2, y1, y2, -1)) # End event

    # Sort events: by x coordinate, then by type
    events.sort(key=lambda e: (e.x, e.typ))

    active_intervals = []

    for event in events:
        if event.typ == 1:  # Starting event
            # Check for overlaps with active intervals
            for interval in active_intervals:
                if overlaps((event.x, event.y1, event.x, event.y2), interval):
                    return True
            # Add the new interval to active intervals
            insert_active_interval(active_intervals, (event.y1, event.y2))
        else:  # Ending event
            remove_active_interval(active_intervals, (event.y1, event.y2))

    return False

# Example usage
rectangles = [
    (1, 1, 3, 3),
    (2, 2, 4, 4),
    (5, 5, 7, 7),
]

print(check_overlapping_rectangles(rectangles))  # Output: True

class Point:
  def __init__(self, x,y):
    self.x_ = x
    self.y_ = y



class Box:
  def __init__(self, p1, p2):
    self.lb = Point(p1)
    self.rt = Point(p2) 
  
