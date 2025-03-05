import qrcode
from PIL import Image

# target_url = "https://wa.me/18183319292?text=Hello%20I%20stopped%20by%20your%20booth%20at%20JIS%20Miami!"
target_url = "https://www.instagram.com/california_earrings"
logo_path = "assets/instagram_logo.png"

# 🔹 Generate QR Code
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo placement
    box_size=25,
    border=3,
)
qr.add_data(target_url)
qr.make(fit=True)

# 🔹 Create QR Code image
qr_img = qr.make_image(fill_color="white", back_color="black").convert("RGB")
# ce logo color: #cfa539

try:
    logo = Image.open(logo_path)

    qr_width, qr_height = qr_img.size
    max_size = qr_width // 5
    w, h = logo.size
    ratio = min(max_size / w, max_size / h)
    new_w, new_h = int(w * ratio), int(h * ratio)
    logo = logo.resize((new_w, new_h))

    padding = 20
    padded_logo_size = (new_w + padding, new_h + padding)
    logo_with_border = Image.new("RGB", padded_logo_size, "black")
    logo_with_border.paste(logo, (padding // 2, padding // 2))
    pos = ((qr_width - padded_logo_size[0]) // 2, (qr_height - padded_logo_size[1]) // 2)

    # Overlay the logo onto the QR code
    qr_img.paste(logo_with_border, pos)

except FileNotFoundError:
    print("❌ Logo file not found! Generating QR code without logo.")

# 🔹 Save QR code with logo
file_output = "output/qr_code_to_ig.png"
qr_img.save(file_output)
print(f"✅ QR Code saved to {file_output}")