const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const fs = require('fs');
const path = require('path');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const packageDefinition = protoLoader.loadSync(
    'filtro_imagem.proto',
    {keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true    
    });
const filtro_imagem_proto = grpc.loadPackageDefinition(packageDefinition).filtro;

function main() {
    const client = new filtro_imagem_proto('192.168.1.9:50051', grpc.credentials.createInsecure());

    console.log("\nSelecione qual filtro você deseja aplicar na imagem:");
    console.log("1 - Preto e Branco");
    console.log("2 - Negativo");
    console.log("3 - Sepia");
    console.log("4 - Blur");
    console.log("5 - Contorno");
    console.log("6 - Relevo");
    console.log("7 - Pixel Art 8 Pixels");
    console.log("8 - Pixel Art 16 Pixels");
    console.log("9 - Pixel Art 32 Pixels");
    console.log("10 - Pixel Art 64 Pixels");
    console.log("11 - Pixel Art 128 Pixels");
    console.log("12 - Pixel Art 256 Pixels");

    readline.question("Escolha o filtro dentre as opções fornecidas:\n", resposta => {
        const filtro = parseInt(resposta);
        const nome_imagem = 'input';
        const opcoes = {
            1: "_Preto_e_Branco",
            2: "_Negativo",
            3: "_Sepia",
            4: "_Blur",
            5: "_Contorno",
            6: "_Relevo",
            7: "_Pixelizado_8_Pixels",
            8: "_Pixelizado_16_Pixels",
            9: "_Pixelizado_32_Pixels",
            10: "_Pixelizado_64_Pixels",
            11: "_Pixelizado_128_Pixels",
            12: "_Pixelizado_256_Pixels"
        };
        if (opcoes[filtro]) {
            const tipo_filtro = opcoes[filtro];

            const imagem = fs.readFileSync(nome_imagem + '.jpg');

            client.aplicaFiltro({ filtro: filtro, imagem: imagem, nome_imagem: nome_imagem}, function (err, response) {
                if (err) {
                    console.error(err);
                } else {
                    console.log('Status: Sucesso');
                    fs.writeFileSync(nome_imagem + tipo_filtro + '.jpg', response.imagemModificada);
                }
            });
        } else {
            console.log("Opção inválida!");
        }

        readline.close();
    });

}

main();