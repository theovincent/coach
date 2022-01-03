import os
from PIL import Image


def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


def square_images(path_to_images):
    for target in ["A", "B"]:
        for fold in ["train", "val", "test"]:
            for path_image in os.listdir(f"{path_to_images}/{target}/{fold}"):
                im = Image.open(f"{path_to_images}/{target}/{fold}/{path_image}")
                im_new = expand2square(im, 0)
                im_new.save(f"{path_to_images}/{target}/{fold}/{path_image}")


if __name__ == "__main__":
    square_images("../pytorch-CycleGAN-and-pix2pix/Doom_Heatlh_Supreme_Small/")
