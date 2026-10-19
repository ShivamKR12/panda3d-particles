# Panda3D Particles Showcase & Tutorials

A collection of 3D particle systems and demos built using the [Panda3D](https://www.panda3d.org/) game engine in Python.

It demonstrates built-in physics-based sprite particles configured through `.ptf` files, an interactive GUI particle editor panel, and an advanced GPU shader-driven particle system.

## ✨ Demos Included

### 1. Physics Particle System (`steam_example.py` / `main.py`)
Loads preconfigured particle effects from `.ptf` files using Panda3D's built-in physics and particle factory (`PointParticleFactory`, `SpriteParticleRenderer`, `LinearNoiseForce`, `DiscEmitter`).

**Controls:**
- **1**: Load Steam (`steam.ptf`)
- **2**: Load Dust (`dust.ptf`)
- **3**: Load Fountain (`fountain.ptf`)
- **4**: Load Smoke (`smoke.ptf`)
- **5**: Load Smokering (`smokering.ptf`)
- **6**: Load Fireish (`fireish.ptf`)
- **Esc**: Quit

### 2. Advanced GPU Shader Particles (`advanced.py`)
Demonstrates an inertial particle system computed entirely on the GPU using modern GLSL 1.50 shaders with `imageBuffer` texture storage (`GL_ARB_shader_image_load_store`) and rotating teapot emitter.

**Controls:**
- **Left / Right Arrow**: Rotate emitter teapot
- **Esc**: Quit

### 3. Particle Panel Editor (`particle_panel.py`)
Launches Panda3D's interactive Tkinter-based visual particle panel (`direct.tkpanels.ParticlePanel`) for real-time authoring and tweaking of particle systems.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ installed.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShivamKR12/panda3d-particles.git
   cd panda3d-particles
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the particle demo:
   ```bash
   python main.py
   ```

4. Or run the advanced GPU shader simulation:
   ```bash
   python advanced.py
   ```

## 🛠️ Credits & Tech Stack

- **Game Engine**: [Panda3D](https://www.panda3d.org/)
- **Language**: Python 3
- **Shaders**: GLSL (OpenGL 3.2+)
- **Original Samples**: Phil Saltzman, Shao Zhang & Panda3D contributors
