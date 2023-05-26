from PIL import Image
import numpy as np

def main():
    
    img = Image.open("lena_gray.bmp").convert("L")
    width, height = img.size
    pixel = np.asarray(img).copy()
    original = np.asarray(img).copy()
    m = np.full((3,3), 1)
    m = m/9
    
    def borramento (pixel, m):    
        for x in range(1,height-1):
            for y in range(1,width-1):
                jan = np.sum(pixel[x-1:x+2, y-1:y+2] * m)
                pixel[x,y] = jan
                
        imgN = Image.fromarray(pixel)
        imgN.save("borrada2.png")
        
        return pixel
    
    def unsharpM (original, pixel, k):
        
        mascara = np.subtract(original, pixel)
        original = original + k * mascara
               
        imgUM = Image.fromarray(original)
        imgUM.save("mascaraUnsharp.png")
        
        
    def highBoost (original, pixel, k):
        mascara = np.subtract(original, pixel)
        original = original + k * mascara
               
        imgUM = Image.fromarray(original).convert("RGB")
        imgUM.save("highBoost.png")
        
    pixelBorrado = borramento(pixel, m)
    unsharpM(original, pixelBorrado, 1)
    highBoost(original, pixelBorrado, 1.2)
    

if __name__ == "__main__":
    main() 