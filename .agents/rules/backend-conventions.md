# Rule: Backend and agent conventions

Applies to anything under `backend/`.

## API contracts

- Every endpoint’s request/response shape is a Pydantic model in
`backend/models/schemas.py`, not a loose dict. This is a small thing
that reads as meaningfully more professional in code review —
don’t skip it for speed.
- `/diagnose`, `/advise`, `/chat` are the three core endpoints. If you add a
new one, document its contract in the same style (see existing spec
for the JSON shape of each) before implementing it.
- Add a lightweight `/health` endpoint (return `{"status": "ok"}`) that
does not trigger a model load — this exists specifically so the free-tier keep-alive ping (UptimeRobot) has something cheap to hit.

## LangGraph agent

- The planner node’s branching must be grounded in real domain
logic: disease category (fungal/bacterial/viral/nutritional)
determines whether the weather tool gets called, because spray
timing relative to rain only matters for some disease types. Don’t
add branches that don’t correspond to an actual decision a domain
expert would make — branching for the sake of looking like a
graph defeats the point.
- Weather tool failures must degrade gracefully: wrap the
OpenWeatherMap call in try/except, set the state field to None on
failure, and make sure the synthesizer’s prompt produces a
complete, useful response either way (it should just omit the rain-timing note rather than failing the whole request).
- Cost estimation in the advisory output must never present a fake-precise number. Use a wide range and always append a disclaimer
sentence directing the user to confirm with a local agro-dealer —
this is a one-sentence prompt addition, handle it in the synthesizer
prompt template, not as a separate feature.

## RAG

- Build the FAISS index at deploy/startup time
(`backend/rag/build_index.py` runs as part of the build step), never
commit the binary index file to the repo.
- Keep the advisory document corpus at 10-20 curated documents. If
asked to expand it significantly, flag that this changes the project’s
“curated, defensible corpus” story before doing it.

## Deployment

- The `/health` endpoint and any keep-alive documentation belongs in
the README’s deployment section, stated plainly (e.g. “kept warm
via scheduled health checks; first request after extended inactivity
may still take a few seconds”) rather than implying flawless
uptime.
