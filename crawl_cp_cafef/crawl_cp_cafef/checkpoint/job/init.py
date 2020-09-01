#1. lay list co phieu, dat ten la {co_phieu}.txt
#2. init voi moi file = 0
VN30 = ['BID', 'CTG', 'EIB', 'FPT', 'GAS', 'HDB', 'HPG', 'KDH', 'MBB', 'MSN', 'MWG', 'NVL', 'PLX',
        'PNJ', 'POW', 'REE', 'ROS', 'SAB', 'SBT', 'SSI', 'STB', 'TCB', 'TCH', 'VCB', 'VHM', 'VIC',
        'VJC', 'VNM','VPB', 'VRE']

HNX30 = ['ACB', 'BVS', 'CAP', 'CEO', 'DDG', 'DHT', 'DP3', 'DTD', 'HUT', 'KLF', 'L14', 'LHC', 'MBS',
         'NBC', 'NDN', 'NRC', 'PVB', 'PVC', 'PVI', 'PVS', 'SHB', 'SHS', 'SLS', 'TNG', 'TVC', 'VC3',
         'VCG', 'VCS', 'VGS', 'VMC']

if __name__=="__main__":
    lst_cp = VN30 + HNX30

    for cp in lst_cp:
        f = open("{}.txt".format(cp), "w")
        f.write('0')
