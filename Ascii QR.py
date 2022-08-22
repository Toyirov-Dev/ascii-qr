import io
import qrcode
import os

qr = qrcode.QRCode()

data = input("--> ")

qr.add_data(data)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())

os.system('pause')