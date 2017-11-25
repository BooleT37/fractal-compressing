class EncodedImage:
    def __init__(self, transformations, width, height):
        """
        :param transformations: models.TransformationInfo.TransformationInfo
        :param width: number
        :param height: number
        """
        self.transformations = transformations
        self.width = width
        self.height = height

    def __str__(self):
        return f"width: {self.width}\nheight: {self.height}\ntransformations: {self.transformations}\n"
