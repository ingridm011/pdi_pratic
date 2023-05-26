from PIL import Image
import numpy as np

def main():
    
    img = Image.open("lena_ruido.bmp").convert("L")
    width, height = img.size
    pixel = np.asarray(img).copy()
    mascara = np.array([[1, 3, 1],[3, 16, 3], [1, 3, 1]])
    mascara = mascara/32
        
    for x in range(1,height-1):
        for y in range(1,width-1):
            jan = np.sum(pixel[x-1:x+2, y-1:y+2] * mascara)
            pixel[x,y] = jan
            
    imgN = Image.fromarray(pixel)
    imgN.save("mascara3.png")
            
                
    
if __name__ == "__main__":
    main() 