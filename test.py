import qrcode
from qrcode.image.pure import PyPNGImage

img = qrcode.make("https://ys.learnus.org", image_factory=PyPNGImage)
print(img)
