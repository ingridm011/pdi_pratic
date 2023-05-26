from PIL import Image
import numpy as np

def main():
    
    img = Image.open("lena_gray.bmp").convert("L")
    width, height = img.size
    pixelB = np.asarray(img).copy()
    pixel = np.asarray(img).copy().astype("int8")
    m = np.full((3,3), 1)
    m = m/9
    mascara = np.array([[-1, -1, -1],[-1, 8, -1], [-1, -1, -1]])
    i = int((9-2)/2)
    
    def borramento (pixel, m):    
        for x in range(1,height-1):
            for y in range(1,width-1):
                jan = np.sum(pixel[x-1:x+2, y-1:y+2] * m)
                pixel[x,y] = jan
                
        Image.fromarray(pixelB).show()
    
        return pixel
    
    original = borramento(pixel, m)
    original = np.asarray(original).copy().astype("int8")
        
    for x in range(i,height-1):
        for y in range(i,width-1):
            pixel[x,y] = int(np.sum(original[x-1:x+2, y-1:y+2] * mascara))
            
    Image.fromarray(pixel).show()       
    def adjustment(pixel: int):
        return int((pixel + 255) * 255 / 510)
   
    ajuste = np.vectorize(adjustment)
    output = np.asarray(ajuste(pixel), dtype=np.uint8)
             
    pixel = original + output        
    Image.fromarray(pixel).show()
           
       
if __name__ == "__main__":
    main() 