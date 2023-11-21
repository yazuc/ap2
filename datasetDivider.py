import pandas as pd
import os

cats = pd.DataFrame(os.listdir("./train/cat"), columns=['Cats'])
dogs = pd.DataFrame(os.listdir("./train/dog"), columns=['Dogs'])

test_cats = cats.sample(frac = 0.1, random_state = 69)
test_dogs = dogs.sample(frac = 0.1, random_state = 420)

print(test_dogs)