# Model Metrics — KisanAI

**Generated:** 2026-07-08 14:43
**Dataset:** PlantVillage (Kaggle) — 20,638 images across 15 classes
**Model:** EfficientNet-B0 (transfer learning, ImageNet pretrained)

## Training Configuration

| Parameter | Value |
|-----------|-------|
| Batch Size | 32 |
| Image Size | 224×224 |
| Phase 1 LR | 0.001 (frozen backbone) |
| Phase 2 LR | 0.0001 (unfrozen, discriminative) |
| Epochs | 5 + 8 |
| Class Weighted Loss | Yes |

## Validation Results (PlantVillage — Lab Conditions)

| Metric | Value |
|--------|-------|
| **Accuracy** | **99.66%** |
| F1 Score (weighted) | 0.9966 |
| Loss | 0.0069 |

## Known Limitations

- **Class imbalance:** Dataset ranges from ~152 to ~3208 images per class.
- **Worst F1 classes:** Tomato__Target_Spot, Tomato_Early_blight, Tomato_Spider_mites_Two_spotted_spider_mite.
- **Field validation pending:** PlantDoc evaluation not yet run (see Phase 2 checklist in AGENTS.md).

## Honesty Note

These metrics reflect training on the full PlantVillage dataset with real leaf images.
The previous 38% accuracy figure was from training on synthetic color-block data (dummy dataset),
which has been discarded per AGENTS.md honesty requirements.
