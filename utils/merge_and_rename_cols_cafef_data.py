import pandas as pd
# lich_su_giao_dich + thong_ke_dat_lenh + giao_dich_khoi_ngoai + nganh + nhom_nganh

if __name__=="__main__":
    #lich su giao dich
    lich_su_giao_dich = pd.read_csv('./lich_su_giao_dich.csv' )
    lich_su_giao_dich.drop(columns=['_id'],inplace=True)
    print(lich_su_giao_dich.keys())

    #rename columns
    lich_su_giao_dich.rename(columns = {'KL GD Khớp Lệnh':'KL Giao Dịch khớp lệnh',
                                        'GT GD Khớp Lệnh': 'GT Giao Dịch khớp lệnh',
                                        'KL GD Thỏa Thuận': 'KL Giao Dịch thỏa thuận',
                                        'GT GD Thỏa Thuận': 'GT Giao Dịch thỏa thuận',
                                        }, inplace = True)
    # thong ke dat lenh
    thong_ke_dat_lenh = pd.read_csv('./thong_ke_dat_lenh.csv')
    thong_ke_dat_lenh.drop(columns=['_id', 'Thay Đổi', 'Thay Đổi Theo %'],inplace=True)

    # rename cols
    thong_ke_dat_lenh.rename(columns = {'Số lệnh mua':'Số lệnh mua khớp lệnh',
                                        'Khối lượng đặt mua': 'Khối lượng đặt mua khớp lệnh',
                                        'KLTB 1 lệnh mua': 'KLTB 1 lệnh mua khớp lệnh',
                                        'Số lệnh bán': 'Số lệnh bán khớp lệnh',
                                        'Khối lượng đặt bán': 'Khối lượng đặt bán khớp lệnh',
                                        'KLTB 1 lệnh bán': 'KLTB 1 lệnh bán khớp lệnh'
                                        }, inplace = True)
    print(thong_ke_dat_lenh.keys())

    # gdkn
    giao_dich_khoi_ngoai = pd.read_csv('./giao_dich_khoi_ngoai.csv')

    # rename cols
    giao_dich_khoi_ngoai.drop(columns=['_id', 'Thay Đổi', 'Thay Đổi Theo %'],inplace=True)
    giao_dich_khoi_ngoai.rename(columns = {"KL Giao Dịch Ròng": "KL Giao Dịch Ròng khối ngoại",
                                           "GT Giao Dịch Ròng": "GT Giao Dịch Ròng khối ngoại",
                                           "KLTB 1 lệnh mua": "KL đặt mua khối ngoại",
                                           "Khối lượng đặt mua": "GT đặt mua khối ngoại",
                                           "Giá trị đặt mua": "KL đặt bán khối ngoại",
                                           "Khối lượng đặt bán": "GT đặt bán khối ngoại"
                                           }, inplace=True)
    print(giao_dich_khoi_ngoai.keys())

    # # gop 3 df
    result_1 = pd.merge(thong_ke_dat_lenh,lich_su_giao_dich, on=['Chung_khoan_name', 'San Chung Khoan', 'Ngày'])
    result_2 = pd.merge(result_1,giao_dich_khoi_ngoai, on=['Chung_khoan_name', 'San Chung Khoan', 'Ngày'])

    result_2.to_csv('./cafef_tong_hop.csv')



