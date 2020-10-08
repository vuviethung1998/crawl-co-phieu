import json
from bs4 import BeautifulSoup as soup

_str = '''374|updatePanel|ctl00_ContentPlaceHolder1_LabelUpdatePanel|
                                <h1 itemprop="name" style="font-weight:bold;font-size:12px">LỊCH SỬ GIÁ - Mã CK VIC - <a href='http://s.cafef.vn/hose/VIC-tap-doan-vingroup-cong-ty-co-phan.chn' style='color:#fff; font-weigth: normal;'>Hồ sơ công ty</a></h1><span style="color: rgb(255, 255, 204);">
                                    </span>
                            |3975|updatePanel|ctl00_ContentPlaceHolder1_LinkUpdatePanel|
                        <div id="ctl00_ContentPlaceHolder1_divDataHistory" class="cf_ResearchDataHistory_Tab1_Sel">
                            <div class="ResearchDataHistory_BoxHeader"><div></div></div>
                            <div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(1);"><a href="/Lich-su-giao-dich-VIC-1.chn#data" id="ctl00_ContentPlaceHolder1_aLSG">Lịch sử giá</a></div>
                        </div>
                        <div class="splitter"></div>
                        <div id="ctl00_ContentPlaceHolder1_divCungCau" class="cf_ThongKeDatLenh">
                            <div class="ResearchDataHistory_BoxHeader"><div></div></div>
                            <div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(2);">
                                <a href="/Lich-su-giao-dich-VIC-2.chn#data" id="ctl00_ContentPlaceHolder1_aTKL">Thống kê đặt lệnh</a>
                            </div>
                        </div>
                        <div class="splitter" style=''></div>
                        <div id="ctl00_ContentPlaceHolder1_divKhopLenh" class="cf_ThongKeDatLenh" style="width: 145px;">
                            <div class="ResearchDataHistory_BoxHeader" style="background-image: url('http://cafef3.vcmedia.vn/v2/images/history_top_145.gif');"><div></div></div>
                            <div onclick="javascript:changeTabXemLichSu(6);" class="ResearchDataHistory_BoxContent">
                                <a href="/Lich-su-giao-dich-VIC-6.chn#data" id="ctl00_ContentPlaceHolder1_aKL">Khớp lệnh theo lô <img align="absmiddle" alt="" src="http://cafef3.vcmedia.vn/images/new2.png" border="0" /></a>
                            </div>
                        </div>
                        <div class="splitter"></div>
                        <div id="ctl00_ContentPlaceHolder1_divGDNN" class="cf_ResearchDataHistory" style="width: 145px;">
                            <div class="ResearchDataHistory_BoxHeader" style="background-image: url('http://cafef3.vcmedia.vn/v2/images/history_top_145.gif');"><div></div></div>
                            <div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(3);">
                                <a href="/Lich-su-giao-dich-VIC-3.chn#data" id="ctl00_ContentPlaceHolder1_aNDTNG">Giao dịch khối ngoại</a>
                            </div>
                        </div>
                        <div class="splitter" style=''></div>
                        <div id="ctl00_ContentPlaceHolder1_divLocalTrans" class="cf_Codonglon" style="width: 190px;">
                            <div class="ResearchDataHistory_BoxHeader" style="background-image: url('http://cafef3.vcmedia.vn/v2/images/history_top_190.gif');"><div></div></div>
                            <div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(4);">
                                <a href="/Lich-su-giao-dich-VIC-4.chn#data" id="ctl00_ContentPlaceHolder1_aCDL">Giao dịch cổ đông lớn & nội bộ</a>
                            </div>
                        </div>
                        <div class="splitter" style=''></div>
                        <div id="ctl00_ContentPlaceHolder1_divMBLFinal" class="cf_ResearchDataHistory" style="width: 155px;">
                            <div class="ResearchDataHistory_BoxHeader" style="background-image: url('http://cafef3.vcmedia.vn/v2/images/history_top_155.gif');"><div></div></div>
                            <div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(5);">
                                <a href="/Lich-su-giao-dich-VIC-5.chn#data" id="ctl00_ContentPlaceHolder1_aCPQ">Giao dịch cổ phiếu quỹ</a>
                            </div>
                        </div>
                        <div class="splitter"></div>
                        
                        |27949|updatePanel|ctl00_ContentPlaceHolder1_ctl03_panelAjax|

<div id="ctl00_ContentPlaceHolder1_ctl03_divHO" style="background-color:#FFF;width:100%;float:left" align="center">
<table cellpadding="2" cellspacing="0" width="100%" style="border-top: solid 1px #e6e6e6"
            id="GirdTable2">
            <tr style="border-bottom: solid 1px #e6e6e6; font-family: Arial; font-size: 10px;
                font-weight: bold; color: #004276; background-color: #FFF" >
                <td rowspan="2" class="Header_DateItem" style="width:6%">Ngày</td>
                <td id="ctl00_ContentPlaceHolder1_ctl03_thAdjustPrice" rowspan="2" class="Header_Price1" style="width:7%">Giá <br /> điều chỉnh</td>

                <td rowspan="2" class="Header_Price1" style="width:7%">Giá <br /> đóng cửa</td>
                <td rowspan="2" class="Header_ChangeItem" colspan="2" style="width:11%">Thay đổi (+/-%)</td>
                <td colspan="2" class="Header_Price1" style="width:18%">GD khớp lệnh</td>
                <td colspan="2" class="Header_Price1" style="width:18%">GD thỏa thuận</td>
                <td rowspan="2" class="Header_Price1" style="width:6%">Giá <br />mở cửa</td>               
                <td rowspan="2" class="Header_Price1" style="width:6%">Giá <br />cao nhất</td>
                <td rowspan="2" class="Header_Price1" style="width:6%">Giá <br />thấp nhất</td>
                <td style="display:none;" rowspan="2" class="Header_Price1" style="width:6%">KL <br /> đợt 1</td>
                <td style="display:none;" rowspan="2" class="Header_Price1" style="width:6%">KL <br /> đợt 2</td>
                <td style="display:none;" rowspan="2" class="Header_Price1" style="width:6%">KL <br /> đợt 3</td>
            </tr>
            <tr style="border-bottom: solid 1px #e6e6e6; font-family: Arial; font-size: 10px;
                font-weight: bold; color: #004276; background-color: #FFF" >
                <td class="Header_Price1" style="width:7%">KL</td>
                <td class="Header_Price1" style="width:11%">GT</td>
                <td class="Header_Price1" style="width:7%">KL</td>
                <td class="Header_Price1" style="width:11%">GT</td>
            </tr>     
       
    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl01_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">10/09/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl01_Td5" class="Item_Price10">90.50&nbsp;</td>
        <td class="Item_Price10">90.50&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_NoChange>0.00 (0.00 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">421,160&nbsp;</td>
        <td class="Item_Price10">38,405,000,000&nbsp;</td>
        <td class="Item_Price10">128,400&nbsp;</td>
        <td class="LastItem_Price">11,707,512,000&nbsp;</td>
        <td class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_Price10">92.50&nbsp;</td>
        <td class="Item_Price10">90.50&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl02_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">09/09/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl02_Td6" class="Item_Price10">90.50&nbsp;</td>
        <td class="Item_Price10">90.50&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_NoChange>0.00 (0.00 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">865,880&nbsp;</td>
        <td class="Item_Price10">78,115,000,000&nbsp;</td>
        <td class="Item_Price10">145,410&nbsp;</td>
        <td class="LastItem_Price">13,117,436,100&nbsp;</td>
        <td class="Item_Price10">90.40&nbsp;</td>
        <td class="Item_Price10">92.40&nbsp;</td>
        <td class="Item_Price10">89.40&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl03_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">08/09/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl03_Td5" class="Item_Price10">90.50&nbsp;</td>
        <td class="Item_Price10">90.50&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Down>-1.00 (-1.09 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">622,290&nbsp;</td>
        <td class="Item_Price10">56,632,000,000&nbsp;</td>
        <td class="Item_Price10">870,000&nbsp;</td>
        <td class="LastItem_Price">81,954,000,000&nbsp;</td>
        <td class="Item_Price10">91.60&nbsp;</td>
        <td class="Item_Price10">92.50&nbsp;</td>
        <td class="Item_Price10">90.50&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl04_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">07/09/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl04_Td6" class="Item_Price10">91.50&nbsp;</td>
        <td class="Item_Price10">91.50&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Down>-2.50 (-2.66 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">465,400&nbsp;</td>
        <td class="Item_Price10">43,559,000,000&nbsp;</td>
        <td class="Item_Price10">0&nbsp;</td>
        <td class="LastItem_Price">0&nbsp;</td>
        <td class="Item_Price10">94.00&nbsp;</td>
        <td class="Item_Price10">95.30&nbsp;</td>
        <td class="Item_Price10">91.50&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl05_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">04/09/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl05_Td5" class="Item_Price10">94.00&nbsp;</td>
        <td class="Item_Price10">94.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Down>-0.50 (-0.53 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">825,960&nbsp;</td>
        <td class="Item_Price10">77,869,000,000&nbsp;</td>
        <td class="Item_Price10">0&nbsp;</td>
        <td class="LastItem_Price">0&nbsp;</td>
        <td class="Item_Price10">94.50&nbsp;</td>
        <td class="Item_Price10">95.50&nbsp;</td>
        <td class="Item_Price10">93.30&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl06_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">03/09/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl06_Td6" class="Item_Price10">94.50&nbsp;</td>
        <td class="Item_Price10">94.50&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>1.80 (1.94 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">1,037,080&nbsp;</td>
        <td class="Item_Price10">98,376,000,000&nbsp;</td>
        <td class="Item_Price10">70,000&nbsp;</td>
        <td class="LastItem_Price">6,622,500,000&nbsp;</td>
        <td class="Item_Price10">93.50&nbsp;</td>
        <td class="Item_Price10">95.60&nbsp;</td>
        <td class="Item_Price10">92.70&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl07_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">01/09/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl07_Td5" class="Item_Price10">92.70&nbsp;</td>
        <td class="Item_Price10">92.70&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>2.70 (3.00 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">675,310&nbsp;</td>
        <td class="Item_Price10">62,114,000,000&nbsp;</td>
        <td class="Item_Price10">0&nbsp;</td>
        <td class="LastItem_Price">0&nbsp;</td>
        <td class="Item_Price10">90.20&nbsp;</td>
        <td class="Item_Price10">94.00&nbsp;</td>
        <td class="Item_Price10">89.90&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl08_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">31/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl08_Td6" class="Item_Price10">90.00&nbsp;</td>
        <td class="Item_Price10">90.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>0.10 (0.11 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">276,580&nbsp;</td>
        <td class="Item_Price10">25,013,000,000&nbsp;</td>
        <td class="Item_Price10">502,261&nbsp;</td>
        <td class="LastItem_Price">46,190,462,230&nbsp;</td>
        <td class="Item_Price10">90.00&nbsp;</td>
        <td class="Item_Price10">91.50&nbsp;</td>
        <td class="Item_Price10">90.00&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl09_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">28/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl09_Td5" class="Item_Price10">89.90&nbsp;</td>
        <td class="Item_Price10">89.90&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Down>-1.10 (-1.21 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">636,020&nbsp;</td>
        <td class="Item_Price10">58,332,000,000&nbsp;</td>
        <td class="Item_Price10">55,000&nbsp;</td>
        <td class="LastItem_Price">5,045,700,000&nbsp;</td>
        <td class="Item_Price10">91.30&nbsp;</td>
        <td class="Item_Price10">92.30&nbsp;</td>
        <td class="Item_Price10">89.90&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl10_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">27/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl10_Td6" class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_NoChange>0.00 (0.00 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">437,950&nbsp;</td>
        <td class="Item_Price10">39,750,000,000&nbsp;</td>
        <td class="Item_Price10">40,000&nbsp;</td>
        <td class="LastItem_Price">3,640,000,000&nbsp;</td>
        <td class="Item_Price10">90.10&nbsp;</td>
        <td class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_Price10">90.10&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl11_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">26/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl11_Td5" class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_NoChange>0.00 (0.00 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">547,280&nbsp;</td>
        <td class="Item_Price10">49,684,000,000&nbsp;</td>
        <td class="Item_Price10">110,000&nbsp;</td>
        <td class="LastItem_Price">9,985,800,000&nbsp;</td>
        <td class="Item_Price10">90.80&nbsp;</td>
        <td class="Item_Price10">91.20&nbsp;</td>
        <td class="Item_Price10">90.00&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl12_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">25/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl12_Td6" class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_Price10">91.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>2.00 (2.25 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">1,074,660&nbsp;</td>
        <td class="Item_Price10">97,198,000,000&nbsp;</td>
        <td class="Item_Price10">0&nbsp;</td>
        <td class="LastItem_Price">0&nbsp;</td>
        <td class="Item_Price10">89.00&nbsp;</td>
        <td class="Item_Price10">91.90&nbsp;</td>
        <td class="Item_Price10">89.00&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl13_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">24/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl13_Td5" class="Item_Price10">89.00&nbsp;</td>
        <td class="Item_Price10">89.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>2.90 (3.37 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">1,052,840&nbsp;</td>
        <td class="Item_Price10">92,696,000,000&nbsp;</td>
        <td class="Item_Price10">102,000&nbsp;</td>
        <td class="LastItem_Price">9,009,660,000&nbsp;</td>
        <td class="Item_Price10">86.50&nbsp;</td>
        <td class="Item_Price10">89.00&nbsp;</td>
        <td class="Item_Price10">86.50&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl14_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">21/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl14_Td6" class="Item_Price10">86.10&nbsp;</td>
        <td class="Item_Price10">86.10&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>0.10 (0.12 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">376,790&nbsp;</td>
        <td class="Item_Price10">32,458,000,000&nbsp;</td>
        <td class="Item_Price10">100,000&nbsp;</td>
        <td class="LastItem_Price">8,612,000,000&nbsp;</td>
        <td class="Item_Price10">86.00&nbsp;</td>
        <td class="Item_Price10">86.90&nbsp;</td>
        <td class="Item_Price10">85.90&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl15_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">20/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl15_Td5" class="Item_Price10">86.00&nbsp;</td>
        <td class="Item_Price10">86.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Down>-0.50 (-0.58 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">990,220&nbsp;</td>
        <td class="Item_Price10">85,427,000,000&nbsp;</td>
        <td class="Item_Price10">0&nbsp;</td>
        <td class="LastItem_Price">0&nbsp;</td>
        <td class="Item_Price10">86.60&nbsp;</td>
        <td class="Item_Price10">87.20&nbsp;</td>
        <td class="Item_Price10">86.00&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl16_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">19/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl16_Td6" class="Item_Price10">86.50&nbsp;</td>
        <td class="Item_Price10">86.50&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_NoChange>0.00 (0.00 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">347,140&nbsp;</td>
        <td class="Item_Price10">30,200,000,000&nbsp;</td>
        <td class="Item_Price10">67,490&nbsp;</td>
        <td class="LastItem_Price">5,875,004,500&nbsp;</td>
        <td class="Item_Price10">86.50&nbsp;</td>
        <td class="Item_Price10">87.60&nbsp;</td>
        <td class="Item_Price10">86.50&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl17_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">18/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl17_Td5" class="Item_Price10">86.50&nbsp;</td>
        <td class="Item_Price10">86.50&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Down>-1.20 (-1.37 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">772,670&nbsp;</td>
        <td class="Item_Price10">67,004,000,000&nbsp;</td>
        <td class="Item_Price10">20,000&nbsp;</td>
        <td class="LastItem_Price">1,734,200,000&nbsp;</td>
        <td class="Item_Price10">87.30&nbsp;</td>
        <td class="Item_Price10">87.70&nbsp;</td>
        <td class="Item_Price10">86.20&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl18_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">17/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl18_Td6" class="Item_Price10">87.70&nbsp;</td>
        <td class="Item_Price10">87.70&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>0.30 (0.34 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">376,200&nbsp;</td>
        <td class="Item_Price10">32,876,000,000&nbsp;</td>
        <td class="Item_Price10">132,450&nbsp;</td>
        <td class="LastItem_Price">11,562,885,000&nbsp;</td>
        <td class="Item_Price10">87.70&nbsp;</td>
        <td class="Item_Price10">88.50&nbsp;</td>
        <td class="Item_Price10">86.80&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl19_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
        <td class="Item_DateItem">14/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl19_Td5" class="Item_Price10">87.40&nbsp;</td>
        <td class="Item_Price10">87.40&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Down>-0.60 (-0.68 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">654,070&nbsp;</td>
        <td class="Item_Price10">57,618,000,000&nbsp;</td>
        <td class="Item_Price10">0&nbsp;</td>
        <td class="LastItem_Price">0&nbsp;</td>
        <td class="Item_Price10">88.00&nbsp;</td>
        <td class="Item_Price10">89.00&nbsp;</td>
        <td class="Item_Price10">87.40&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl20_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
        <td class="Item_DateItem">13/08/2020</td>
        <td id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl20_Td6" class="Item_Price10">88.00&nbsp;</td>
        <td class="Item_Price10">88.00&nbsp;</td>
        <td class="Item_ChangePrice"><span class=Index_Up>0.60 (0.69 %)</span></td>
        <td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
        <td class="Item_Price10">458,680&nbsp;</td>
        <td class="Item_Price10">40,476,000,000&nbsp;</td>
        <td class="Item_Price10">134,000&nbsp;</td>
        <td class="LastItem_Price">11,824,160,000&nbsp;</td>
        <td class="Item_Price10">88.50&nbsp;</td>
        <td class="Item_Price10">89.00&nbsp;</td>
        <td class="Item_Price10">87.50&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
        <td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>

    
        </table>
<div style=" border-bottom: solid 0px #dadada;
    padding-bottom: 10px; text-align: right; float: right">
    <div style="float: right;">
        <table cellpadding="3" cellspacing="1" border="0" class="CafeF_Paging">
        <tr>
                <td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','1')" title=" Back to Page 1"> < </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','1')"  > 1 </a></td><td align="center" style="width: 20px"><span   ><strong> 2 </strong></span></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','3')"  > 3 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','4')"  > 4 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','5')"  > 5 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','6')"  > 6 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','7')"  > 7 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','8')"  > 8 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','9')"  > 9 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','10')"  > 10 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','11')"  > 11 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','12')"  > 12 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','13')"  > 13 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','14')"  > 14 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','15')"  > 15 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','16')"  > 16 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','17')"  > 17 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','18')"  > 18 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','19')"  > 19 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','20')"  > 20 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager2','3')" title=" Next to Page 3"> > </a></td>
        </tr>
</table><span id="ctl00_ContentPlaceHolder1_ctl03_pager2"></span></i></td> </div>
</div>
</div>

    |0|hiddenField|__EVENTTARGET||0|hiddenField|__EVENTARGUMENT||156|hiddenField|__VIEWSTATE|/wEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ==|8|hiddenField|__VIEWSTATEGENERATOR|2E2252AF|79|asyncPostBackControlIDs||ctl00$ContentPlaceHolder1$ctl03$pager2,ctl00$ContentPlaceHolder1$ctl03$btSearch|0|postBackControlIDs|||129|updatePanelIDs||fctl00$ContentPlaceHolder1$LabelUpdatePanel,fctl00$ContentPlaceHolder1$LinkUpdatePanel,tctl00$ContentPlaceHolder1$ctl03$panelAjax|0|childUpdatePanelIDs|||126|panelsToRefreshIDs||ctl00$ContentPlaceHolder1$LabelUpdatePanel,ctl00$ContentPlaceHolder1$LinkUpdatePanel,ctl00$ContentPlaceHolder1$ctl03$panelAjax|2|asyncPostBackTimeout||90|28|formAction||/Lich-su-giao-dich-VIC-1.chn|
'''
if __name__=="__main__":
    lst_data = []
    s = soup(_str, features='lxml').table
    start = 0
    lst_data = []
    for tr in s.find_all('tr', recursive=False):
        for i, td in enumerate(tr.find_all('td', recursive=False)):
            # print(td)
            if start > 1:
                data = {}
                for i, td in enumerate(tr.find_all('td', recursive=False)):
                    print(td)
        #         if i % 15 == 0:
        #             data['Ngày'] =  td.text.replace(u'\xa0', u'')
        #         elif i % 15 == 1:
        #             data['Giá Điều Chỉnh'] =  float(td.text.replace(u'\xa0', u''))
        #         elif i % 15 == 2:
        #             data['Giá Đóng Cửa'] =  float(td.text.replace(u'\xa0', u''))
        #         elif i % 15 == 3:
        #             data['Thay Đổi'] = float(td.text.split('(')[0])
        #             data["Thay Đổi Theo %"] = float(td.text.split('(')[1].strip()[:-2])
        #         elif i % 15 == 5:
        #             data['KL GD Khớp Lệnh'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
        #         elif i % 15 == 6:
        #             data['GT GD Khớp Lệnh'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
        #         elif i % 15 == 7:
        #             data['KL GD Thỏa Thuận'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
        #         elif i % 15 == 8:
        #             data['GT GD Thỏa Thuận'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
        #         elif i % 15 == 9:
        #             data['Giá Mở Cửa'] =  float(td.text.replace(u'\xa0', u''))
        #         elif i % 15 == 10:
        #             data['Giá Cao Nhất'] =  float(td.text.replace(u'\xa0', u''))
        #         elif i % 15 == 11:
        #             data['Giá Thấp Nhất'] =  float(td.text.replace(u'\xa0', u''))
        #         print(data)