import pandas as pd


if __name__=="__main__":
    df = pd.read_csv('./chi_tieu_quan_trong_yearly.csv')
    check_rows_contain_null = df[df.isnull().any(axis=1)]
    check_rows_contain_zr = df[~(df == 0).any(axis=1)]
    print(list(set(check_rows_contain_null['Chung_khoan_name'].tolist())))
    print(list(set(check_rows_contain_zr['Chung_khoan_name'].tolist())))