# ap2
 trab ap2

Nomes: Leonardo T. Rubert, Bruno Battesini

permitir long path para o tensorflow:

-executar no powershell com adm
    New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
    -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force

 requisitos python3:

 python3 -m pip install tensorflow
 python3 -m pip install keras
 python3 -m install opencv-python  
 python3 -m install numpy
 python3 -m pip install openpyxl
 python3 -m pip install pandas
 python3 -m pip install Pillow
 python3 -m pip install scipy   


é necessário alterar os locais conforme sua máquina
ex de variaveis a alterar 
    ap.py: train_directory
    predict.py: img_path_cat, img_path_dog
    reorder.py: dataset_path
    datasetDivider.py: origem_cat, destiny_cat, origem_dog, destiny_dog

compilação dos arquivos com python3

python3 ap.py - para gerar os modelos

python3 predict.py - para prever baseado nas imagens de teste

python3 reorder.py - basicamente monta o diretorio de treino da maneira que ap.py consegue entender

python3 datasetDivider.py - separa os datasets em treino e teste

caso dê algum problema com os modelos, é necessário rodar ap.py novamente

código baseado
https://www.kaggle.com/code/susandaneshmand/cats-vs-dogs-classification-accuracy-99/notebook#Split-Train-,-Test-,-Validation


sobre os modelos:

salvamos diversos modelos, a principio o modelo rodando a 10 epochs e outro rodando a 20 epochs, tem duas versões de cada modelo pois achavamos que o jeito de salvar eles era na
extensão .h5, depois por um erro salvamos em .h6 e tivemos uns casos de erro ao usar esses modelos em outras máquinas, depois de uma pesquisa começamos a usar .keras que é utilizado
na própria documentação do keras, encontrado nesse link: https://keras.io/guides/serialization_and_saving/#savedmodel-format