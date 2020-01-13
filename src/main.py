import os
import pandas as pd
from API.Translator import Translator

INPUT_PATH = os.path.join(os.getcwd(), "dataset/input")

if __name__ == "__main__":
    translator = Translator(num_workers=1, 
                            source_language='en', 
                            target_language='ko', 
                            model='nmt')
    translator.translate_bulk(INPUT_PATH)