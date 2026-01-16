
import math
PI = math.pi
 
# Pure-Python FFT but using separate real/imag float arrays (faster than complex objects)
def fft_real_imag(real, imag, invert=False):
    n = len(real)
    j = 0
    # bit-reversal permutation (swap both real and imag)
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            real[i], real[j] = real[j], real[i]
            imag[i], imag[j] = imag[j], imag[i]
 
    length = 2
    while length <= n:
        ang = 2 * PI / length * (-1 if invert else 1)
        wlen_r = math.cos(ang)
        wlen_i = math.sin(ang)
        half = length // 2
 
        # local bindings for speed
        real_local = real
        imag_local = imag
        for i in range(0, n, length):
            w_r = 1.0
            w_i = 0.0
            base = i
            for j in range(base, base + half):
                u_r = real_local[j]
                u_i = imag_local[j]
                v_r = real_local[j + half] * w_r - imag_local[j + half] * w_i
                v_i = real_local[j + half] * w_i + imag_local[j + half] * w_r
 
                real_local[j] = u_r + v_r
                imag_local[j] = u_i + v_i
                real_local[j + half] = u_r - v_r
                imag_local[j + half] = u_i - v_i
 
                # update w *= wlen
                tmp = w_r * wlen_r - w_i * wlen_i
                w_i = w_r * wlen_i + w_i * wlen_r
                w_r = tmp
        length <<= 1
 
    if invert:
        inv_n = 1.0 / n
        for i in range(n):
            real[i] *= inv_n
            imag[i] *= inv_n
 
def multiply(poly1, poly2):
    total = len(poly1) + len(poly2) - 1
    size = 1 << (total - 1).bit_length()
    # prepare arrays (real and imag)
    ar = [0.0] * size
    ai = [0.0] * size
    br = [0.0] * size
    bi = [0.0] * size
    for i, v in enumerate(poly1):
        ar[i] = float(v)
    for i, v in enumerate(poly2):
        br[i] = float(v)
 
    # forward fft on both
    fft_real_imag(ar, ai, invert=False)
    fft_real_imag(br, bi, invert=False)
 
    # pointwise multiply: (ar + i ai) * (br + i bi)
    cr = [0.0] * size
    ci = [0.0] * size
    for i in range(size):
        cr[i] = ar[i] * br[i] - ai[i] * bi[i]
        ci[i] = ar[i] * bi[i] + ai[i] * br[i]
    fft_real_imag(cr, ci, invert=True)
    res = [int(round(cr[i])) for i in range(total)]
    return res


