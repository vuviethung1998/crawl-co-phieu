import pandas as pd

if __name__=="__main__":
    industry = pd.read_csv('industry_final_merged.csv')

    industry_modify = industry[['Chung_khoan_name', 'Nganh']]
    industry_modify.drop_duplicates(subset=['Chung_khoan_name','Nganh'],inplace=True)
    industry_modify.reset_index(drop=True, inplace=True)
    industry_modify.to_csv('industry_modified.csv')

