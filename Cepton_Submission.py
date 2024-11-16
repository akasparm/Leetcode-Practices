"""
# Title:    Cepton Coding Challenge for Perception Software Engineer

__author__ = "Akash Parmar"
__email__ = "akashparmar1998.ap@gmailcom"

################################################################### QUESTION ####################################################################
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

################################################################### ASSUMPTIONS ##################################################################
1. Segment boudaries are integers and are multiple of 10. Ranges are inclusive of start, but exclusive of end.
2. Output doesn't show the segment with consistent values. (By default the whole segment -inf to inf has the value 0 and therefore, start: [] shows nothing).
3. Segments from start to end are constant unless otherwise modified by add or set.
4. Segments are sorted and the queries are always given in sorted form. (start <= end)
5. Set method overwrites the previous value of respective segments with the newly given value.
"""

class IntensityBySegments:
    def __init__(self):
        """
        Initializes the IntensityBySegments class.

        Attributes:
            segments (list): A list to store the final segments with their corresponding 
                            running intensity values. Each element is a list [point, intensity].
            changes (dict): A dictionary to store intensity changes at specific points. 
                            The keys represent the points, and the values represent the 
                            cumulative change in intensity at that point.
        """

        self.segments = []
        self.changes = {}
        
    def add(self, start, end, amount):
        """
        Add intensity for the range [start, end) with the given amount.
        Merges the new segment into the `changes` dictionary directly.
        """
        # print("Changes before addition:", self.changes)

        # Merge the start point
        if start in self.changes:
            self.changes[start] += amount  # Add the value to the existing entry
        else:
            self.changes[start] = amount  # Add new entry for `start`

        # Merge the end point
        if end not in self.changes:
            self.changes[end] = 0  # Add the value to the existing entry
            
        # Step 3: Update at intervals of 10
        current = start + 10
        while current < end:
            if current in self.changes:
                self.changes[current] += amount  # Update existing entry
            else:
                self.changes[current] = amount  # Add new entry for the interval
            current += 10
            
        # print("Dict after adding the intervals: ", self.changes)
        
        ## Convert to segment format
        all_segments = [[key, self.changes[key]] for key in sorted(self.changes.keys())]

        # Filter segments to only include points where values change
        filtered_segments = []
        for i, segment in enumerate(all_segments):
            if i == 0 or segment[1] != all_segments[i - 1][1]:
                filtered_segments.append(segment)

        self.segments = filtered_segments

        
        
    def set(self, start, end, amount):
        """
        Set intensity for the range [start, end) to a specific value.
        Overwrites the specified range while retaining unaffected segments.
        Updates only the existing keys in `changes` and adds new ones from `new_segments`.
        """
        # Update the changes dictionary for the new range
        self.changes[start] = amount
        previous_value = next((value for point, value in self.segments if point == end), 0)
        self.changes[end] = previous_value  
        
        # Start building a new segments list
        new_segments = []

        # Add unchanged segments before the `start`
        for segment in self.segments:
            point, value = segment
            if point < start:
                new_segments.append([point, value])

        # Add the new `set` values for the range [start, end)`
        if not new_segments or new_segments[-1][1] != amount:
            new_segments.append([start, amount])
        if not new_segments or new_segments[-1][0] != end:
            new_segments.append([end, previous_value])  # Reset the boundary explicitly

        # Add unchanged segments after the `end`
        for segment in self.segments:
            point, value = segment
            if point > end:
                new_segments.append([point, value])

        # Filter consistent values for the final segments list
        filtered_segments = []
        for i, (point, value) in enumerate(new_segments):
            if i == 0 or value != new_segments[i - 1][1]:
                filtered_segments.append([point, value])

        # Update the segments with filtered values
        self.segments = filtered_segments

        # Step 3: Update at intervals of 10
        current = start + 10
        while current < end:
            self.changes[current] = amount  # Update existing entry
            current += 10



        
if __name__== "__main__":
    
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

                    