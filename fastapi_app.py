from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

fitted_lamda_file_path = "E:\\python\\2.PROJECTS\\car sales prediction\\artifacts\\fitted_lambda.pkl"
with open(fitted_lamda_file_path, 'rb') as f:
    fitted_lamda = pickle.load(f)

