from typing import Union, Any

import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
from sqlalchemy import true

df: Union[Union[TextFileReader, DataFrame], Any] = pd.read_csv('202004-divvy-tripdata.csv')

print(df.truncate())