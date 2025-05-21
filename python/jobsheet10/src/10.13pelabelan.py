import cv2
import numpy as np

def visualisasiWarna(citraBerlabel):
    citraWarnaHue = np.uint8(179 * citraBerlabel / np.max(citraBerlabel) if np.max(citraBerlabel) > 0 else 0)
    kanalLain = np.uint8(255 * np.ones_like(citraBerlabel))
    citraWarna = cv2.merge([citraWarnaHue, kanalLain, kanalLain])
    citraWarna = cv2.cvtColor(citraWarna, cv2.COLOR_HSV2BGR)
    citraWarna[citraBerlabel == 0] = 0
    cv2.imshow("Citra berlabel", citraWarna)
    cv2.waitKey(0)

citra = cv2.imread(r'python\jobsheet10\img\bentukWarna.png', 0)
ambang, citra_biner = cv2.threshold(citra, 127, 255, cv2.THRESH_BINARY)
jumObjek, citraBerlabel = cv2.connectedComponents(citra_biner)
visualisasiWarna(citraBerlabel)