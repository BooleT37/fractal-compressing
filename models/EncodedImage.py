class EncodedImage:
    def __init__(self, width, height, transformations):
        self.width = width
        self.height = height
        self.transformations = transformations

    def __str__(self):
        return f"width: {self.width}\nheight: {self.height}\ntransformations: {self.transformations}\n"
