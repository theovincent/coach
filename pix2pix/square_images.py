import os

from PIL import Image

from rl_coach.architectures.pix2pix import expand2square


def square_images(path_to_images):
    for target in ["A", "B"]:
        for fold in ["train", "val", "test"]:
            for path_image in os.listdir(f"{path_to_images}/{target}/{fold}"):
                im = Image.open(f"{path_to_images}/{target}/{fold}/{path_image}")
                im_new = expand2square(im, 0)
                im_new.save(f"{path_to_images}/{target}/{fold}/{path_image}")


if __name__ == "__main__":
    square_images("../pytorch-CycleGAN-and-pix2pix/Doom_Heatlh_Supreme_Small/")
