from PIL import Image
import argparse

def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image by applying XOR operation to each pixel with a key
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the encrypted image
        key (int): Encryption key (0-255)
    """
    try:
        # Open the image
        image = Image.open(input_path)
        pixels = image.load()
        
        # Get image dimensions
        width, height = image.size
        
        # Create a new image for the encrypted result
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_pixels = encrypted_image.load()
        
        # Encrypt each pixel
        for x in range(width):
            for y in range(height):
                if image.mode == 'RGB':
                    r, g, b = pixels[x, y]
                    # XOR each color channel with the key
                    encrypted_pixels[x, y] = (r ^ key, g ^ key, b ^ key)
                elif image.mode == 'RGBA':
                    r, g, b, a = pixels[x, y]
                    # XOR RGB channels, keep alpha unchanged
                    encrypted_pixels[x, y] = (r ^ key, g ^ key, b ^ key, a)
                else:
                    # For grayscale images
                    pixel = pixels[x, y]
                    encrypted_pixels[x, y] = pixel ^ key
        
        # Save the encrypted image
        encrypted_image.save(output_path)
        print(f"Image encrypted successfully! Saved as {output_path}")
        
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypt an image by applying the same XOR operation again
    
    Args:
        input_path (str): Path to the encrypted image
        output_path (str): Path to save the decrypted image
        key (int): Decryption key (must be same as encryption key)
    """
    # Decryption is the same as encryption (XOR is reversible)
    encrypt_image(input_path, output_path, key)
    print(f"Image decrypted successfully! Saved as {output_path}")

def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output image file path")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (0-255)")
    
    args = parser.parse_args()
    
    # Validate key range
    if args.key < 0 or args.key > 255:
        print("Error: Key must be between 0 and 255")
        return
    
    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.key)
    else:
        decrypt_image(args.input, args.output, args.key)

if __name__ == "__main__":
    main()
