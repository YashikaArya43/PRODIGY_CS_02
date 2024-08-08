from PIL import Image

def xor_pixel(pixel, key):
    """Apply XOR operation to each component of the pixel with the given key."""
    return tuple(c ^ key for c in pixel)

def encrypt_image(input_path, output_path, key):
    """Encrypt an image by applying XOR operation to each pixel."""
    with Image.open(input_path) as img:
        pixels = img.load()
        width, height = img.size
        encrypted_image = Image.new('RGB', (width, height))
        encrypted_pixels = encrypted_image.load()

        for x in range(width):
            for y in range(height):
                encrypted_pixels[x, y] = xor_pixel(pixels[x, y], key)

        encrypted_image.save(output_path)
        print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    """Decrypt an image by applying XOR operation to each pixel."""
    # Decryption is the same as encryption with XOR
    encrypt_image(input_path, output_path, key)

def main():
    print("Image Encryption Tool")
    action = input("Would you like to (E)ncrypt or (D)ecrypt an image? ").strip().upper()

    if action not in ('E', 'D'):
        print("Invalid choice. Please select 'E' for Encrypt or 'D' for Decrypt.")
        return

    input_path = input("Enter the input image file path: ")
    output_path = input("Enter the output image file path: ")
    try:
        key = int(input("Enter the XOR key (integer between 0 and 255): "))
        if not (0 <= key <= 255):
            raise ValueError("Key must be between 0 and 255.")
    except ValueError as ve:
        print(f"Invalid key value: {ve}")
        return

    if action == 'E':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
