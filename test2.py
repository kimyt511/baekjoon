from PIL import Image

original_image_path = "test.png"
qr_image_path = "qrtest.png"

original_image = Image.open(original_image_path)
qr_image = Image.open(qr_image_path)

qr_image = qr_image.resize((50, 50))

position = (
    original_image.width - qr_image.width,
    original_image.height - qr_image.height,
)

original_image.paste(qr_image, position)

original_image.save("merged_image.png")

original_image.show()
