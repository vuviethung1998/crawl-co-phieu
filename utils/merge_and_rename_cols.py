import pandas as pd
# lich_su_giao_dich + thong_ke_dat_lenh + giao_dich_khoi_ngoai + nganh + nhom_nganh

if __name__=="__main__":
    #industry
    # industry = pd.read_csv('./industry_final.csv')
    # industry.rename(columns = {"Nganh" :"Nhom_nganh" }, inplace=True)
    # industry.drop(columns=['_id'],inplace=True)

    # chi_so_tai_chinh = pd.read_csv('./chi_so_tai_chinh_yearly.csv')
    # chi_so_tai_chinh.drop(columns=['_id'],inplace=True)
    #
    # print(chi_so_tai_chinh.columns)
    #
    # ket_qua_kinh_doanh = pd.read_csv('./ket_qua_kinh_doanh_yearly.csv')
    # ket_qua_kinh_doanh  = ket_qua_kinh_doanh.drop_duplicates(subset=['Chung_khoan_name',  'Year'])
    # ket_qua_kinh_doanh.drop(columns=['_id'],inplace=True)
    #
    # print(ket_qua_kinh_doanh.columns)

    # chi_tieu_quan_trong = pd.read_csv('./chi_tieu_quan_trong_yearly.csv')
    # chi_tieu_quan_trong.drop(columns=['_id'],inplace=True)
    # chi_tieu_quan_trong  = chi_tieu_quan_trong.drop_duplicates(subset=['Chung_khoan_name',  'Năm'])
    # chi_tieu_quan_trong.rename(columns = {'Năm':'Year'}, inplace = True)
    #
    # print(chi_tieu_quan_trong.columns)

    lich_su_giao_dich = pd.read_csv('./lich_su_giao_dich_full.csv' )
    lich_su_giao_dich.drop(columns=['_id'],inplace=True)
    # print(lich_su_giao_dich.keys())
    #
    thong_ke_dat_lenh = pd.read_csv('./thong_ke_dat_lenh_full.csv')
    thong_ke_dat_lenh.drop(columns=['_id', 'Thay Đổi', 'Thay Đổi Theo %'],inplace=True)
    # # thong_ke_dat_lenh.rename(columns = {'Số lệnh mua':'Số lệnh mua khớp lệnh',
    # #                                     'Khối lượng đặt mua': 'Khối lượng đặt mua khớp lệnh',
    # #                                     'KLTB 1 lệnh mua': 'KLTB 1 lệnh mua khớp lệnh',
    # #                                     'Số lệnh bán': 'Số lệnh bán khớp lệnh',
    # #                                     'Khối lượng đặt bán': 'Khối lượng đặt bán khớp lệnh',
    # #                                     'KLTB 1 lệnh bán': 'KLTB 1 lệnh bán khớp lệnh'
    # #                                     }, inplace = True)
    # # print(thong_ke_dat_lenh.keys())
    #
    giao_dich_khoi_ngoai = pd.read_csv('./giao_dich_khoi_ngoai_full.csv')
    giao_dich_khoi_ngoai.drop(columns=['_id', 'Thay Đổi', 'Thay Đổi Theo %'],inplace=True)
    # # giao_dich_khoi_ngoai.rename(columns = {"KL Giao Dịch Ròng": "KL Giao Dịch Ròng Khối Ngoại",
    # #                                        "GT Giao Dịch Ròng": "GT Giao Dịch Ròng Khối Ngoại",
    # #                                        "KLTB 1 lệnh mua": "KL đặt mua khối ngoại",
    # #                                        "Khối lượng đặt mua": "GT đặt mua khối ngoại",
    # #                                        "Giá trị đặt mua": "KL đặt bán khối ngoại",
    # #                                        "Khối lượng đặt bán": "GT đặt bán khối ngoại"
    # #                                        }, inplace=True)
    # # print(giao_dich_khoi_ngoai.keys())
    #
    # # gop 3 df
    result_1 = pd.merge(giao_dich_khoi_ngoai,lich_su_giao_dich, on=['Chung_khoan_name', 'Ngày'])
    result_2 = pd.merge(result_1,thong_ke_dat_lenh, on=['Chung_khoan_name', 'Ngày'])

    # # merge nganh vs nhom nganh
    # # nganh = pd.read_csv('nganh_full_data.csv')[['Chung_khoan_code', 'IndustryName']]
    # # nganh.rename(columns = {"Chung_khoan_code": "Chung_khoan_name", "IndustryName" :"Ngành" }, inplace=True)
    # nhom_nganh = pd.read_csv("industry_modified.csv")
    # # nhom_nganh.rename(columns = {"Chung_khoan_code": "Chung_khoan_name", "IndustryName" :"Nganh" }, inplace=True)
    # # # print(nhom_nganh.head())
    # industry_merged = pd.merge(industry, nhom_nganh, on=['Chung_khoan_name'])
    # #
    # # result_3 = pd.merge(kqkd_cstc, nhom_nganh, on=['Chung_khoan_name'])
    # # loai bo duplicated columns
    # final_res  = industry_merged.drop_duplicates(subset=['Chung_khoan_name',  'Nganh'])
    # # final_res.drop(columns=['Unnamed: 0'],inplace=True)
    # final_res.reset_index(drop=True, inplace=True)
    #
    # final_chi_tieu_quan_trong = pd.merge(chi_tieu_quan_trong, final_res, on=['Chung_khoan_name'], how='left')
    #
    # final_chi_tieu_quan_trong.to_csv('./industry_final_merged.csv')
    # # print(final_chi_tieu_quan_trong.head())



