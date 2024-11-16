"""
Cepton Programming Question:

We are looking for a program that manages “intensity” by segments. Segments are intervals from -infinity to infinity, we liked you to implement functions 
that updates intensity by an integer amount for a given range. All intensity starts with 0. Please implement these two functions:

add(from, to, amount)  
set(from, to, amount)
You should implement the functions based on your own interpretation of the problem and document any assumptions you make. 

Here is an example sequence (data stored as an array of start point and value for each segment.):
Start: []
Call: add(10, 30, 1) => [[10,1],[30,0]]
Call: add(20, 40, 1) => [[10,1],[20,2],[30,1],[40,0]]
Call: add(10, 40, -2) => [[10,-1],[20,0],[30,-1],[40,0]]

Start: []
Call: add(10, 30, 1) => [[10,1],[30,0]]
Call: add(20, 40, 1) => [[10,1],[20,2],[30,1],[40,0]]
Call: add(10, 40, -1) => [[20,1],[30,0]]
Call: add(10, 40, -1) => [[10,-1],[20,0],[30,-1],[40,0]]
"""

class IntensityManager:
    def __init__(self):
        # Dictionary to store intensity changes
        self.changes = {}
        # List to store the final segments with intensities
        self.segments = []

    def add(self, start, end, amount):
        """
        Add intensity for the range [start, end) with the given amount.
        Avoids duplicates and ensures the specified range is updated correctly.
        """
        # Update changes for the range
        self.changes[start] = self.changes.get(start, 0) + amount
        self.changes[end] = self.changes.get(end, 0) - amount

        # Start building the new segments list
        new_segments = []
        running_intensity = 0

        # Sort the keys
        sorted_points = sorted(self.changes.keys())

        for i, point in enumerate(sorted_points):
            # Update running intensity
            running_intensity += self.changes[point]

            # Add the current point to new_segments
            if not new_segments or new_segments[-1][0] != point:  # Avoid duplicates
                new_segments.append([point, running_intensity])

        # Merge with previous segments to retain non-zero values outside the range
        merged_segments = []
        existing_index = 0

        for segment in new_segments:
            point, value = segment

            # Add all previous segments that occur before the current point
            while existing_index < len(self.segments) and self.segments[existing_index][0] < point:
                prev_point, prev_value = self.segments[existing_index]
                if prev_value != 0 and (not merged_segments or merged_segments[-1][0] != prev_point):
                    merged_segments.append([prev_point, prev_value])
                existing_index += 1

            # Add the current segment
            if value != 0 and (not merged_segments or merged_segments[-1][0] != point):
                merged_segments.append([point, value])

        # Add any remaining previous segments
        while existing_index < len(self.segments):
            prev_point, prev_value = self.segments[existing_index]
            if prev_value != 0 and (not merged_segments or merged_segments[-1][0] != prev_point):
                merged_segments.append([prev_point, prev_value])
            existing_index += 1

        # Ensure the last boundary is included
        if len(self.segments) > 0 and self.segments[-1][1] == 0:
            last_boundary = self.segments[-1]
            if merged_segments[-1][0] != last_boundary[0]:
                merged_segments.append(last_boundary)

        # Remove duplicates explicitly
        final_segments = []
        for i, segment in enumerate(merged_segments):
            if i == 0 or segment != merged_segments[i - 1]:
                final_segments.append(segment)

        # Update self.segments
        self.segments = final_segments



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
