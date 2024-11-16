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
        Avoids duplicates and ensures the specified range is updated correctly.

        Args:
            start (_type_): _description_
            end (_type_): _description_
            amount (_type_): _description_
        """
        
        self.changes[start] = self.changes.get(start, 0) + amount
        # Fetch the previous value at the boundary `end` or default to 0
        previous_value = next((value for point, value in self.segments if point == end), 0)

        # Adjust the `end` boundary by subtracting the amount
        self.changes[end] = previous_value - amount
        
        # Start building the new segments list
        new_segments = []
        running_intensity = 0

        sorted_points = sorted([[key, value] for key, value in self.changes.items()])
        
        new_segments = []
        running_intensity = 0
        
        for point, value in sorted_points:
            running_intensity += value
            if not new_segments or new_segments[-1][1] != running_intensity:
                new_segments.append([point, running_intensity])
                
        
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
                
        merged_segments.extend(self.segments[i:])
        merged_segments.extend(new_segments[j:])
        
        self.segments = merged_segments
        
        
    def set(self, start, end, amount):
        """
        Set intensity for the range [start, end) to a specific value.
        Overwrites the specified range while retaining unaffected segments.
        Ensures no duplicate boundaries are created.
        """
        # Update changes dictionary to reflect the new range
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


        
if __name__== "__main__":
    
    IntensityManager = IntensityBySegments()

    IntensityManager.add(20, 40, 1)
    print(IntensityManager.segments)
    
    IntensityManager.add(60, 90, 1)
    print(IntensityManager.segments)
    
    IntensityManager.set(50, 120, 8)
    print(IntensityManager.segments)
    
    IntensityManager.add(-10, 60, -5)
    print(IntensityManager.segments)
    
    IntensityManager.set(0, 10, -5)
    print(IntensityManager.segments)
    
    
    

                    