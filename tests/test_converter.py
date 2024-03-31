import os
import pytest
from PIL import Image
from src.recastdoc.converter import images_to_pdf


# Utility function for creating a dummy image
def create_dummy_image(path, size=(100, 100), color=(255, 0, 0)):
    img = Image.new("RGB", size, color)
    img.save(path)


@pytest.fixture
def setup_images(tmp_path):
    # Create dummy images for testing
    image_paths = [tmp_path / f"image_{i}.png" for i in range(3)]
    for path in image_paths:
        create_dummy_image(path)
    return image_paths


def test_single_image_to_pdf(setup_images, tmp_path):
    output_pdf_path = tmp_path / "output.pdf"
    images_to_pdf([setup_images[0]], output_pdf_path)
    assert os.path.exists(output_pdf_path), "PDF file was not created."


def test_multiple_images_to_pdf(setup_images, tmp_path):
    output_pdf_path = tmp_path / "output.pdf"
    images_to_pdf(setup_images, output_pdf_path)
    assert os.path.exists(output_pdf_path), "PDF file was not created."


def test_no_image_files(tmp_path):
    output_pdf_path = tmp_path / "output.pdf"
    with pytest.raises(ValueError):
        images_to_pdf([], output_pdf_path)
