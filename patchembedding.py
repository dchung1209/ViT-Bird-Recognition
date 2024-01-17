import torch
import torch.nn as nn

class PatchEmbedding(nn.Module):
    def __init__(self, in_channels = 3, patch_size = 16, embed_size = 768):
        super().__init__()
        self.patch_size = patch_size
        self.patcher = nn.Conv2d(in_channels = in_channels,
                                 out_channels = embed_size,
                                 kernel_size = patch_size,
                                 stride = patch_size)

        self.flatten = nn.Flatten(start_dim = 2)

    def forward(self, x):
        x = self.patcher(x)
        x = self.flatten(x)
        x = x.permute(0, 2, 1)
        return x