

## ViT from Scratch
<img src="https://github.com/dchung1209/ViT-Bird-Recognition/assets/121478848/5e48e44e-dbcc-416c-8898-3aba331a82ce" width="700">

The overall structure of the model is derived from [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)


<img src="https://github.com/dchung1209/ViT-Bird-Recognition/assets/121478848/cd522330-dfd0-40b5-89c2-6e916776aca4" width="700">

The hyperparameters of the model adhere to **ViT-Base**

### Result (epoch 300)

| Precision | Recall | F1-Score | Accuracy |
| --------- | ------ | -------- | -------- |
| 85%       | 80%    | 79%      | 80%      |



## DinoV2 

[DinoV2](https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/) is a recent state-of-the-art vision transform model developed by Meta AI.

For the fair comparison, the model using 86M parameters is used

### Result (epoch 40)

| Precision | Recall | F1-Score | Accuracy |
| --------- | ------ | -------- | -------- |
| 90%       | 89%    | 88%      | 89%      |


## ViT (ImageNet-21K Pretrained)

### Result

| Precision | Recall | F1-Score | Accuracy |
| --------- | ------ | -------- | -------- |
| 98%       | 99%    | 98%      | 99%      |
