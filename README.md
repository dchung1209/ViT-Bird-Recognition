# Bird Species Recognition

A dataset comprising 20 distinct bird species includes 3,208 training images and 100 test images (with 5 images per species). All the images are in JPG format, with dimensions of 224 x 224 x 3, representing color images.

### Train Distribution
![image](https://github.com/dchung1209/ViT-Bird-Recognition/assets/121478848/3e10d459-a026-4373-a508-78b07300ded3)

### Test Distribution
![image](https://github.com/dchung1209/ViT-Bird-Recognition/assets/121478848/bac9484e-768a-4337-8371-79fcfc524869)


## ViT from Scratch
<img src="https://github.com/dchung1209/ViT-Bird-Recognition/assets/121478848/5e48e44e-dbcc-416c-8898-3aba331a82ce" width="700">

The overall structure of the model is derived from [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)


<img src="https://github.com/dchung1209/ViT-Bird-Recognition/assets/121478848/cd522330-dfd0-40b5-89c2-6e916776aca4" width="700">

The hyperparameters of the model adhere to **ViT-Base**

### Result

| Precision | Recall | F1-Score | Accuracy |
| --------- | ------ | -------- | -------- |
| 85%       | 80%    | 79%      | 80%      |



## DinoV2 

[DinoV2](https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/) is a recent state-of-the-art vision transform model developed by Meta AI.

To ensure a fair comparison, the employed model shares the same embedding dimension and maintains a similar parameter size of 82 million.

### Result 

| Precision | Recall | F1-Score | Accuracy |
| --------- | ------ | -------- | -------- |
| 90%       | 89%    | 88%      | 89%      |


## ViT (ImageNet-21K Pretrained)

### Result

| Precision | Recall | F1-Score | Accuracy |
| --------- | ------ | -------- | -------- |
| 98%       | 99%    | 98%      | 99%      |
