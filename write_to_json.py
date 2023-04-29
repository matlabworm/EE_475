# script to return a JSON file per image

import json

# Opening JSON file
root = "/Users/user/Desktop/trashcan1/json/"
f = open(root + 'instances_val_trashcan.json')

data = json.load(f)

for image in data['images']:           # iteration per image
    bbox = []
    labels = []
    for annotation in data['annotations']:  # iteration per object in an image
        if image['id'] == annotation['image_id']:
            bbox.append(annotation['bbox'])
            labels.append(annotation['category_id'])
    if len(bbox):           # if there is an object in the image
        dictionary = {
            "file_name": image['file_name'],
            "image_id": image['id'],
            "annotations": {
                "object_1": {
                    "bbox_coordinates": bbox[0],
                    "category_id": labels[0]}
            }
        }
        if len(bbox) > 1:     # for multiple objects in an image
            for h in range(1, len(bbox)):
                dictionary["annotations"]["object_" + str(h+1)] = {
                    "bbox_coordinates": bbox[h],
                    "category_id": labels[h]}
    else:       # background is chosen as an object if there is no object in the image
        dictionary = {
            "file_name": image['file_name'],
            "image_id": image['id'],
            "annotations": {
                "object_1": {
                    "bbox_coordinates": [0, 0, image['width'], image['height']],
                    "category_id": 0}
            }
        }
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    file_name = image['file_name']
    file_name = file_name.rsplit(".", 1)[0]
    json_file_name = file_name + ".json"

    file = open(json_file_name, "w+")
    json_directory = root + json_file_name

    # Writing to sample.json
    with open(json_directory, "w") as outfile:
        outfile.write(json_object)
