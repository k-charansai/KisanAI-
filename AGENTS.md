# AGENTS.md — KisanAI

This file is read by every agent before it starts work in this project.
Treat it as binding context, not a suggestion. If a request from the
user conflicts with something here, flag the conflict before proceeding
rather than silently picking one side.

## What this project is

KisanAI is a crop disease diagnosis tool: a user uploads a leaf photo, a
fine-tuned EfficientNet-B0 model identifies the disease, Grad-CAM
shows which pixels drove that prediction, and a LangGraph agent
turns the diagnosis into a treatment plan using weather context and a
small curated knowledge base.

## Who this is for and why that matters

This is a final-year CS student’s portfolio project, built to be the
strongest possible signal in a screening round for AI-focused startup
roles (target: 7-10 LPA in India). That single fact should shape almost
every judgment call you make. Two consequences worth internalizing:

1. **Credibility beats raw numbers.** An honest 87% lab accuracy
with a documented 65% field-accuracy drop on a second dataset is
a stronger artifact than an unqualified “98% accuracy” claim,
because the former survives a technical interviewer’s first follow-up question and the latter doesn’t. Never let a metric ship without
the caveat that makes it true.
2. **Demonstrated skill beats production-optimal engineering.** Where there’s a genuine tension between “the cleanest way to
build this” and “the way that best demonstrates a skill this
candidate needs to show,” default to the latter — but say so
explicitly in the relevant code comment or plan artifact, don’t bury
the tradeoff.

## Non-negotiable architectural decisions (do not silently revise these)

These were deliberated already, including a round of external review.
If you think one is wrong, raise it as a question — don’t just build
something different.

- **Keep LangGraph for the advisory agent**, even though a vanilla
Python function pipeline would be objectively simpler and more
maintainable for this exact use case. The point of this project is to
demonstrate agentic orchestration skill for AI-startup hiring. The
planner node’s branching must be real (it branches on disease
category — fungal/bacterial/viral/nutritional — not decoratively),
not a single fixed path dressed up as a graph.
- **EfficientNet-B0**, transfer learning via freeze-then-unfreeze
staged fine-tuning. Not a from-scratch architecture. Be precise
about this distinction in any documentation or resume-facing text
— overclaiming “trained a model from nothing” is the kind of detail
that loses credibility under questioning.
- **Grad-CAM is required, not optional.** It directly answers a
documented failure mode of PlantVillage-trained models
(background bias — the model can learn to associate background
characteristics with disease labels rather than actual lesions). Every diagnosis the deployed app returns must include a Grad-CAM overlay, not just a notebook demo.
- **Field validation on PlantDoc is required**, evaluated with the
same checkpoint, no retraining. Expect and report a real accuracy
drop (60-75% is a normal, defensible range for this domain shift)
rather than treating it as a failure to fix.
- **Class-weighted loss** for training, to correct PlantVillage’s real
imbalance (Tomato ~18k images vs Raspberry ~371).
- **RAG corpus stays small (10-20 curated documents)**, built into
FAISS at deploy time rather than committed as a binary index file.
Don’t expand this into a large scraped corpus — quality and
defensibility over volume.
- **Free-tier deployment with a free keep-alive workaround**
(UptimeRobot pings against a lightweight /health endpoint), not
paid hosting. Document the limitation honestly in the README
rather than hiding it.

## Honesty requirements (apply to every artifact you produce)

- Never write a metric, accuracy number, or capability claim into
README.md, docs/model_metrics.md, or any resume-facing text
unless it was actually produced by running the code. Placeholder
numbers must be marked as `[TODO: fill in after training]`, never
invented or estimated.
- If a result is worse than hoped (e.g. low field accuracy, a class with
poor F1), report it plainly with a one-sentence explanation rather
than omitting it or softening it into vagueness.
- `PRIVACY_NOTE.md` must stay a single honest paragraph (see existing
file once created) — do not expand it into a compliance program.
This is a portfolio demo, not a product with real users; say so.

