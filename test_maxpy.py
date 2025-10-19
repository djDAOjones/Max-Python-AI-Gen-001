#!/usr/bin/env python
"""Test MaxPy installation and create a simple patch"""

import sys
print("Python path:")
for p in sys.path:
    print(f"  {p}")

print("\nTrying to import maxpy...")
try:
    import maxpy as mp
    print("✓ Successfully imported maxpy")
    
    # Create a simple test patch
    patch = mp.MaxPatch()
    osc = patch.place("cycle~ 440")[0]  # place() returns a list
    dac = patch.place("ezdac~")[0]
    # Connect using .outs[] and .ins[] attributes
    patch.connect([osc.outs[0], dac.ins[0]])
    patch.save("hello_world.maxpat")
    print("✓ Created hello_world.maxpat")
    
except ImportError as e:
    print(f"✗ Failed to import maxpy: {e}")
    print("\nChecking site-packages directory...")
    import os
    site_packages = "/Users/joe/Library/CloudStorage/OneDrive-OurWiltonTrust/Jen and Jones/2023-08-11 Dithering Research/Windsurf Projects/realtime-dithering-001/venv/lib/python3.10/site-packages"
    if os.path.exists(site_packages):
        items = os.listdir(site_packages)
        maxpy_items = [item for item in items if 'max' in item.lower()]
        print(f"MaxPy-related items: {maxpy_items}")
