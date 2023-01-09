import re
import sqlite3
from datetime import datetime
from os import listdir
import json
import shutil
import pandas as pd
from application_login.logger import App_Logger


class RawDataValidation:
    """
    This class handles all the validation check on Raw Training Data
    """
    
    def __init__(self,path):
        self.Batch_Directory = path
        self.schema_path = "schema_training.json"
    
    def values_from_schema(self):
        """
        This method extracts all the relevant information from the pre-defined "schema_training.json" file.
        Output: LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, Number of Columns
        On Failure: Raise ValueError,KeyError,Exception
        """
        
        try:
            with open(self.schema_path,'r') as f:
                dic = json.load(f)
                f.close()
            pattern = dic['SampleFileName']
            LengthOfDateStampInFile = dic['LengthOfDateStampInFile']
            LengthOfTimeStampInFile = dic['LengthOfTimeStampInFile']
            no_of_col = dic['NumberofColumns']
            column_names = dic['ColName']
               
        except:
            pass
        
        return LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, no_of_col

raw=RawDataValidation('Dataset')
raw.values_from_schema()
