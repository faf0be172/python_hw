import os

from src.final_test.painter import ml_paint_image


def test_ml_painter():
    ml_paint_image("faf0be")
    try:
        assert os.path.exists("faf0be_painted_image.png")
    finally:
        os.remove("faf0be_painted_image.png")
