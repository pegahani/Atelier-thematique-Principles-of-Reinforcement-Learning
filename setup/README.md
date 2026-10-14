# Setup for the RL atelier

We work **locally**, on your own computer (CPU only, no GPU needed), from Session 1 on.
Please do this setup **before Session 1** and run `check_setup.ipynb`. It takes about 15 minutes.

If something fails, don't worry:

- For **Session 1**, you only need `pip install gymnasium numpy matplotlib jupyterlab` (no PyTorch, no Box2D).
- Bring the error message to Session 2, we fix it together.

## Why a virtual environment?

A **virtual environment** is a folder (here `.venv`) that holds its own copy of Python and its own packages.
Everything for this course is installed inside it, so:

- it does not break the Python of your system or of your other courses,
- everyone in the course has the same package versions,
- if something goes wrong, you delete the `.venv` folder and start again.

You **activate** the environment each time you open a new terminal to work on the course.
When it is active, your terminal prompt starts with `(.venv)`.

## Get the course files

All the course material is on GitHub: <https://github.com/pegahani/Atelier-thematique-Principles-of-Reinforcement-Learning>

- **With git** (recommended), in a terminal:
  ```bash
  git clone https://github.com/pegahani/Atelier-thematique-Principles-of-Reinforcement-Learning.git
  cd Atelier-thematique-Principles-of-Reinforcement-Learning
  ```
  Before each session, get the new material with `git pull` (inside that folder).
- **Without git**: on the GitHub page, *Code → Download ZIP*, then unzip it.
  You will need to download it again before each session.

Each session has its own folder (`session-1/`, `session-2/`, …). Create your virtual environment **once**,
at the top of the course folder (next to this `setup/` folder), and use it for all sessions.

## Open a terminal

All the commands below are typed in a terminal:

- **macOS**: open the *Terminal* app (Cmd + Space, type "Terminal").
- **Windows**: open *PowerShell* (Start menu, type "PowerShell").
- **Linux**: Ctrl + Alt + T on most distributions.

Then go to the course folder with `cd`, for example `cd Documents/Atelier-thematique-Principles-of-Reinforcement-Learning`.
`ls` (macOS / Linux) or `dir` (Windows) lists the files: you should see `setup/` and `session-1/`.
**All the commands below are run from this folder.**

## Requirements

- Python **3.10, 3.11, 3.12 or 3.13** (3.12 recommended).
  **Python 3.14 does not work yet**: `box2d` (needed for LunarLander) has no prebuilt package for it.
- About 1.5 GB of free disk space (mostly PyTorch).
- No GPU needed.

## Option A (recommended): `uv`

[`uv`](https://docs.astral.sh/uv/) is a fast Python package manager. It downloads the right Python version
for you, so it works the same on Windows, macOS and Linux.

1. Install uv:
   - **macOS / Linux**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - **Windows** (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

   Then close and reopen your terminal.

2. Create and activate the environment, in the course folder:
   ```bash
   uv venv --python 3.12 .venv
   ```
   - **macOS / Linux**: `source .venv/bin/activate`
   - **Windows** (PowerShell): `.venv\Scripts\activate`

3. **Linux only**: install the CPU build of PyTorch first (the default one comes with ~3 GB of GPU libraries):
   ```bash
   uv pip install torch --index-url https://download.pytorch.org/whl/cpu
   ```

4. Install everything else (all systems):
   ```bash
   uv pip install -r setup/requirements.txt
   ```

5. Start Jupyter and open `setup/check_setup.ipynb`:
   ```bash
   jupyter lab
   ```
   Next time, you only need to activate the environment (step 2, second line) and run `jupyter lab`.

## Option B: you already have Python 3.10–3.13

No extra tool needed. Check your version first with `python3 --version` (macOS / Linux) or `py --version` (Windows).

- **macOS / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- **Windows** (PowerShell):
  ```bash
  py -3.12 -m venv .venv
  .venv\Scripts\activate
  ```

Then, with the environment active:
```bash
# Linux only:
pip install torch --index-url https://download.pytorch.org/whl/cpu
# all systems:
pip install -r setup/requirements.txt
jupyter lab
```

## Option C: conda / miniforge

```bash
conda create -n rl python=3.12 -y
conda activate rl
# Linux only:
pip install torch --index-url https://download.pytorch.org/whl/cpu
# all systems:
pip install -r setup/requirements.txt
jupyter lab
```

## Option D: VS Code

Create the environment with option A, B or C, open the course folder in VS Code, install the *Jupyter* extension,
and select `.venv` (or `rl`) as the kernel at the top right of the notebook.

## Common problems

| Symptom | Fix |
|---|---|
| `error: command 'swig' failed` or `Failed building wheel for box2d` | Your Python is too recent (3.14) or too old. Recreate the environment with Python 3.12 (`uv venv --python 3.12 .venv`). |
| pip downloads `nvidia-...` packages (Linux) | Stop it, then install torch with `--index-url https://download.pytorch.org/whl/cpu` first (step 3). |
| `ModuleNotFoundError` in Jupyter but the package is installed | The notebook uses another kernel. Select `.venv` / `rl` as the kernel. |
| Windows: `uv` is not recognised | Close and reopen the terminal after installing uv. |
| Windows: `running scripts is disabled on this system` when activating | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once in PowerShell, then activate again. |
| Download interrupted or very slow (PyTorch is ~200 MB) | Run the same command again: already downloaded packages are not downloaded twice. |
