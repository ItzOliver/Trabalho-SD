from concurrent import futures
import grpc
import filtro_imagem_pb2
import filtro_imagem_pb2_grpc
from PIL import Image, ImageFilter
import io

def Preto_e_Branco(img):
    PB = img.convert('L')
    return PB

def Negativo(img):
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
    sepia = Image.new(img.mode, img.size, "white")

    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            r, g, b = img.getpixel((i, j))
            sepia.putpixel((i, j), (sepia_pixel(r, g, b)))

    return sepia

def Blur(img):
    Blur = img.filter(ImageFilter.BLUR)
    return Blur

def Contorno(img):
    Contorno = img.filter(ImageFilter.CONTOUR)
    return Contorno

def Relevo(img):
    emboss = img.filter(ImageFilter.EMBOSS)
    return emboss

def Pixelizar8Pixels(img):
    imgMenor = img.resize((8, 8))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar16Pixels(img):
    imgMenor = img.resize((16, 16))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar32Pixels(img):
    imgMenor = img.resize((32, 32))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar64Pixels(img):
    imgMenor = img.resize((64, 64))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar128Pixels(img):
    imgMenor = img.resize((128, 128))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

def Pixelizar256Pixels(img):
    imgMenor = img.resize((256, 256))
    imgFinal = imgMenor.resize(img.size)
    return imgFinal

class filtroServicer(filtro_imagem_pb2_grpc.filtroServicer):
    def aplicaFiltro(self, request, context):
        opcao = request.filtro
        dadosImagem = request.imagem
    
        imagem = Image.open(io.BytesIO(dadosImagem)) # Lê os bytes da imagem recebida e transforma eles em imagem

        opcoes = {
            1: lambda: Preto_e_Branco(imagem),
            2: lambda: Negativo(imagem),
            3: lambda: Sepia(imagem),
            4: lambda: Blur(imagem),
            5: lambda: Contorno(imagem),
            6: lambda: Relevo(imagem),
            7: lambda: Pixelizar8Pixels(imagem),
            8: lambda: Pixelizar16Pixels(imagem),
            9: lambda: Pixelizar32Pixels(imagem),
            10: lambda: Pixelizar64Pixels(imagem),
            11: lambda: Pixelizar128Pixels(imagem),
            12: lambda: Pixelizar256Pixels(imagem)
        }

        if opcao in opcoes:
            imagemProcessada = opcoes[opcao]()
            dadosImagemProcessada = io.BytesIO() # Converte a imagem gerada em bytes para o envio
            imagemProcessada.save(dadosImagemProcessada, format = "JPEG") 
            dadosImagemProcessada = dadosImagemProcessada.getvalue()
            return filtro_imagem_pb2.ImageResponse(imagemModificada = dadosImagemProcessada)
        else:
            context.set_details("Opção inválida!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return filtro_imagem_pb2.ImageResponse(imagemModificada = b"")

def serve():
    print("Iniciando Server!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10)) ### especifica o número de threads disponíveis
    filtro_imagem_pb2_grpc.add_filtroServicer_to_server(filtroServicer(), server)
    server.add_insecure_port("192.168.172.192:50051")
    server.start()
    print("ouvindo...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()