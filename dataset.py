
from torch.utils.data import Dataset
import os
import torch
import torch.utils.data
from PIL import Image
import json


class TrashCanDataset(torch.utils.data.Dataset):
    def __init__(self, root, transforms=None):
        self.root = root
        self.transforms = transforms
        # load all image files, sorting them to
        # ensure that they are aligned
        self.imgs = list(sorted(os.listdir(os.path.join(root, "images"))))
        self.objs = list(sorted(os.listdir(os.path.join(root, "objects"))))

    def __getitem__(self, idx):
        # load images and objects
        img_path = os.path.join(self.root, "images", self.imgs[idx])

        img_name = self.imgs[idx]
        obj_path = os.path.join(self.root, "objects", img_name.rsplit(".", 1)[0] + ".json")
        img = Image.open(img_path).convert("RGB")

        f = open(obj_path)
        data = json.load(f)

        # get the bounding box coordinates and the label for each object
        boxes = []
        labels = []
        for obj in data['annotations']:
            pos = data['annotations'][obj]["bbox_coordinates"]
            xmin = pos[0]
            xmax = xmin + pos[2]
            ymin = pos[1]
            ymax = ymin + pos[3]
            boxes.append([xmin, ymin, xmax, ymax])
            labels.append(data['annotations'][obj]['category_id'])

        boxes = torch.as_tensor(boxes, dtype=torch.float32)
        labels = torch.as_tensor(labels, dtype=torch.int64)

        image_id = torch.tensor([idx])

        target = {"boxes": boxes, "labels": labels, "image_id": image_id}

        if self.transforms:
            img, target = self.transforms(img, target)

        return img, target

    def __len__(self):
        return len(self.imgs)
