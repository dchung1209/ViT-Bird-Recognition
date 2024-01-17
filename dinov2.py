import torch
import torch.nn as nn

class DinoV2(nn.Module):
    def __init__(self):
        super().__init__()
        self.dinov2 = torch.hub.load('facebookresearch/dinov2', 'dinov2_vitb14')
        self.classifier = nn.Sequential(
            nn.Linear(384, 256),
            nn.ReLU(),
            nn.Linear(256, 20)
        )

    def forward(self, x):
        x = self.dinov2(x)
        x = self.dinov2.norm(x)
        x = self.classifier(x)
        return x
