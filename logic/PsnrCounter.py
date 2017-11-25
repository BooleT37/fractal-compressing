import math

epsilon = 0.001

def count_mse(pixels_list_1, pixels_list_2):
    n = len(pixels_list_1)
    summ = 0
    for i in range(n):
        pixel1 = pixels_list_1[i]
        pixel2 = pixels_list_2[i]
        diff = pixel1 - pixel2
        if abs(diff) > epsilon:
            summ += diff ** 2

    mse = summ / n
    return mse


def count_psnr(pixels_list_1, pixels_list_2):
    mse = count_mse(pixels_list_1, pixels_list_2)
    if mse == 0:
        raise MseIsZeroException()
    return 10 * math.log10(255 * 255 / mse)


class MseIsZeroException(Exception):
    def __str__(self):
        return "Pixels are equal, PSNR is undefined"
