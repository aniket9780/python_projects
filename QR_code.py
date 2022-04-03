import qrcode


obj_qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)
obj_qr.add_data("https://www.google.com")
obj_qr.make(fit = True)
qr_img = obj_qr.make_image(fill_color = "white", back_color = "black")
qr_img.save("qr_data.png")
