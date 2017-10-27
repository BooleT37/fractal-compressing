class TransformationInfo:
    def __init__(self, transform_num, psnr):
        self.transform_num = transform_num
        self.psnr = psnr

    def __str__(self):
        return f"(transform: {self.transform_num}, PSNR: {self.psnr})"

    def __repr__(self):
        return "\n" + self.__str__()
