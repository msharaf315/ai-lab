import os
import numpy as np
from PIL import Image
from torch.utils.data import Dataset


class EverdellBoardDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = os.listdir(image_dir)

    def __len__(self):
        return len(self.images)

    def __get_item__(self, index):
        image_path = os.path.join(self.image_dir, self.images[index])
        # TODO replace the self.images[index] for mask to add the suffix for mask
        mask_path = os.path.join(self.mask_dir, self.images[index] + "")
        image = np.array(Image.open(image_path).convert("RGB"))
        mask = np.array(Image.open(mask_path).convert("RGB"), dtype=np.float32)
        if self.transform is not None:
            augmentations = self.transform(image=image, mask=mask)
            image = augmentations["image"]
            mask = augmentations["mask"]

        return image, mask
