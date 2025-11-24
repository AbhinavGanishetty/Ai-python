class RectangleAI:
    """
    AI-Generated Docstring:
    -----------------------
    Represents a rectangle defined by its width and height. 
    Provides methods to compute the geometric area and perimeter.
    
    Attributes:
        width (float): The horizontal length of the rectangle.
        height (float): The vertical length of the rectangle.
    
    Methods:
        area(): Returns the area of the rectangle (width × height).
        perimeter(): Returns the perimeter (2 × (width + height)).
    """

    def __init__(self, width, height):
        # AI-generated inline comment:
        # Store width and height values to define the rectangle dimensions.
        self.width = width
        self.height = height

    def area(self):
        # AI-generated inline comment:
        # Area is computed by multiplying width and height.
        return self.width * self.height

    def perimeter(self):
        # AI-generated inline comment:
        # Perimeter is calculated as twice the sum of width and height.
        return 2 * (self.width + self.height)



class RectangleManual:
    """
    Manually Written Docstring:
    ---------------------------
    A simple Rectangle class that supports computation of area and perimeter.
    
    This class is intentionally documented by hand to contrast with
    the automatically generated version above. Its purpose is identical,
    but the writing style is more concise and human-tailored.

    Parameters:
        width (float): The rectangle's width.
        height (float): The rectangle's height.

    Functions:
        area(): Compute and return width * height.
        perimeter(): Compute and return 2 * (width + height).
    """

    def __init__(self, width, height):
        # Manual comment:
        # Initialize rectangle dimensions.
        self.width = width
        self.height = height

    def area(self):
        # Manual comment:
        # Standard geometric area formula.
        return self.width * self.height

    def perimeter(self):
        # Manual comment:
        # Standard perimeter formula.
        return 2 * (self.width + self.height)



# ---------------------------
# DEMO / TEST EXECUTION
# ---------------------------
if __name__ == "__main__":
    rect_ai = RectangleAI(10, 5)
    rect_manual = RectangleManual(10, 5)

    print("AI Rectangle:")
    print("  Area:", rect_ai.area())
    print("  Perimeter:", rect_ai.perimeter())

    print("\nManual Rectangle:")
    print("  Area:", rect_manual.area())
    print("  Perimeter:", rect_manual.perimeter())
