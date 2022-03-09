import os
import pytest
from aiohttp import ClientConnectorError
from src.hw3.image_downloader import download_some_images


def clear_images_directory():
    for filename in os.listdir("images"):
        file_path = os.path.join("images", filename)
        os.unlink(file_path)


def test_simple_downloading():
    try:
        download_some_images(3)
        assert len(os.listdir("images")) == 3
    except AssertionError:
        raise AssertionError("Images number is incorrect")
    else:
        clear_images_directory()


def test_negative_images_number():
    with pytest.raises(ValueError):
        download_some_images(-1)


def test_host_connection_error():
    try:
        download_some_images(3)
        clear_images_directory()
    except ClientConnectorError:
        raise AssertionError("Cannot connect to host")


def test_image_key_not_found_error():
    try:
        download_some_images(3)
        clear_images_directory()
    except ValueError:
        raise AssertionError("Image link missed")
