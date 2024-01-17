import torch
import torch.nn as nn

from patchembedding import PatchEmbedding


class ViT(nn.Module):
  def __init__(self, img_size = 224, num_channels = 3, patch_size = 16, embed_size = 768,
                      transformer_depth = 12, num_heads = 12, mlp_size = 3072, dropout = 0.1, num_classes = 20):
    super().__init__()

    self.dropout = nn.Dropout(dropout)

    # Patch Embedding
    self.patch_embedding = PatchEmbedding(num_channels, patch_size, embed_size)

    self.cls_token = nn.Parameter(torch.randn(1, 1, embed_size), requires_grad = True)

    # Positional Embedding
    patch_size = (img_size * img_size) // patch_size**2 # N = HW/P^2
    self.positional_embedding = nn.Parameter(torch.randn(1, patch_size + 1, embed_size), requires_grad = True)

    # Transformer Encoder
    self.transformer_encoder = nn.TransformerEncoder(encoder_layer = nn.TransformerEncoderLayer(embed_size,
                                                                                                num_heads,
                                                                                                mlp_size,
                                                                                                activation = "gelu",                                                                                        batch_first = True), num_layers = 12)
    # MLP Head
    self.mlp_head = nn.Sequential(
        nn.LayerNorm(embed_size),
        nn.Linear(embed_size, num_classes)
        )

  def forward(self, x):
    x = self.patch_embedding(x)
    cls_token = self.cls_token.expand(x.shape[0], -1, -1)
    x = torch.cat((cls_token, x), dim = 1)
    x = self.positional_embedding + x
    x = self.dropout(x)
    x = self.transformer_encoder(x)
    x = self.mlp_head(x[:, 0])
    return x
