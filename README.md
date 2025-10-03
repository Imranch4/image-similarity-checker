# image-similarity-checker

# 🖼️ image-similarity-checker

A Python tool to compare two images and measure their similarity using three powerful methods: **Perceptual Hash (pHash)**, **Structural Similarity Index (SSIM)**, and **ORB Feature Matching**.

---

## 🚀 Introduction

**image-similarity-checker** is a lightweight Python utility designed for fast and reliable image comparison. Whether you're working on duplicate detection, image recognition, or automated testing, this tool provides multiple techniques to analyze and quantify image similarity.

---

## ✨ Features

- **Perceptual Hash (pHash):** Robust to minor changes and noise, ideal for detecting visually similar images.
- **Structural Similarity Index (SSIM):** Measures perceived change in structural information between two images.
- **ORB Feature Matching:** Detects and matches keypoints for advanced similarity analysis.
- **Easy to use:** Simple command-line interface and modular code.
- **Open Source:** MIT licensed for commercial and personal projects.

---

## ⚡ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/image-similarity-checker.git
    cd image-similarity-checker
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    **Required packages:**
    - Pillow
    - imagehash
    - opencv-python
    - numpy
    - scikit-image

---

## 🛠️ Usage

Compare two images using all methods:

```bash
python image-similarity.py --img1 path/to/image1.jpg --img2 path/to/image2.jpg
```

**Options:**
- `--img1` : Path to the first image.
- `--img2` : Path to the second image.

**Sample Output:**
```
pHash Similarity: 94%
SSIM Score: 0.87
ORB Match Score: 120 matches
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open a [pull request](https://github.com/yourusername/image-similarity-checker/pulls) or [issue](https://github.com/yourusername/image-similarity-checker/issues).

**Recommended steps:**
1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **Made with ❤️ in Python**

---

**Links:**  
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [imagehash](https://pypi.org/project/ImageHash/)
- [OpenCV](https://opencv.org/)
- [scikit-image](https://scikit-image.org/)

---

_If you find this project useful, please ⭐ star the repo!_

## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/Imranch4/image-similarity-checker
