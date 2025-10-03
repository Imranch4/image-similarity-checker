from PIL import Image
import imagehash
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def phash_compare(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    hash1 = imagehash.phash(img1)
    hash2 = imagehash.phash(img2)
    diff = hash1 - hash2
    return diff

def ssim_compare(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    h = min(img1.shape[0], img2.shape[0])
    w = min(img1.shape[1], img2.shape[1])
    img1 = cv2.resize(img1, (w, h))
    img2 = cv2.resize(img2, (w, h))

    score, _ = ssim(img1, img2, full=True)
    return score

def orb_match(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return 0

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    return len(matches)

if __name__ == "__main__":
    img1 = "before.jpg"
    img2 = "after.jpg"

    phash_diff = phash_compare(img1, img2)
    ssim_score = ssim_compare(img1, img2)
    orb_matches = orb_match(img1, img2)

    print(f"Comparing '{img1}' and '{img2}':\n")

    print(f"1️ Perceptual Hash (pHash) difference: {phash_diff}")
    print("   - Lower values mean images are more similar.")

    print(f"\n2️ Structural Similarity Index (SSIM): {ssim_score:.4f}")
    print("   - Value ranges from 0 to 1. Closer to 1 means more similar.")

    print(f"\n3️ ORB Feature Matches: {orb_matches}")
    print("   - Higher number of matches indicates higher similarity.")
