import pandas as pd

if __name__=="__main__":

    lich_su_giao_dich = pd.read_csv('./lich_su_giao_dich_top_60.csv' )
    lich_su_giao_dich.drop(columns=['_id'],inplace=True)
    # print(lich_su_giao_dich.keys())

    thong_ke_dat_lenh = pd.read_csv('./thong_ke_dat_lenh_top_60.csv')
    thong_ke_dat_lenh.drop(columns=['_id', 'Thay Đổi', 'Thay Đổi Theo %'],inplace=True)
    thong_ke_dat_lenh.rename(columns = {'Số lệnh mua':'Số lệnh mua khớp lệnh',
                                        'Khối lượng đặt mua': 'Khối lượng đặt mua khớp lệnh',
                                        'KLTB 1 lệnh mua': 'KLTB 1 lệnh mua khớp lệnh',
                                        'Số lệnh bán': 'Số lệnh bán khớp lệnh',
                                        'Khối lượng đặt bán': 'Khối lượng đặt bán khớp lệnh',
                                        'KLTB 1 lệnh bán': 'KLTB 1 lệnh bán khớp lệnh'
                                        }, inplace = True)
    # print(thong_ke_dat_lenh.keys())

    giao_dich_khoi_ngoai = pd.read_csv('./giao_dich_khoi_ngoai_top_60.csv')
    giao_dich_khoi_ngoai.drop(columns=['_id', 'Thay Đổi', 'Thay Đổi Theo %'],inplace=True)
    giao_dich_khoi_ngoai.rename(columns = {"KL Giao Dịch Ròng": "KL Giao Dịch Ròng Khối Ngoại",
                                           "GT Giao Dịch Ròng": "GT Giao Dịch Ròng Khối Ngoại",
                                           "KLTB 1 lệnh mua": "KL đặt mua khối ngoại",
                                           "Khối lượng đặt mua": "GT đặt mua khối ngoại",
                                           "Giá trị đặt mua": "KL đặt bán khối ngoại",
                                           "Khối lượng đặt bán": "GT đặt bán khối ngoại"
                                           }, inplace=True)
    # print(giao_dich_khoi_ngoai.keys())

    # gop 3 df
    result_1 = pd.merge(giao_dich_khoi_ngoai,lich_su_giao_dich, on=['Chung_khoan_name', 'Ngày'])
    result_2 = pd.merge(result_1,thong_ke_dat_lenh, on=['Chung_khoan_name', 'Ngày'])

    # loai bo duplicated columns
    final_res  = result_2.drop_duplicates(subset=['Chung_khoan_name', 'Ngày'])
    final_res.to_csv('./merged_full_data_top_60.csv')
    # pd.set_option('display.max_columns', None)
    # print(final_res.tail())
    # print(len(final_res))

