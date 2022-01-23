import os

from PIL import Image

from rl_coach.architectures.pix2pix import expand2square


def square_images(path_to_folder, folder, target_folder):
    for target in ["A", "B"]:
        for image_name in os.listdir(f"{path_to_folder}/{folder}/{target}"):
            im = Image.open(f"{path_to_folder}/{folder}/{target}/{image_name}")
            im_new = expand2square(im, 0)

            image_number = int(image_name.split(".")[0])

            if image_number <= 2000:
                fold = "train"
            elif image_number <= 2500:
                fold = "val"
            else:
                fold = "test"
            im_new.save(f"{path_to_folder}/{target_folder}/{target}/{fold}/{image_number}.jpg")


if __name__ == "__main__":
    square_images("../pytorch-CycleGAN-and-pix2pix", "Doom_Health_Supreme", "Doom_Health_Supreme_Split")
