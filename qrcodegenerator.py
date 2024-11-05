import qrcode

website_link = 'https://sumanth-0.vercel.app/'
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('sumanth-0_qr.png')
