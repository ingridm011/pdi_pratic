from PIL import Image
import numpy as np

def main():
    
    img = Image.open("lena_gray.bmp").convert("L")
    width, height = img.size
    pixel = np.asarray(img).copy().astype("int8")
    original = np.asarray(pixel).copy().astype("int8")
    mascaraHorizontal = np.array([[-1, 0, 1],[-1, 0, 1], [-1, 0, 1]])
    mascaraVertical = np.array([[-1, -1, -1],[0, 0, 0], [1, 1, 1]])
    
        
    for x in range(1,height-1):
        for y in range(1,width-1):
            pixel[x,y] = int(np.sum(original[x-1:x+2, y-1:y+2] * mascaraVertical))
                     
    pixel[pixel>255] = 255
    pixel[pixel < 0] = 0
    Image.fromarray(pixel).show()
        

            
if __name__ == "__main__":
    main() 