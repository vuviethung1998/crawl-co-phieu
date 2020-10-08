import json
from bs4 import BeautifulSoup as soup

_str = '''380|updatePanel|ctl00_ContentPlaceHolder1_LabelUpdatePanel|
                                <h1 itemprop="name" style="font-weight:bold;font-size:12px">THỐNG KÊ ĐẶT LỆNH - Mã CK VIC - <a href='http://s.cafef.vn/hose/VIC-tap-doan-vingroup-cong-ty-co-phan.chn' style='color:#fff; font-weigth: normal;'>Hồ sơ công ty</a></h1><span style="color: rgb(255, 255, 204);">
                                    </span>
                            |3980|updatePanel|ctl00_ContentPlaceHolder1_LinkUpdatePanel|
                        <div id="ctl00_ContentPlaceHolder1_divDataHistory" class="cf_ResearchDataHistory_Tab1">
                            <div class="ResearchDataHistory_BoxHeader"><div></div></div>
                            <div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(1);"><a href="/Lich-su-giao-dich-VIC-1.chn#data" id="ctl00_ContentPlaceHolder1_aLSG">Lịch sử giá</a></div>
                        </div>
                        <div class="splitter"></div>
                        <div id="ctl00_ContentPlaceHolder1_divCungCau" class="cf_ThongKeDatLenh_Selected">
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
                        
                        |23545|updatePanel|ctl00_ContentPlaceHolder1_ctl03_panelAjax|
<div style="background-color:#FFF;width:100%;float:left" align="center">

       
    <table cellpadding="2" cellspacing="0" width="100%" style="border-top: solid 1px #e6e6e6"
            class="GirdTable">
            <tr style="border-bottom: solid 1px #e6e6e6; font-family: Arial; font-size: 10px;
                font-weight: bold; color: #004276; background-color: #FFF">
                <td class="Header_DateItem" style="height:30px;width:6%">Ngày</td>
                <td class="Header_Price" style="height:30px;width:10%">Thay đổi (+/-%)</td>    
                <td class="Header_ChangeItem" style="height:30px;width:6%">Số lệnh <br /> mua</td>
                <td class="Header_Price" style="height:30px;width:6%">Khối lượng <br /> đặt mua</td>
                  <td class="Header_ChangeItem" style="height:30px;width:6%"><i> KLTB <br /> 1 lệnh mua</i> </td>    
                <td class="Header_Price" style="height:30px;width:6%">Số lệnh đặt bán</td>
                <td class="Header_Price" style="height:30px;width:6%">Khối lượng <br /> đặt bán</td>
                  <td class="Header_ChangeItem" style="height:30px;width:6%"><i>KLTB <br /> 1 lệnh bán</i> </td>    
                <td class="Header_Price" style="height:30px;width:10%">Chênh lệch KL <br/> đặt mua - đặt bán</td>
            </tr> 
    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl01_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">10/09/2020</td>
	<td class="Item_Price" style="height:30px;">90.5<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,289&nbsp;</td>
	<td class="Item_Price" style="height:30px;">737,500&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">572 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">877&nbsp;</td>
	<td class="Item_Price" style="height:30px;">711,270&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">811 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">26,230</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl02_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">09/09/2020</td>
	<td class="Item_Price" style="height:30px;">90.5<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">2,590&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,361,860&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">526 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,340&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,282,610&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">957 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">79,250</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl03_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">08/09/2020</td>
	<td class="Item_Price" style="height:30px;">90.5<span class=Index_Down> (-1.1 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,827&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,244,140&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">681 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">955&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,057,160&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,107 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">186,980</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl04_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">07/09/2020</td>
	<td class="Item_Price" style="height:30px;">91.5<span class=Index_Down> (-2.7 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,365&nbsp;</td>
	<td class="Item_Price" style="height:30px;">738,170&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">541 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,191&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,455,200&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,222 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-717,030</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl05_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">04/09/2020</td>
	<td class="Item_Price" style="height:30px;">94<span class=Index_Down> (-0.5 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,585&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,174,550&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">741 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,868&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,271,360&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">681 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-96,810</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl06_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">03/09/2020</td>
	<td class="Item_Price" style="height:30px;">94.5<span class=Index_Up> (1.9 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,323&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,613,110&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,219 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">2,354&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,871,140&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">795 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-258,030</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl07_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">01/09/2020</td>
	<td class="Item_Price" style="height:30px;">92.7<span class=Index_Up> (3.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,146&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,137,350&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">992 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,965&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,278,980&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">651 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-141,630</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl08_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">31/08/2020</td>
	<td class="Item_Price" style="height:30px;">90<span class=Index_Up> (0.1 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">954&nbsp;</td>
	<td class="Item_Price" style="height:30px;">562,600&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">590 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">924&nbsp;</td>
	<td class="Item_Price" style="height:30px;">869,420&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">941 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-306,820</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl09_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">28/08/2020</td>
	<td class="Item_Price" style="height:30px;">89.9<span class=Index_Down> (-1.2 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">755&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,001,650&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,327 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,836&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,269,360&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">691 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-267,710</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl10_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">27/08/2020</td>
	<td class="Item_Price" style="height:30px;">91<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">687&nbsp;</td>
	<td class="Item_Price" style="height:30px;">836,640&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,218 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">932&nbsp;</td>
	<td class="Item_Price" style="height:30px;">984,940&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,057 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-148,300</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl11_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">26/08/2020</td>
	<td class="Item_Price" style="height:30px;">91<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,335&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,053,100&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">789 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,734&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,168,150&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">674 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-115,050</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl12_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">25/08/2020</td>
	<td class="Item_Price" style="height:30px;">91<span class=Index_Up> (2.2 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,375&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,710,680&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,244 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">2,889&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,774,590&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">614 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-63,910</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl13_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">24/08/2020</td>
	<td class="Item_Price" style="height:30px;">89<span class=Index_Up> (3.4 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,475&nbsp;</td>
	<td class="Item_Price" style="height:30px;">2,179,300&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,477 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">2,027&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,781,540&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">879 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">397,760</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl14_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">21/08/2020</td>
	<td class="Item_Price" style="height:30px;">86.1<span class=Index_Up> (0.1 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,248&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,136,400&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">911 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,029&nbsp;</td>
	<td class="Item_Price" style="height:30px;">906,730&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">881 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">229,670</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl15_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">20/08/2020</td>
	<td class="Item_Price" style="height:30px;">86<span class=Index_Down> (-0.6 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,764&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,686,490&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">956 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">2,281&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,972,680&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">865 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-286,190</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl16_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">19/08/2020</td>
	<td class="Item_Price" style="height:30px;">86.5<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">993&nbsp;</td>
	<td class="Item_Price" style="height:30px;">745,810&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">751 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">881&nbsp;</td>
	<td class="Item_Price" style="height:30px;">657,460&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">746 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">88,350</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl17_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">18/08/2020</td>
	<td class="Item_Price" style="height:30px;">86.5<span class=Index_Down> (-1.4 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">2,237&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,184,930&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">530 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,402&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,172,980&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">837 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">11,950</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl18_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">17/08/2020</td>
	<td class="Item_Price" style="height:30px;">87.7<span class=Index_Up> (0.3 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,399&nbsp;</td>
	<td class="Item_Price" style="height:30px;">638,620&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">456 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">932&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,044,400&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">1,121 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-405,780</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl19_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height:30px;">14/08/2020</td>
	<td class="Item_Price" style="height:30px;">87.4<span class=Index_Down> (-0.7 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,257&nbsp;</td>
	<td class="Item_Price" style="height:30px;">989,230&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">787 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,277&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,236,360&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">968 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-247,130</td>
</tr>

    
        <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl20_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #fff">
	<td class="Item_DateItem" style="height:30px;">13/08/2020</td>
	<td class="Item_Price" style="height:30px;">88<span class=Index_Up> (0.7 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' alt='' /> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,121&nbsp;</td>
	<td class="Item_Price" style="height:30px;">857,390&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">765 &nbsp;</td>
	<td class="Item_Price" style="height:30px;">1,146&nbsp;</td>
	<td class="Item_Price" style="height:30px;">876,050&nbsp;</td>
	<td class="Item_Price" style="height:30px;font-style:italic;">764 &nbsp;</td>
	<td class="Item_Price" style="height:30px;padding-right:8px">-18,660</td>
</tr>

    </table>
        
<div style="border-bottom: solid 0px #dadada;padding-bottom: 10px; text-align: right; float: right">
    <div style="float: right;">
        <table cellpadding="3" cellspacing="1" border="0" class="CafeF_Paging">
	<tr>
		<td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','1')" title=" Back to Page 1"> < </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','1')"  > 1 </a></td><td align="center" style="width: 20px"><span   ><strong> 2 </strong></span></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','3')"  > 3 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','4')"  > 4 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','5')"  > 5 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','6')"  > 6 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','7')"  > 7 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','8')"  > 8 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','9')"  > 9 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','10')"  > 10 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','11')"  > 11 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','12')"  > 12 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','13')"  > 13 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','14')"  > 14 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','15')"  > 15 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','16')"  > 16 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','17')"  > 17 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','18')"  > 18 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','19')"  > 19 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','20')"  > 20 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','3')" title=" Next to Page 3"> > </a></td>
	</tr>
</table><span id="ctl00_ContentPlaceHolder1_ctl03_pager1"></span>
    </div>
</div>
</div>
 |0|hiddenField|__EVENTTARGET||0|hiddenField|__EVENTARGUMENT||156|hiddenField|__VIEWSTATE|/wEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ==|8|hiddenField|__VIEWSTATEGENERATOR|2E2252AF|79|asyncPostBackControlIDs||ctl00$ContentPlaceHolder1$ctl03$pager1,ctl00$ContentPlaceHolder1$ctl03$btSearch|0|postBackControlIDs|||129|updatePanelIDs||fctl00$ContentPlaceHolder1$LabelUpdatePanel,fctl00$ContentPlaceHolder1$LinkUpdatePanel,tctl00$ContentPlaceHolder1$ctl03$panelAjax|0|childUpdatePanelIDs|||126|panelsToRefreshIDs||ctl00$ContentPlaceHolder1$LabelUpdatePanel,ctl00$ContentPlaceHolder1$LinkUpdatePanel,ctl00$ContentPlaceHolder1$ctl03$panelAjax|2|asyncPostBackTimeout||90|28|formAction||/Lich-su-giao-dich-VIC-2.chn|
'''

if __name__=="__main__":
    lst_data = []
    s = soup(_str, features='lxml').table
    start = 0
    lst_data = []
    for tr in s.find_all('tr', recursive=False):
        if start >= 1:
            data = {}
            for i, td in enumerate(tr.find_all('td', recursive=False)):
                if i % 9 == 0:
                    data['Ngày'] =  td.text.replace(u'\xa0', u'')
                elif i % 9 == 1:
                    data['Thay Đổi'] = float(td.text.split('(')[0])
                    data["Thay Đổi Theo %"] = float(td.text.split('(')[1].strip()[:-2])
                elif i % 9 == 2:
                    data['Số lệnh mua'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                elif i % 9 == 3:
                    data['Khối lượng đặt mua'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                elif i % 9 == 4:
                    data['KLTB 1 lệnh mua'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                elif i % 9 == 5:
                    data['Số lệnh bán'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                elif i % 9 == 6:
                    data['Khối lượng đặt bán'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                elif i % 9 == 7:
                    data['KLTB 1 lệnh bán'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                elif i % 9 == 8:
                    data['Chênh lệch KL đặt mua - đặt bán'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
            lst_data.append(data)
        start += 1
    print(lst_data)