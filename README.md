# Max-Python-AI-Gen-001

**GitHub:** https://github.com/djDAOjones/Max-Python-AI-Gen-001

AI-driven Max/MSP patch generator for real-time screen region capture and dithering preview using MaxPy.

## Overview

This project uses MaxPy (a Python metaprogramming library for Max/MSP) to generate patches that:
- Capture a screen region in real-time
- Apply dithering algorithms
- Preview the dithered output continuously inside Max/MSP

**Goal:** Build a real-time dithering preview tool without compiled externals (v1).

## Environment

- **Platform:** macOS 15.6.1+
- **Max/MSP:** 8.6.5
- **Python:** 3.10.13 (in venv)
- **License:** MIT

## Setup

### 1. Install Dependencies

```bash
# Activate virtual environment
source venv/bin/activate

# Verify MaxPy installation
python test_maxpy.py
```

### 2. MaxPy Installation (Already Done)

MaxPy was installed from GitHub (not PyPI) with manual fixes:

```bash
# Original installation
pip uninstall -y maxpy
git clone https://github.com/Barnard-PL-Labs/MaxPy.git
cp -r MaxPy/maxpy venv/lib/python3.10/site-packages/

# Dependencies
pip install tabulate numpy==1.22.3 sphinx_rtd_theme
```

## Usage

### Test MaxPy

```bash
python test_maxpy.py
```

This creates `hello_world.maxpat` - a simple sine wave patch.

### Create Your Own Patch

```python
import maxpy as mp

patch = mp.MaxPatch()
osc = patch.place("cycle~ 440")[0]
dac = patch.place("ezdac~")[0]
patch.connect([osc.outs[0], dac.ins[0]])
patch.save("my_patch.maxpat")
```

## MaxPy Syntax Reference

**Placing Objects:**
```python
obj = patch.place("object_name")[0]  # Returns list, get first element
objs = patch.place("object", num_objs=5)  # Create multiple
```

**Connecting Objects:**
```python
patch.connect([source.outs[0], dest.ins[0]])
```

**Multiple Connections:**
```python
for s, d in zip(sources, dests):
    patch.connect([s.outs[0], d.ins[0]])
```

## Project Structure

```
Max-Python-AI-Gen-001/
├── venv/                   # Python virtual environment
├── test_maxpy.py          # MaxPy test script
├── hello_world.maxpat     # Generated test patch
├── install_correct_maxpy.sh
└── README.md
```

## Development Notes

### MaxPy Installation Issues Resolved

1. **Wrong Package:** PyPI's `maxpy` is for approximate computing, not Max/MSP
2. **Solution:** Installed from GitHub: `Barnard-PL-Labs/MaxPy`
3. **Missing Files:** Manually created `tools/` module files
4. **Dependencies:** Added `tabulate` and other requirements

### Key Learnings

- Use `source venv/bin/activate` before running scripts
- `place()` returns a list - use `[0]` to get the object
- Connections use `.outs[]` and `.ins[]` attributes
- Always work in the venv to ensure correct dependencies

## Resources

- [MaxPy GitHub](https://github.com/Barnard-PL-Labs/MaxPy)
- [MaxPy Documentation](https://barnard-pl-labs.github.io/MaxPy/)
- [MaxPy Examples](https://github.com/Barnard-PL-Labs/MaxPy/tree/main/examples)

## Next Steps

1. Build screen capture object integration
2. Implement dithering algorithms (Floyd-Steinberg, Ordered, Atkinson, Threshold)
3. Create real-time preview interface
4. Test with Max/MSP 8.6.5

## Status

- ✅ MaxPy environment setup complete
- ✅ Test patch generation working
- ⏳ Screen capture implementation
- ⏳ Dithering algorithms
- ⏳ Real-time preview

---

**Last Updated:** 2025-01-19  
**Maintainer:** djDAOjones