## Tech stack

- **ML**: PyTorch, torchvision, scikit-learn, ONNX/ONNX Runtime for
inference export
- **Backend**: FastAPI, LangGraph, Gemini 1.5 Flash, FAISS
- **Frontend**: React (MERN stack — the candidate is actively learning this, so React serves double duty as portfolio skill + project frontend). Deploy to Vercel. Add CORS middleware to FastAPI backend to allow requests from the Vercel domain.
- **Deployment**: Render (backend), Streamlit Community Cloud
(frontend)

## Repository structure

```
kisanai/
├── AGENTS.md                  # this file
├── PRIVACY_NOTE.md
├── README.md
├── ml/                        # vision model: data, training, eval, Grad-CAM, export
├── backend/                   # FastAPI + LangGraph agent + RAG
├── frontend/                  # React app (Vite + React, deployed to Vercel)
└── docs/                      # model_metrics.md, architecture diagram, demo assets
```
Full structure detail lives in `docs/architecture.md` once generated —
don’t ask the user to repeat it, read that file.

## Working conventions

- **Always plan before implementing.** For anything beyond a one-line fix, produce a Task List and Implementation Plan artifact first
and wait for explicit approval before writing code. This project
moves in weekly phases (see the build sequence below) — don’t
jump ahead to backend work while the vision model phase is still
open, even if it seems faster to parallelize.
- **Python**: PEP 8, type hints on function signatures, docstrings on
every public function explaining why a non-obvious choice was
made (not just what the code does — the existing `ml/src/` files are
the reference style for this).
- **No magic numbers.** Hyperparameters (learning rates, epoch
counts, thresholds) are named constants or CLI arguments, never
bare literals.
- **Every training/eval run that produces a number must print
or save that number to a file** (`training_summary.json`,
`docs/model_metrics.md`, etc.) — don’t let results live only in a
terminal scrollback the user has to copy by hand.
- **Never commit**: raw datasets, model checkpoints (`.pt`, `.onnx`), `.env`
files, or the FAISS binary index. `.gitignore` already covers these —
extend it, don’t bypass it.
- **Ask before assuming when a Kaggle/GitHub dataset’s
structure doesn’t match what’s documented.** Dataset mirrors
change. If a download script’s sanity check fails (wrong class
count, missing folders), stop and report the discrepancy rather
than guessing a workaround.

## Build sequence (current phase tracking)

Update this checklist as phases complete — it’s how a new agent
session knows where the project actually stands, since Antigravity
doesn’t carry memory between sessions.

- [x] **Phase 1 — Vision model core**: dataset download, EDA (including
near-duplicate check via perceptual hashing and class distribution
analysis), training with class-weighted loss, PlantVillage
evaluation, Grad-CAM gallery
- [x] **Phase 2 — Field validation + export**: PlantDoc download and
class-name mapping, field accuracy evaluation, ONNX export, full
`docs/model_metrics.md` writeup
- [x] **Phase 3 — Backend + agent**: FastAPI skeleton, vision service
(with Grad-CAM at inference time), LangGraph agent with disease-category planner branching, weather tool with explicit failure
handling, RAG built at deploy time
- [x] **Phase 4 — Frontend + deploy**: React frontend (image upload component, diagnosis + Grad-CAM overlay results panel, follow-up chat component), backend on Render, frontend on Vercel, UptimeRobot keep-alive on `/health` endpoint. Do NOT start frontend until FastAPI backend is deployed and all three endpoints return real responses.
- [x] **Phase 5 — Polish**: demo GIF, architecture diagram, final
README pass confirming every claimed number matches
`docs/model_metrics.md`

Do not start a phase until the previous one’s required deliverables
exist on disk. If the user asks to skip ahead, surface that this breaks
the dependency chain (e.g. the backend’s vision_service needs a real
ONNX checkpoint, not a stub) before proceeding.
