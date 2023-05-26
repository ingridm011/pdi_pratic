from PIL import Image
import numpy as np

def main():
    
    img = Image.open("q4.png").convert("L")
    width, height = img.size
    pixel = np.asarray(img).copy()
    pixelE = np.asarray(img).copy()
    pixelD = pixel.copy()
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
            
    imgE = Image.fromarray(erosao(pixel, elemE, centro))
    imgE.save("erosao.png")
    
    img2 = Image.fromarray(dilatacao(pixel, elemE, centro))
    img2.save("dilatacao.png")
    
    def abertura (pixels, elemE, centro):
        
        pixelErodido = erosao(pixels, elemE, centro)
        resultA = dilatacao(pixelErodido, elemE, centro)
        imgA = Image.fromarray(resultA)
        imgA.save("abertura.png")
        
    abertura(pixel, elemE, centro)
    
    def fechamento(pixels, elemE, centro):
    
        pixelDilatado = dilatacao(pixels, elemE, centro)
        Image.fromarray(pixelDilatado)
        img2.save("dilatacaof.png")
        resultF = erosao(pixelDilatado, elemE, centro)
        imgA = Image.fromarray(resultF)
        imgA.save("fechamento.png")
        
    fechamento(pixel, elemE, centro)
                 
if __name__ == "__main__":
    main()   