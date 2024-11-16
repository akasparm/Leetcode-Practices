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

class IntensityBySegments:
    """
    A class to manage intensity values across continuous segments.
    Segments represent intervals on the number line with specific intensity values.
    This class provides functionality to add or set intensity values over defined ranges.

    Methods:
        __init__():
            Initializes the class with attributes for tracking segment changes and the resulting segments.
        add(start, end, amount):
            Adds a specified intensity amount to a range of segments.
        set(start, end, amount):
            Sets a specified intensity value for a range of segments, overwriting previous values.
    """

    def __init__(self):
        """
        Initializes the IntensityBySegments class.

        Attributes:
            segments (list): Stores the final segments with their corresponding intensity values.
                             Each element is a list [point, intensity].
            changes (dict): Stores intensity changes at specific points.
                            Keys represent the points, and values represent the cumulative change at that point.
        """
        self.segments = []
        self.changes = {}

    def _filter_segments(self, all_segments):
        """
        Filters the list of all segments to only include points where intensity values change.

        Args:
            all_segments (list): List of all segments including points and their intensity values.

        Returns:
            list: A filtered list of segments where intensity values change.
        """
        filtered_segments = []
        for i, segment in enumerate(all_segments):
            if i == 0 or segment[1] != all_segments[i - 1][1]:
                filtered_segments.append(segment)
        return filtered_segments

    def add(self, start, end, amount):
        """
        Adds intensity for the range [start, end) by a specified amount.
        Updates the `changes` dictionary to reflect the added intensity.

        Args:
            start (int): The start point of the range (inclusive).
            end (int): The end point of the range (exclusive).
            amount (int): The amount to add to the intensity in the range.

        Returns:
            None
        """
        # Merge the start point
        if start in self.changes:
            self.changes[start] += amount
        else:
            self.changes[start] = amount

        # Merge the end point
        if end not in self.changes:
            self.changes[end] = 0

        # Update intermediate points at intervals of 10
        current = start + 10
        while current < end:
            if current in self.changes:
                self.changes[current] += amount
            else:
                self.changes[current] = amount
            current += 10

        # Convert changes to segments
        all_segments = [[key, self.changes[key]] for key in sorted(self.changes.keys())]

        # Filter segments using the common method
        self.segments = self._filter_segments(all_segments)

    def set(self, start, end, amount):
        """
        Sets intensity for the range [start, end) to a specific value,
        overwriting any previous intensity values in that range.

        Args:
            start (int): The start point of the range (inclusive).
            end (int): The end point of the range (exclusive).
            amount (int): The intensity value to set for the range.

        Returns:
            None
        """
        # Update changes dictionary for the range
        self.changes[start] = amount
        previous_value = next((value for point, value in self.segments if point == end), 0)
        self.changes[end] = previous_value

        # Update intermediate points at intervals of 10
        current = start + 10
        while current < end:
            self.changes[current] = amount
            current += 10

        # Convert changes to segments
        all_segments = [[key, self.changes[key]] for key in sorted(self.changes.keys())]

        # Filter segments using the common method
        self.segments = self._filter_segments(all_segments)

if __name__ == "__main__":
    """
    Demonstrates the usage of the IntensityBySegments class through various operations.

    Calls methods add() and set() on different ranges and prints the resulting segments.
    """
    IntensityManager = IntensityBySegments()

    IntensityManager.set(-20, 0, 3)
    print("Displayed Result: ", IntensityManager.segments)

    IntensityManager.add(10, 30, 3)
    print("Displayed Result: ", IntensityManager.segments)

    IntensityManager.add(20, 40, 1)
    print("Displayed Result: ", IntensityManager.segments)

    IntensityManager.set(20, 50, 5)
    print("Displayed Result: ", IntensityManager.segments)

    IntensityManager.add(50, 80, -2)
    print("Displayed Result: ", IntensityManager.segments)

    IntensityManager.set(70, 90, 5)
    print("Displayed Result: ", IntensityManager.segments)

    IntensityManager.set(100, 130, -5)
    print("Displayed Result: ", IntensityManager.segments)

    IntensityManager.add(0, 40, -20)
    print("Displayed Result: ", IntensityManager.segments)
