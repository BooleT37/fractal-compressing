class TransformationInfo:
    def __init__(self, domain_index, transform_num, brightness, contrast, psnr):
        """
        :param domain_index: number
        :param transform_num: number
        :param brightness: number
        :param contrast: number
        :param psnr: number
        """
        self.domain_index = domain_index
        self.brightness = brightness
        self.contrast = contrast
        self.transform_num = transform_num
        self.psnr = psnr

    def __str__(self):
        return f"(domain_block: {self.domain_index}, transform: {self.transform_num}," \
               f"brightness: {self.brightness}, contrast: {self.contrast}, PSNR: {self.psnr})"

    def __repr__(self):
        return "\n" + self.__str__()
