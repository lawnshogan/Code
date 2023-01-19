import qrcode

def generate_qr_code(ssid, password):
    wifi_qr = qrcode.QRCode(version=1, box_size=10, border=5)
    wifi_qr.add_data(f'WIFI:S:{ssid};T:WPA;P:{password};;')
    wifi_qr.make(fit=True)
    img = wifi_qr.make_image(fill_color='black', back_color='white')
    img.save(f'{ssid}.png')
    print(f'QR code saved as {ssid}.png')

# Example usage
generate_qr_code('Wifi_Name', 'Password')