# Simple Image Encryption Tool

A basic image encryption tool that uses pixel manipulation with XOR operations for simple encryption and decryption.

## Features

- **Simple Encryption**: Uses XOR operation with a key value (0-255)
- **Reversible**: Same operation encrypts and decrypts
- **Multiple Formats**: Supports RGB, RGBA, and grayscale images
- **Command-line Interface**: Easy to use from terminal

## Installation

```bash
pip install Pillow
```

## Usage

### Command Line

```bash
# Encrypt an image
python image_encryptor.py encrypt input.jpg encrypted.png 123

# Decrypt an image  
python image_encryptor.py decrypt encrypted.png decrypted.jpg 123
```

### Parameters

- `mode`: `encrypt` or `decrypt`
- `input`: Input image file path
- `output`: Output image file path  
- `key`: Encryption key (0-255)

### Python Module

```python
from image_encryptor import encrypt_image, decrypt_image

# Encrypt
encrypt_image('input.jpg', 'encrypted.png', 123)

# Decrypt
decrypt_image('encrypted.png', 'decrypted.jpg', 123)
```

## How It Works

The tool performs a simple XOR operation on each pixel:

- For RGB images: `(r ^ key, g ^ key, b ^ key)`
- For RGBA images: `(r ^ key, g ^ key, b ^ key, a)` (alpha unchanged)
- For grayscale: `pixel ^ key`

Since XOR is reversible, the same operation decrypts the image.

## Example

```bash
# Create test image and test encryption
python test_image_encryption.py
```

## Limitations

- Very basic security (not suitable for sensitive data)
- Key must be between 0-255
- Same key must be used for encryption and decryption

## Files

- `image_encryptor.py` - Main encryption/decryption tool
- `test_image_encryption.py` - Test script with demonstration
- `README_image_encryption.md` - This documentation
