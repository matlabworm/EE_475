# EE_475
EE_475 Underwater Litter Detection

This repository is constructed for people to reproduce the results obtained in my EE_475 project
The dataset is avaliable at https://doi.org/10.13020/g1gx-y834

1) write_to_jason.py file is run to split the json file that is provided with the dataset. The reason behind is to comply with the __getitem__ method in the data loader. All the train and validation images should be moved to the same folder, they will be split later on in the training process. Same goes for the annotations (splitted json files), they should be in a folder next to the images.
2) The other files (except write_to_jason.py) has to be present in the same directory with trashcan.pynb
3) The roots in the files have to be adjusted before running them
4) trashcan.pynb file is run on either google colab or jupyter notebook, note that it is a python notebook file.

As the project goes on, these files will be updated for improved results.
