from PIL import Image

def load_image(image_path):
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, output_path):
    try:
        image.save(output_path)
        print(f"Image saved successfully to {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

def swap_pixels(image):
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width // 2):
            left_pixel = pixels[x, y]
            right_pixel = pixels[width - x - 1, y]
            pixels[x, y] = right_pixel
            pixels[width - x - 1, y] = left_pixel

def invert_pixels(image):
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = (255 - r, 255 - g, 255 - b)

def apply_operation(image, operation):
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]
            if operation == "add":
                r, g, b = (r + 50) % 256, (g + 50) % 256, (b + 50) % 256
            elif operation == "subtract":
                r, g, b = (r - 50) % 256, (g - 50) % 256, (b - 50) % 256
            elif operation == "multiply":
                r, g, b = (r * 2) % 256, (g * 2) % 256, (b * 2) % 256
            pixels[x, y] = (r, g, b)

def main():
    image_path = input("Enter the path to the image: ")
    image = load_image(image_path)
    if not image:
        return
    print("Available operations:")
    print("1. Swap pixels")
    print("2. Invert pixels")
    print("3. Apply mathematical operation (add, subtract, multiply)")
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
    output_path = input("Enter the output path to save the image: ")
    save_image(image, output_path)

if __name__ == "__main__":
    main()
