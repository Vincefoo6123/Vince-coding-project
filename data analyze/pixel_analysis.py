"""
SEM 掃描式電子顯微鏡（Scanning Electron Microscope）。
不使用光線，而是利用電子束來「照」出物體的微觀構造。
材料工程師會用 SEM 觀察斷面。
化學家需要確認合成出的奈米粉末是否均勻。
半導體產業 SEM 能快速定位並放大這些極微小的瑕疵
"""
from simpleimage import SimpleImage
img = SimpleImage("partical_analysis.png")
img.show()

n_pixel = 0
n_bg = 0
for pixel in img:
    n_pixel += 1
    total = (pixel.red+pixel.blue+pixel.green)
    if total < 330:
        # bg
        n_bg += 1
        pixel.red = 255
        pixel.blue = 0
        pixel.green = 0
img.show()
print((n_pixel-n_bg)/n_pixel)
