# Kickoff prompt — paste this into Antigravity’s agent chat to start Phase 1

Use Planning mode for this. Don’t write any code yet.

Read AGENTS.md and .agents/rules/ml-conventions.md fully before
doing anything else. This is a fresh project — there’s no existing code
in ml/ yet, so you’re building from scratch, but the architecture,
conventions, and constraints in AGENTS.md are already decided and
not open for silent revision.

Your task: build out Phase 1 of the build sequence in AGENTS.md —
the vision model core. Concretely, that means:

1. A dataset download script that pulls PlantVillage from Kaggle, with
a sanity check that reports the class count found (should be 38)
and fails loudly with a clear message if the structure looks wrong.
2. An EDA notebook that includes: class distribution analysis
(PlantVillage has a real imbalance — Tomato ~18k images vs
Raspberry ~371 — make this visible), and a near-duplicate check
using perceptual hashing (the imagehash library) to quantify how
much near-duplication exists in the dataset, since the train/val split
is image-level rather than leaf-level and this number needs to be
reported honestly in the eventual model_metrics.md.
3. A PyTorch Dataset class with separate train (augmented) and eval
(clean) transform pipelines.
4. An EfficientNet-B0 model setup using transfer learning: freeze the
backbone, train the head, then unfreeze the last two feature blocks
and fine-tune at a lower learning rate. Use named constants for the
hyperparameters, not bare literals — and print them at the start of
each run.
5. A training script that computes class weights from the training
split (inverse-frequency weighting) and uses them in the loss
function to correct for the imbalance found in step 2.
6. An evaluation script that produces the confusion matrix, per-class
precision/recall/F1, and explicitly surfaces the most-confused class
pairs — not just an overall accuracy number.
7. A Grad-CAM implementation targeting model.features[-1], usable
both from a notebook (for the sample gallery) and importable into
a backend service later — keep it dependency-light, no heavy
plotting libraries baked into the core implementation.

Before writing any code, produce a Task List and Implementation Plan
covering: the exact file structure you’ll create under ml/, the order
you’ll build things in, and any open questions (for example, if you’re
unsure about a specific hyperparameter default, ask rather than
guessing). I’ll review and approve before you start implementation.

One constraint to hold onto throughout: every number this phase
produces (validation accuracy, per-class F1, the near-duplicate
percentage, the Grad-CAM observations) needs to end up written to a
file, not just printed to a terminal I’d have to copy by hand. Plan for
where each of those numbers lands before you start coding.
