# Base64 Icon Studio 🖼️

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
## 🤝 Contributing
Contributions are welcome! If you'd like to add features (like image resizing or batch processing), feel free to fork the repo and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
