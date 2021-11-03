import pandas as pd
if __name__=="__main__":
    df = pd.read_csv('nhom_nganh.csv')
    df_blank = df[df.isnull().any(axis=1)]
    df_blank.to_csv('nhom_nganh_blank.csv')
