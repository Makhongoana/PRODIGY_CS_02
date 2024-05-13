from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Iterate through each pixel and apply encryption
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            img.putpixel((x, y), encrypted_pixel)

    # Save the encrypted image
    img.save("encrypted_image.png")

# Function to decrypt the image
def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    width, height = img.size

    # Iterate through each pixel and apply decryption
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            img.putpixel((x, y), decrypted_pixel)

    # Save the decrypted image
    img.save("decrypted_image.png")

# Example usage
image_path = "/storage/emulated/0/Pictures/facebook/1714968292193.jpg"
encryption_key = 50

# Encrypt the image
encrypt_image(image_path, encryption_key)

# Decrypt the encrypted image
decrypt_image("encrypted_image.png", encryption_key)