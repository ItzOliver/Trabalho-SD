from PIL import Image
from PIL import ImageFilter

def Preto_e_Branco(img):
    PB = Image.open(img).convert('L')
    return PB

def Negativo(img):
    img = Image.open(img)
    negativo = Image.new(img.mode, img.size, "red")

    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            r, g, b = img.getpixel((i, j))
            negativo.putpixel((i, j), (255-r, 255-g, 255-b))

    return negativo

def get_max(valor):
    if valor > 255:
        return 255

    return int(valor)

def sepia_pixel(vermelho, verde, azul):
    tVermelho = get_max((0.759 * vermelho) + (0.398 * verde) + (0.194 * azul))
    tVerde = get_max((0.676 * vermelho) + (0.354 * verde) + (0.173 * azul))
    tAzul = get_max((0.524 * vermelho) + (0.277 * verde) + (0.136 * azul))

    return tVermelho, tVerde, tAzul

def Sepia(img):
    img = Image.open(img)
    sepia = Image.new(img.mode, img.size, "white")

    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            r, g, b = img.getpixel((i, j))
            sepia.putpixel((i, j), (sepia_pixel(r, g, b)))

    return sepia

def Blur(img):
    img = Image.open(img)
    Blur = img.filter(ImageFilter.BLUR)
    return Blur

def Contorno(img):
    img = Image.open(img)
    Contorno = img.filter(ImageFilter.CONTOUR)
    return Contorno

def Relevo(img):
    img = Image.open(img)
    emboss = img.filter(ImageFilter.EMBOSS)
    return emboss

def Pixelizar8Pixels(img):
    img = Image.open(img)
    imgMenor = img.resize((8, 8))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar16Pixels(img):
    img = Image.open(img)
    imgMenor = img.resize((16, 16))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar32Pixels(img):
    img = Image.open(img)
    imgMenor = img.resize((32, 32))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar64Pixels(img):
    img = Image.open(img)
    imgMenor = img.resize((64, 64))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar128Pixels(img):
    img = Image.open(img)
    imgMenor = img.resize((128, 128))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar256Pixels(img):
    img = Image.open(img)
    imgMenor = img.resize((256, 256))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

nome = input("Escreva o nome do arquivo jpg que você deseja modificar:\n")
arquivo = nome + ".jpg"

print("\nSelecione qual filtro você deseja aplicar na imagem:")
print("1 - Preto e Branco")
print("2 - Negativo")
print("3 - Sepia")
print("4 - Blur")
print("5 - Contorno")
print("6 - Relevo")
print("7 - Pixel Art 8 Pixels")
print("8 - Pixel Art 16 Pixels")
print("9 - Pixel Art 32 Pixels")
print("10 - Pixel Art 64 Pixels")
print("11 - Pixel Art 128 Pixels")
print("12 - Pixel Art 256 Pixels")

opcao = int(input("Digite o número do filtro:\n"))

opcoes = {
    1: lambda: Preto_e_Branco(arquivo).save(nome + "_Preto_e_Branco.jpg"),
    2: lambda: Negativo(arquivo).save(nome + "_Negativo.jpg"),
    3: lambda: Sepia(arquivo).save(nome + "_Sepia.jpg"),
    4: lambda: Blur(arquivo).save(nome + "_Blur.jpg"),
    5: lambda: Contorno(arquivo).save(nome + "_Contorno.jpg"),
    6: lambda: Relevo(arquivo).save(nome + "_Relevo.jpg"),
    7: lambda: Pixelizar8Pixels(arquivo).save(nome + "_PixelArt8P.jpg"),
    8: lambda: Pixelizar16Pixels(arquivo).save(nome + "_PixelArt16P.jpg"),
    9: lambda: Pixelizar32Pixels(arquivo).save(nome + "_PixelArt32P.jpg"),
    10: lambda: Pixelizar64Pixels(arquivo).save(nome + "_PixelArt64P.jpg"),
    11: lambda: Pixelizar128Pixels(arquivo).save(nome + "_PixelArt128P.jpg"),
    12: lambda: Pixelizar256Pixels(arquivo).save(nome + "_PixelArt256P.jpg")
}

if opcao in opcoes:
    opcoes[opcao]()
    print("Imagem alterada com sucesso!")
else:
    print("Opção inválida!")