import os
import glob
import pandas as pd
import numpy as np
from multiprocessing import Pool
from google.cloud import translate_v2 as translate
from time import sleep

PROJECT_PATH = os.getcwd()
INPUT_PATH = os.path.join(PROJECT_PATH, "dataset/input")
OUTPUT_PATH = os.path.join(PROJECT_PATH, "dataset/output/")

class Translator(object):
    def __init__(self, num_workers=1, source_language='en', target_language='ko', model='nmt'):
        self.num_workers = num_workers
        self.source_language = source_language
        self.target_language = target_language
        self.model = model

        credential_path = os.path.join(PROJECT_PATH, "google_credential.json")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
        self.client = translate.Client()

    def load_data_path(self, input_path=None):
        path = os.path.join(input_path, "*.csv")
        data_list = glob.glob(path)
        print(data_list)
        return data_list

    def translate_bulk(self, input_folder=None):
        source_list = self.load_data_path(input_folder)

        for src in source_list:
            output = src.replace("input", "output")
            translate_result = self.processing(src)
            translate_result.to_csv(output)

    def processing(self, file_name=None):
        source_file = pd.read_csv(file_name)
        #source_file = source_file.iloc[0:100,:]

        source_split = np.array_split(source_file['Input'], self.num_workers)
        
        pool = Pool(self.num_workers)
        translate_result = pd.concat(map(self.translate_file, source_split))
        pool.close()
        pool.join()
        return translate_result

    def translate_file(self, file=None ):

        temp_dataframe = pd.DataFrame(columns=['input', 'output'])
        size = 0
        for line in file:
            size += len(line)
            sleep(0.5)
            print(size)
            result = self.client.translate( line,
                                            source_language=self.source_language, 
                                            target_language=self.target_language,
                                            model=self.model)
            print(result['input'], result['translatedText'])
            temp_dataframe.loc[len(temp_dataframe)] =[result['input'], result['translatedText']]
            
        return temp_dataframe            
            
        

if __name__ == "__main__":
    translator = Translator(num_workers=1)
    translator.translate_bulk(INPUT_PATH)