import matplotlib.pyplot as plt
from colorization.colorizers import *


def ml_paint_image(chat_id):
    image_path = f'{chat_id}_loaded_image.jpg'

    # load colorizers
    colorizer_siggraph17 = siggraph17(pretrained=True).eval()

    # default size to process images is 256x256
    # grab L channel in both original ("orig") and resized ("rs") resolutions
    img = load_img(image_path)
    (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256, 256))

    # colorizer outputs 256x256 ab map
    # resize and concatenate to original L channel
    img_bw = postprocess_tens(tens_l_orig, torch.cat((0 * tens_l_orig, 0 * tens_l_orig), dim=1))
    out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())
    plt.imsave(f'{chat_id}_painted_image.png', out_img_siggraph17)
