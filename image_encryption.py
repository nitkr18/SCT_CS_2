from PIL import Image

def load_image(image_path):
    """Load an image from the given path."""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, output_path):
    """Save the image to the specified path."""
    try:
        image.save(output_path)
        print(f"Image saved successfully to {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

def swap_pixels(image):
    """Swap pixel values in the image."""
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width // 2):  # Swap pixels horizontally
            # Get pixel values
            left_pixel = pixels[x, y]
            right_pixel = pixels[width - x - 1, y]

            # Swap pixel values
            pixels[x, y] = right_pixel
            pixels[width - x - 1, y] = left_pixel

def invert_pixels(image):
    """Invert the color of each pixel in the image."""
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]  # Get RGB values
            pixels[x, y] = (255 - r, 255 - g, 255 - b)  # Invert colors

def apply_operation(image, operation):
    """Apply a mathematical operation to each pixel."""
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]  # Get RGB values

            # Apply the operation
            if operation == "add":
                r, g, b = (r + 50) % 256, (g + 50) % 256, (b + 50) % 256
            elif operation == "subtract":
                r, g, b = (r - 50) % 256, (g - 50) % 256, (b - 50) % 256
            elif operation == "multiply":
                r, g, b = (r * 2) % 256, (g * 2) % 256, (b * 2) % 256

            pixels[x, y] = (r, g, b)

def main():
    # Load the image
    image_path = input("Enter the path to the image: ")
    image = load_image(image_path)
    if not image:
        return

    # Display available operations
    print("Available operations:")
    print("1. Swap pixels")
    print("2. Invert pixels")
    print("3. Apply mathematical operation (add, subtract, multiply)")

    # Get user choice
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        swap_pixels(image)
    elif choice == "2":
        invert_pixels(image)
    elif choice == "3":
        operation = input("Enter the operation (add/subtract/multiply): ")
        apply_operation(image, operation)
    else:
        print("Invalid choice!")
        return

    # Save the modified image
    output_path = input("Enter the output path to save the image: ")
    save_image(image, output_path)

if __name__ == "__main__":
    main()
