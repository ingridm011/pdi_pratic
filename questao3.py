from PIL import Image
import numpy as np

def main():
    
    img = Image.open("img1Q3.png").convert("L")
    img2 = Image.open("img2Q3.png").convert("L")
    width, height = img.size
    
    def uniao (img, img2):
        
        pixel1 = np.asarray(img).copy()
        pixel2 = np.asarray(img2).copy()
        pixelN = np.asarray(img).copy()
    
        for x in range(height):
            for y in range(width):
                if pixel1[x,y] == 255 or pixel2[x,y]== 255:
                    pixelN[x,y] = 255
                else:
                    pixelN[x,y] = 0

        imagI = Image.fromarray(pixelN)
        imagI = imagI.save("uniao.png")
    
    def intersecao (img, img2):
        
        pixel1 = np.asarray(img).copy()
        pixel2 = np.asarray(img2).copy()
        pixelN = np.asarray(img).copy()
    
        for x in range(height):
            for y in range(width):
                if pixel1[x,y] == 255 and pixel2[x,y]== 255:
                    pixelN[x,y] = 255
                else:
                    pixelN[x,y] = 0

        imagI = Image.fromarray(pixelN)
        imagI = imagI.save("intersecao.png")
    
    def diferenca (img, img2):
        
        pixel1 = np.asarray(img).copy()
        pixel2 = np.asarray(img2).copy()
        pixelN = np.asarray(img).copy()
        
        for x in range(height):
            for y in range(width):
                if pixel1[x,y] == 255 and pixel2[x,y] == 0:
                    pixelN[x,y] = 255
                else:
                    pixelN[x,y] = 0

        imagI = Image.fromarray(pixelN)
        imagI = imagI.save("diferenca.png")
    
    uniao(img,img2)
    intersecao(img, img2)
    diferenca (img, img2)
    

if __name__ == "__main__":
    main() 