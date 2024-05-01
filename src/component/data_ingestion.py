import os

import sys
sys.path.append('C:/Users/amran/Documents/mlprojects')
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
sys.path.append('C:/Users/amran/Documents/mlprojects/src/component')
from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig
from dataclasses import dataclass
from model_trainer import ModelTrainerConfig
from model_trainer import ModelTrainer
#

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv") #the compounds of data ingestion
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    
    
class DataIngestion:
    
    def __init__(self):
        self.ingestion_config= DataIngestionConfig() #will consist class variable called earlier
    
    def initiate_data_ingestion(self):
        #read from the data base 
        logging.info("Enter the data ingestion method or component")
        try: 
            
            df= pd.read_csv(r'C:\Users\amran\Documents\mlprojects\artifacts\data.csv')
            logging.info('REad the data set as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split ")
            train_set,test_set =train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completes")
            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)
            pass
        
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))