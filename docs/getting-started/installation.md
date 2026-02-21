# Installation

Detailed installation instructions for each platform component.

---

## Core Requirements

All Vindicta components require:

- **Python 3.10+** (for backend components)
- **Node.js 18+** (for UI components)
- **uv** (recommended package manager)

### Installing uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Component Installation

### The Engine (Physics & Simulation)

The simulation engine and back-end logic layer:

```bash
git clone https://github.com/vindicta-platform/vindicta-engine.git
cd vindicta-engine
uv sync
```

### The Platform (Web & Identity)

The unified web interface and user entry point:

```bash
git clone https://github.com/vindicta-platform/vindicta-platform.git
cd vindicta-platform
npm install
```

### Individual Modules

Each module can be installed independently:

```bash
# Core Platform
uv pip install git+https://github.com/vindicta-platform/vindicta-foundation.git
uv pip install git+https://github.com/vindicta-platform/vindicta-engine.git

# Logic & Data
uv pip install git+https://github.com/vindicta-platform/warscribe-system.git
uv pip install git+https://github.com/vindicta-platform/vindicta-economy.git
uv pip install git+https://github.com/vindicta-platform/vindicta-oracle.git
```

---

## Verification

Verify your installation:

```bash
# Check CLI equivalent (if installed)
# vindicta --version

# Run tests
pytest tests/ -v
```

---

## Troubleshooting

### uv lock file issues

```bash
uv cache clean
rm uv.lock
uv sync
```

### Port already in use

```bash
# Find process on port 8000
lsof -i :8000
# or on Windows
netstat -ano | findstr :8000
```
