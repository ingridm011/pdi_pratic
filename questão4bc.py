from PIL import Image
import numpy as np

def main():
    
    img = Image.open("imgN.png").convert("L")
    width, height = img.size
    pixel = np.asarray(img).copy()
    pixelD = pixel.copy()
    pixelE = pixel.copy()
    elemE = np.full((3,3), 255)
    centro = (1,2)
    
    def dilatacao (pixels, elemE, centro):
        for x in range(height):
            for y in range(width):
                if elemE[centro] == pixels[x,y]:
                        pixelD[x-1:x+2, y-1:y+2] = elemE
                        
        return pixelD
    
    def erosao (pixels, elemE, centro):
        for x in range(height):
            for y in range(width):
                    if not np.array_equal(elemE,pixels[x-1:x+2,y-1:y+2]):
                        pixelE[x,y] = 0
        return pixelE
    
    def abertura (pixels, elemE, centro):
        
        pixelErodido = erosao(pixels, elemE, centro)
        imgE = Image.fromarray(pixelErodido)
        imgE.save("fds.png")
        resultAbtr = dilatacao (pixelErodido, elemE, centro)
        imgA = Image.fromarray(resultAbtr)
        imgA.save("abertura.png")
        
    abertura(pixel, elemE, centro)
    
if __name__ == "__main__":
    main() 