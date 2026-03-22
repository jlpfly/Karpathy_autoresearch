# Training Output Explained in Plain English

This file explains what you are seeing when `uv run train.py` is running.

Short version: the model is doing lots of tiny "practice tests" on text. It guesses the next token, gets graded, adjusts its internal weights a little bit, and repeats that cycle for about 5 minutes.

In an interactive terminal, the live training area now uses **two lines**:

- the top line shows the raw metrics
- the bottom line shows the plain-English helper words for those metrics

## The big picture

Think of training like this:

1. The model reads a tiny chunk of text.
2. It tries to guess what comes next.
3. The code measures how wrong the guess was.
4. The model nudges its "brain" a little so it will do better next time.
5. That loop repeats hundreds of times.

So the terminal output is basically a live scoreboard for that practice session.

## Part 1: The startup summary at the top

Before the scrolling `step ...` line starts, the script prints a quick "about this run" summary.

Example:

```text
wte                     : 1,048,576
value_embeds            : 2,097,152
lm_head                 : 1,048,576
transformer_matrices    : 3,145,984
scalars                 : 8
total                   : 7,340,296
Estimated FLOPs per token: 3.145882e+07
Scaling AdamW LRs by 1/sqrt(256/768) = 1.732051
Skipping torch.compile because Triton is not installed; running model and optimizer in eager mode.
Time budget: 300s
Gradient accumulation steps: 2
```

### What those startup lines mean

| Output | What it means | Dummy-speak |
| --- | --- | --- |
| `wte` | Token embedding weights | "The table that gives each token its starting meaning." |
| `value_embeds` | Extra value embedding weights used by attention | "Extra memory pieces the model uses while thinking about the text." |
| `lm_head` | Final output layer | "The part that turns the model's thoughts into its next guess." |
| `transformer_matrices` | Main matrix weights in the network | "Most of the model's actual brain." |
| `scalars` | A few small learned numbers | "Tiny adjustment knobs." |
| `total` | Total number of trainable parameters | "How big the model's brain is overall." |
| `Estimated FLOPs per token` | Rough amount of math per token | "How much calculator work each tiny piece of text costs." |
| `Scaling AdamW LRs ...` | The optimizer is scaling learning rates for this model size | "The script is setting how hard the model should try to learn each step." |
| `Skipping torch.compile ... eager mode` | A compile-time speedup is unavailable, so PyTorch runs in normal mode | "Turbo mode is off, but normal driving still works." |
| `Time budget: 300s` | Timed training will run for about 5 minutes | "This practice session lasts 5 minutes." |
| `Gradient accumulation steps: 2` | The script combines 2 mini-batches before each optimizer update | "It looks at two small study packets before making one real correction." |

## Part 2: The live training display

This is the two-line area that keeps updating while the run is active:

```text
step: 00369 | done:  35.0% | loss: 2.372307 | lrm: 1.00 | dt:  296ms | tok/sec: 110,832 | mfu: 8.7% | epoch: 1 | remaining: 195s
study round | run done | wrongness | learning pace | time for 1 study | text speed | GPU busy | data lap | time left
```

The first line is the live scoreboard.

The second line is the built-in plain-English legend.

### What each live metric means

| Column | What it means | Dummy-speak |
| --- | --- | --- |
| `step: 00369` | The 369th training update | "The model has finished 369 study rounds." |
| `done: 35.0%` | Percent of the timed training budget that is done | "We are about one-third finished." |
| `loss: 2.372307` | Current training error; lower is usually better | "How wrong the model still is right now. Lower is better." |
| `lrm: 1.00` | Learning-rate multiplier | "How hard the model is pressing the gas pedal while learning." |
| `dt: 296ms` | Time taken for that step | "One study round took about 0.3 seconds." |
| `tok/sec: 110,832` | Tokens processed per second | "How fast the laptop is chewing through text." |
| `mfu: 8.7%` | Model FLOPs utilization | "A rough score for how much of the GPU's math power is actually getting used." |
| `epoch: 1` | Current pass through the training data | "We are still in the first full lap through the dataset." |
| `remaining: 195s` | Estimated time left in the 5-minute budget | "About 3 minutes and 15 seconds left." |

