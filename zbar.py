from PIL import Image
# from pyzbar.pyzbar import decode
from pylibdmtx.pylibdmtx import decode
import zxing

reader = zxing.BarCodeReader("/var/opt/zxing")

result = reader.decode('matrix2.png')
print(result)
