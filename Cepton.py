
class IntensityManager:
    def __init__(self):
        # Dictionary to store intensity changes
        self.changes = {}
        # List to store the final segments with intensities
        self.segments = []

    def add(self, start, end, amount):
        """
        Add intensity for the range [start, end) with the given amount.
        Ensures the specified range is updated while retaining unaffected segments.
        """
        # Update changes for the range
        self.changes[start] = self.changes.get(start, 0) + amount
        self.changes[end] = self.changes.get(end, 0) - amount

        # Create a sorted list of points with their changes
        sorted_points = sorted([[key, value] for key, value in self.changes.items()])

        # Build the new segments with cumulative intensity
        new_segments = []
        running_intensity = 0

        for point, value in sorted_points:
            running_intensity += value
            if not new_segments or new_segments[-1][1] != running_intensity:
                new_segments.append([point, running_intensity])

        # Merge the new segments with existing segments
        merged_segments = []
        i, j = 0, 0

        while i < len(self.segments) and j < len(new_segments):
            if self.segments[i][0] < new_segments[j][0]:
                merged_segments.append(self.segments[i])
                i += 1
            elif self.segments[i][0] > new_segments[j][0]:
                merged_segments.append(new_segments[j])
                j += 1
            else:
                merged_segments.append(new_segments[j])
                i += 1
                j += 1

        # Add remaining segments from either list
        merged_segments.extend(self.segments[i:])
        merged_segments.extend(new_segments[j:])

        # Update the segments list
        self.segments = merged_segments


    def set(self, start, end, amount):
        """
        Set intensity for the range [start, end) to a specific value.
        Overwrites the specified range while retaining unchanged segments.
        """
        # Start building a new segments list
        new_segments = []

        # Add unchanged segments before the `start`
        for segment in self.segments:
            point, value = segment
            if point < start:
                new_segments.append([point, value])

        # Add the new `set` values for the range [start, end)
        current = start
        while current < end:
            new_segments.append([current, amount])
            current += 10

        # Ensure the `end` point explicitly has intensity 0
        new_segments.append([end, 0])

        # Add unchanged segments after the `end`
        for segment in self.segments:
            point, value = segment
            if point >= end:
                new_segments.append([point, value])

        # Replace the old segments with the new ones
        self.segments = new_segments


# Testing the implementation
manager = IntensityManager()

# Perform operations
manager.set(-20, 0, 3)
print("After set(-20, 0, 3):", manager.segments)  

manager.add(10, 30, 3)
print("After add(10, 30, 3):", manager.segments) 

manager.add(20, 40, 1)
print("After add(20, 40, 1):", manager.segments) 

manager.set(20, 50, 5)
print("After set(20, 50, 5):", manager.segments) 

manager.add(50, 80, -2)
print("After add(50, 80, -2):", manager.segments) 

manager.set(70, 90, 5)
print("After set(70, 90, 5):", manager.segments) 

manager.set(100, 130, -5)
print("After set(100, 130, -5):", manager.segments) 

manager.add(0, 40, -20)
print("After add(0, 40, -20):", manager.segments) 
