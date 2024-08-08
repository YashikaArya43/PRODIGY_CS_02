xor_pixel Function:
Takes a pixel (a tuple of RGB values) and a key.
Applies the XOR operation to each color component with the key and returns the result.
encrypt_image Function:
Opens the image and reads its pixels.
Creates a new image and applies the XOR operation to each pixel.
Saves the encrypted image.
decrypt_image Function:
The decryption process is the same as encryption due to the reversible nature of XOR.
main Function:
Handles user input for encryption or decryption.
Takes file paths and a key value from the user.
Calls the appropriate function based on the user's choice.
