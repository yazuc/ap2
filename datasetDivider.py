import pandas as pd
import shutil
import os

origem_cat = r'D:\Faculdade\cic\Fundamentos de ES\Primeiro Projeto\2\ap2\train\cat'
destiny_cat = r'D:\Faculdade\cic\Fundamentos de ES\Primeiro Projeto\2\ap2\test\cat'
origem_dog = r'D:\Faculdade\cic\Fundamentos de ES\Primeiro Projeto\2\ap2\train\dog'
destiny_dog = r'D:\Faculdade\cic\Fundamentos de ES\Primeiro Projeto\2\ap2\test\dog'

cats = pd.DataFrame(os.listdir(".\\train\\cat"), columns=['Cats'])
dogs = pd.DataFrame(os.listdir(".\\train\\dog"), columns=['Dogs'])

test_cats = cats.sample(frac = 0.1, random_state = 69)
test_dogs = dogs.sample(frac = 0.1, random_state = 420)

test_cats = test_cats.reset_index()
test_dogs = test_dogs.reset_index()

for index, row in test_cats.iterrows():

    print(index)

    shutil.move(os.path.join(origem_cat, test_cats.iloc[index]["Cats"]), os.path.join(destiny_cat, test_cats.iloc[index]["Cats"]))
    shutil.move(os.path.join(origem_dog, test_dogs.iloc[index]["Dogs"]), os.path.join(destiny_dog, test_dogs.iloc[index]["Dogs"]))