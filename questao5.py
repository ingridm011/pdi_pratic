from PIL import Image
import numpy as np

def main():
    img = Image.open("quadro.png")
    width, height = img.size
    pixel = np.asarray(img).copy()
    
    for x in range(height):
            for y in range(width):
                if np.all(pixel[x,y] == [0,0,0,255]):
                    pixel[x,y] = [0,0,0,255]
                else:
                    pixel[x,y] = [255,255,255,255]
                                    
    Image.fromarray(pixel).show()           


if __name__ == "__main__":
    main() 