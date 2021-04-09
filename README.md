# DeepLearning2

This repository contains the code used to produce the Practical 2 project report titled '*From Lego Bricks to Actual Bricks: StyleTransfer with CycleGAN*'. 

Our aim with this project was to inspect and develop method to perform image-to-image translation using CycleGAN and two data-sets (Lego House and Real House images)

## Data Sets
1. Lego House image dataset - this dataset was manually created using the Google Image feature and then processed to remove duplicates.
2. Real House image dataset - [House price estimation from visual and textual features](https://github.com/emanhamed/Houses-dataset) was used to gather real house images and then processed to have only the images which contain front images.

## [CycleGAN](https://junyanz.github.io/CycleGAN/)

CycleGAN is a type of GAN which image-to-image translation without the need to image paid between domains. 

## Networks Inspected

1. Standard - The first experiment was observed with the standard CycleGAN.
2. ResNet - ResNet model as a discriminator was used.
3. VGG16 - VGG16 model as a discriminator was used.

## Results 

1. Standard

![alt text](https://github.com/KylevdLangemheen/DeepLearning2/blob/main/standard.png "Standard Result") 
 
2. Resnet

![alt text](https://github.com/KylevdLangemheen/DeepLearning2/blob/main/resnet.png "ResNet Result")

3. VGG16

![alt text](https://github.com/KylevdLangemheen/DeepLearning2/blob/main/vgg.png "VGG results")

## Links
Links and references used in the project

- https://machinelearningmastery.com/cyclegan-tutorial-with-keras
- https://machinelearningmastery.com/how-to-develop-cyclegan-models-from-scratch-with-keras/
