# Base64 Icon Studio 🖼️

⚠️ **LICENSE & USAGE NOTICE — READ FIRST**

This repository is **source-available for private technical evaluation and testing only**.

- ❌ No commercial use  
- ❌ No production use  
- ❌ No academic, institutional, or government use  
- ❌ No research, benchmarking, or publication  
- ❌ No redistribution, sublicensing, or derivative works  
- ❌ No independent development based on this code  

All rights remain exclusively with the author.  
Use of this software constitutes acceptance of the terms defined in **LICENSE.txt**.

---

A lightweight, desktop utility built with Python to instantly convert images into Base64 Data URIs. Perfect for web developers and UI designers who want to embed icons directly into CSS, HTML, or JSON files without managing external assets.

## ✨ Features
- Drag & Drop: Simply drop any image file onto the interface to encode it.
- Smart Mime-Types: Automatically detects file extensions (.png, .jpg, .svg, .ico, etc.) to generate the correct Data URI header.
- Encoding History: Maintains a list of the last 10 encoded items—double-click any item to re-copy it.
- Dual Mode: * GUI: User-friendly window for visual workflow.
    - CLI: Headless mode for quick terminal usage.
- Clipboard Integration: One-click copying to your system clipboard.
- Auto-Save: Automatically saves the latest result to encoded_output.txt as a fallback.

## 🚀 Installation

1. Clone the repository
```Bash
git clone https://github.com/yourusername/base64-icon-studio.git
cd base64-icon-studio
```
2. Install Dependencies
This project requires tkinterdnd2 for the drag-and-drop functionality:

```Bash
pip install tkinterdnd2
```
Note: Standard tkinter is usually included with Python. If you are on Linux, you may need to install python3-tk via your package manager.

## 🛠️ Usage

Graphical Interface (Recommended)

Run the script without arguments to launch the GUI:
```Bash
python encode_icon.py
```
Command Line Interface

Pass a file path as an argument to get the Base64 string printed directly to your terminal:
```Bash
python encode_icon.py path/to/your/icon.png
```

---
## 📂 Supported Formats

The Studio handles all common web formats, including:
- Raster: .png, .jpg, .jpeg, .gif, .ico
- Vector: .svg

## 📝 Technical Details
- Core Library: base64 for encoding.
- GUI Framework: Tkinter + TkinterDnD2.
- Output Format: data:<mime_type>;base64,<encoded_data>

---
## Contribution Policy

Feedback, bug reports, and suggestions are welcome.

You may submit:

- Issues
- Design feedback
- Pull requests for review

However:

- Contributions do not grant any license or ownership rights
- The author retains full discretion over acceptance and future use
- Contributors receive no rights to reuse, redistribute, or derive from this code

---

## License
This project is not open-source.

It is licensed under a private evaluation-only license.
See LICENSE.txt for full terms.
