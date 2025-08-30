from PIL import Image
import numpy as np
import os

def create_test_image():
    """Create a simple test image for demonstration"""
    # Create a 100x100 RGB image with a gradient
    width, height = 100, 100
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    
    # Create a gradient pattern
    for x in range(width):
        for y in range(height):
            r = int((x / width) * 255)
            g = int((y / height) * 255)
            b = int(((x + y) / (width + height)) * 255)
            pixels[x, y] = (r, g, b)
    
    # Save the test image
    image.save('test_image.png')
    print("Created test_image.png")
    return 'test_image.png'

def test_encryption_decryption():
    """Test the encryption and decryption process"""
    print("=== Image Encryption Test ===")
    print()
    
    # Create a test image
    test_image_path = create_test_image()
    
    # Test key
    key = 123
    
    # Import the encryption functions
    from image_encryptor import encrypt_image, decrypt_image
    
    # Encrypt the image
    encrypted_path = 'encrypted_image.png'
    encrypt_image(test_image_path, encrypted_path, key)
    
    # Decrypt the image
    decrypted_path = 'decrypted_image.png'
    decrypt_image(encrypted_path, decrypted_path, key)
    
    # Verify the images
    original = Image.open(test_image_path)
    decrypted = Image.open(decrypted_path)
    
    # Convert to numpy arrays for comparison
    original_array = np.array(original)
    decrypted_array = np.array(decrypted)
    
    # Check if they are identical
    if np.array_equal(original_array, decrypted_array):
        print("✓ Test passed: Original and decrypted images are identical!")
    else:
        print("✗ Test failed: Images are different!")
    
    # Show file sizes
    original_size = os.path.getsize(test_image_path)
    encrypted_size = os.path.getsize(encrypted_path)
    decrypted_size = os.path.getsize(decrypted_path)
    
    print(f"\nFile sizes:")
    print(f"Original: {original_size} bytes")
    print(f"Encrypted: {encrypted_size} bytes")
    print(f"Decrypted: {decrypted_size} bytes")
    
    # Clean up test files
    for file in [encrypted_path, decrypted_path]:
        if os.path.exists(file):
            os.remove(file)
    
    print("\nTest completed!")

if __name__ == "__main__":
    test_encryption_decryption()
