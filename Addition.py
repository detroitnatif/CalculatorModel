# Import PyTorch
import torch
from torch import nn

import os
# Import torchvision 
import torchvision
from torchvision import datasets
from torchvision.transforms import ToTensor
from torchvision import transforms
# Import matplotlib for visualization
import matplotlib.pyplot as plt

x_train = torch.rand(2, 100)