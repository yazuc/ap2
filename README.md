# ap2
 trab ap2

Nomes: Leonardo T. Rubert, Bruno Battesini

 requisitos python3:

 python3 -m pip install tensorflow
 python3 -m pip install keras
 python3 -m install opencv-python  
 python3 -m install numpy
 python3 -m pip install openpyxl
 python3 -m pip install pandas
 python3 -m pip install Pillow
 python3 -m pip install scipy   

permitir long path para o tensorflow:

-executar no powershell com adm
    New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
    -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force


é necessário alterar os locais conforme sua máquina
ex de variaveis a alterar 
    ap.py: train_directory
    predict.py: img_path_cat, img_path_dog
    reorder.py: dataset_path
    datasetDivider.py: origem_cat, destiny_cat, origem_dog, destiny_dog

compilação dos arquivos com python3

python3 ap.py

python3 predict.py

python3 reorder.py basicamente monta o diretorio de treino da maneira que ap.py consegue entender

python3 datasetDivider.py separa os datasets em treino e teste

código baseado
https://www.kaggle.com/code/susandaneshmand/cats-vs-dogs-classification-accuracy-99/notebook#Split-Train-,-Test-,-Validation
