#!/usr/bin/env python
"""
Panda3D Particles Demo Launcher
Launches the particle effects demo (steam_example.py) by default.
"""
import runpy

if __name__ == "__main__":
    runpy.run_module("steam_example", run_name="__main__")
