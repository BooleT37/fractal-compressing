class EncodedImage:
    def __init__(self, transformations, width, height):
        self.transformations = transformations
        self.width = width
        self.height = height

    def __str__(self):
        return f"width: {self.width}\nheight: {self.height}\ntransformations: {self.transformations}\n"
