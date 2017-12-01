class EncodedImage:
    def __init__(self, transformations, width, height, mean, std):
        """
        :param transformations: models.TransformationInfo.TransformationInfo
        :param width: number
        :param height: number
        """
        self.transformations = transformations
        self.width = width
        self.height = height
        self.mean = mean
        self.std = std

    def __str__(self):
        return f"width: {self.width}\nheight: {self.height}\nmean: {self.mean}" \
               f"\nstd: {self.std}\ntransformations: {self.transformations}\n"
