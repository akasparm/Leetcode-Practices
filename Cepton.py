class IntensityManager:
    def __init__(self):
        # Initialize an empty dictionary to store intensity changes
        self.changes = {}
    
    def add(self, start, end, amount):
        """
        Add intensity for the range [start, end) with the given amount.
        """
        # Update the dictionary with start and end points
        self.changes[start] = self.changes.get(start, 0) + amount
        self.changes[end] = self.changes.get(end, 0) - amount

    def normalize(self):
        """
        Normalize the changes dictionary to calculate running intensity.
        """
        # Step 1: Sort the keys (points)
        sorted_points = sorted(self.changes.keys())

        # Step 2: Calculate cumulative intensities and fill gaps
        result = []
        running_intensity = 0
        
        for i, point in enumerate(sorted_points):
            # Update running intensity
            running_intensity += self.changes[point]
            
            # Check if this point has intensity zero and is not the last one
            if running_intensity == 0 and i < len(sorted_points) - 1:
                continue  # Skip points with zero intensity if they are not the last one

            # Add the current point
            result.append([point, running_intensity])
            
            # Fill in intermediate points if there's a gap
            if i + 1 < len(sorted_points):
                next_point = sorted_points[i + 1]
                # Add intermediate points for the gap if intensity is non-zero
                if running_intensity != 0:
                    for intermediate in range(point + 10, next_point, 10):  # Increment by 10
                        result.append([intermediate, running_intensity])

        return result

# Testing the updated implementation
manager = IntensityManager()


manager.add(10, 30, 3)
print(manager.normalize())  

# Second call: add(20, 40, 1)
manager.add(20, 40, 1)
print(manager.normalize())  

# Third call: add(10, 40, -2)
manager.add(10, 50, -2)
print(manager.normalize())

# Third call: add(10, 40, -2)
manager.add(-30, 80, -2)
print(manager.normalize()) 

# Third call: add(10, 40, -2)
manager.add(90, 100, -2)
print(manager.normalize()) 