### What the second line's helper words mean

| Helper word | Refers to | Plain meaning |
| --- | --- | --- |
| `study round` | `step` | How many update rounds have happened |
| `run done` | `done` | How far through the timed run you are |
| `wrongness` | `loss` | How wrong the model currently is |
| `learning pace` | `lrm` | How strong the learning-rate schedule is right now |
| `time for 1 study` | `dt` | How long one training update took |
| `text speed` | `tok/sec` | How fast text is being processed |
| `GPU busy` | `mfu` | Roughly how hard the GPU is being worked |
| `data lap` | `epoch` | Which pass through the dataset you are on |
| `time left` | `remaining` | Approximate time remaining in the 5-minute budget |

## Part 3: What is actually happening during those 5 minutes?

Every step is basically this:

1. Grab a small batch of tokenized text.
2. Ask the model to predict the next token for each position.
3. Compare the guesses to the real answers.
4. Calculate `loss`, which is the "how wrong were we?" score.
5. Send that error backward through the network so the model knows what to adjust.
6. Update the weights a tiny bit.
7. Repeat until the timer runs out.

So if the line keeps updating, the model is actively studying, getting graded, and correcting itself over and over.

## Part 4: How to read the live display like a normal person

If you do not care about the technical details, here is the simple way to watch the run:

- `step` should keep going up.
- `%` should keep going up until it reaches `100%`.
- `remaining` should keep going down to `0s`.
- `loss` should usually drift downward over time, though small jumps are normal.
- `tok/sec` tells you how fast the run is going.
- `mfu` tells you how busy the GPU is.
- the second line is just a human-friendly label row; it should stay the same while the numbers above it change

### What is normal?

- `loss` bouncing up and down a little is normal.
- `dt` changing a bit is normal.
- `tok/sec` changing a bit is normal.
- `mfu` being much lower than `100%` is normal on a smaller laptop GPU.

### What is not normal?

- The script prints `FAIL`
- The run crashes with a CUDA out-of-memory error
- The step line stops updating for a long time and never finishes

## Part 5: The final summary block

At the end, the script prints a scorecard like this:

```text
---
val_bpb:          0.652241
training_seconds: 300.3
total_seconds:    312.3
peak_vram_mb:     2033.6
mfu_percent:      8.02
total_tokens_M:   30.9
num_steps:        944
num_params_M:     7.3
depth:            4
```

### What the final lines mean

| Output | What it means | Dummy-speak |
| --- | --- | --- |
| `val_bpb` | Validation bits per byte; lower is better | "The final test score on text the model did not train on. Lower is better." |
| `training_seconds` | Time spent in the timed training loop | "How long the real practice session lasted." |
| `total_seconds` | Total wall-clock time, including setup and final evaluation | "How long you waited in real life from start to finish." |
| `peak_vram_mb` | Peak GPU memory used | "The most video memory the run needed." |
| `mfu_percent` | Average model FLOPs utilization over the run | "How hard the run kept the GPU working, on average." |
| `total_tokens_M` | Total tokens processed, in millions | "How much text the model studied." |
| `num_steps` | Total number of training updates | "How many study rounds happened." |
| `num_params_M` | Model size in millions of parameters | "How big the model's brain is." |
| `depth` | Number of transformer layers | "How many stacked thinking layers are inside the model." |

## One-sentence cheat sheet

If you want the whole thing in one sentence:

> The terminal is showing how far through the 5-minute practice session the model is, how wrong it still is, how fast your laptop is processing text, how busy the GPU is, and what the final score looked like at the end.

## Super-short cheat sheet

- `loss` = wrongness
- `tok/sec` = speed
- `remaining` = time left
- `val_bpb` = final score
- lower `loss` and lower `val_bpb` are good

