# Rule: ML conventions

Applies to anything under `ml/`.

## Reproducibility

- Set and log a random seed at the top of every training script. Print
it in the run’s console output and save it in `training_summary.json`.
- Every run’s hyperparameters (learning rates, epoch counts, batch
size, dropout, weight decay) must be printed at the start of the run
and saved alongside the checkpoint, not left implicit in code that
might change later.

## Data handling

- Never commit raw images, `.pt` checkpoints, or `.onnx` exports.
These belong in `.gitignore` under `ml/data/raw/`,
`ml/data/raw_plantdoc/`, and `ml/checkpoints/`.
- Train and validation transforms are different on purpose (train has
augmentation, eval does not) — when modifying `dataset.py`,
preserve this split rather than collapsing to one transform pipeline
for convenience.
- If you change the train/val split ratio or strategy, update the
docstring in `dataset.py` explaining the new approach and why, and
update the corresponding paragraph in `docs/model_metrics.md` if
results have already been generated.

## Metrics and honesty

- Never report only overall accuracy. Per-class F1 and the confusion
matrix are required outputs of every full evaluation run, not
optional extras.
- When evaluating on PlantDoc (field validation), the class-name
mapping between PlantDoc’s labels and PlantVillage’s 38 classes
must be written out explicitly in the notebook, including any
PlantDoc classes that get excluded and why. Silent exclusion is not
acceptable.
- Grad-CAM output requires a written observation, not just the
image gallery. After generating the heatmap gallery, write 3-5
sentences in `docs/model_metrics.md` describing what was actually
observed (does the model attend to lesions, or to
background/edges?) — including if the finding is mixed or
negative.

## Model and export

- `target_layer` for Grad-CAM is `model.features[-1]` for EfficientNet-B0 — don’t change this without updating the docstring explanation
in `gradcam.py` of why a different layer was chosen.
- ONNX export must include the sanity-check inference pass
(already in `export.py`) confirming the output shape matches
`num_classes`. Don’t skip this step even if the export command
appears to succeed.
