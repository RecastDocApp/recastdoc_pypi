from PIL import Image


def images_to_pdf(image_files, output_pdf):
    """
    Convert a list of image files to a single PDF file.

    Parameters:
    - image_files: A list of paths to the image files.
    - output_pdf: The path for the output PDF file.
    """
    if not image_files:
        raise ValueError("No image files provided")

    # Open and convert images to RGB
    image_list = [Image.open(image_file).convert("RGB") for image_file in image_files]

    # Use the first image as the basis for the PDF
    first_image = image_list[0]
    # If there are additional images, prepare them for appending
    other_images = image_list[1:] if len(image_list) > 1 else []

    # Save the first image, and append the rest if they exist
    if other_images:
        first_image.save(output_pdf, save_all=True, append_images=other_images)
    else:
        first_image.save(output_pdf)
