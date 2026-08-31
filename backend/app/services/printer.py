"""
Thermal printer integration point.

This does nothing until you have real hardware connected, but it's where that
logic goes once you do. Two common paths for USB/network thermal label printers:

1. Generic ESC/POS thermal printers -> `pip install python-escpos`
     from escpos.printer import Usb
     p = Usb(vendor_id, product_id)
     p.image("label.png")
     p.cut()

2. Brother QL label printers -> `pip install brother_ql`
     from brother_ql.conversion import convert
     from brother_ql.backends.helpers import send
     from brother_ql.raster import BrotherQLRaster
     qlr = BrotherQLRaster('QL-800')
     instructions = convert(qlr=qlr, images=['label.png'], label='29x90')
     send(instructions=instructions, printer_identifier='usb://0x04f9:0x209b', backend_identifier='pyusb')

Wire whichever matches your printer model into print_label() below,
then call it from routers/labels.py after generating the QR image.
"""

def print_label(item_id: str, image_path: str) -> bool:
    raise NotImplementedError(
        "Connect your thermal printer model here (see module docstring), "
        "or print manually via the browser print dialog for now."
    )
