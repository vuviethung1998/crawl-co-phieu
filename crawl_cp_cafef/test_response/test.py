import json
from bs4 import BeautifulSoup as soup

_str = '''379|updatePanel|ctl00_ContentPlaceHolder1_LabelUpdatePanel|
                                <h1 itemprop="name" style="font-weight:bold;font-size:12px">GDNDT NƯỚC NGOÀI - Mã CK VIC - <a href='http://s.cafef.vn/hose/VIC-tap-doan-vingroup-cong-ty-co-phan.chn' style='color:#fff; font-weigth: normal;'>Hồ sơ công ty</a></h1><span style="color: rgb(255, 255, 204);">
                                    </span>
                            |3980|updatePanel|ctl00_ContentPlaceHolder1_LinkUpdatePanel|
                        <div id="ctl00_ContentPlaceHolder1_divDataHistory" class="cf_ResearchDataHistory_Tab1">
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
                        <div id="ctl00_ContentPlaceHolder1_divGDNN" class="cf_ResearchDataHistory_Selected" style="width: 145px;">
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
                        
                        |25837|updatePanel|ctl00_ContentPlaceHolder1_ctl03_panelAjax|
        <div style="background-color: #FFF; width: 100%; float: left" align="center">
            
                    <table cellpadding="2" cellspacing="0" width="100%" style="border-top: solid 1px #e6e6e6"
                        class="GirdTable">
                        <tr style="border-bottom: solid 1px #e6e6e6; font-family: Arial; font-size: 12px;
                            font-weight: bold; color: #004276; background-color: #FFF">
                            <td class="Header_DateItem" rowspan="2" style="height: 30px; width: 6%">Ngày</td>
                            <td class="Header_Price" rowspan="2" style="height: 30px; width: 8%">KL giao<br />dịch ròng</td>
                            <td class="Header_Price" rowspan="2" style="height: 30px; width: 10%">Giá trị giao<br />dịch ròng</td>
                            <td class="Header_Price" rowspan="2" style="height: 30px; width: 12%">Thay đổi (+/-%)</td>
                            <td colspan="2" class="GDNN_Header" style="height: 30px; width: 7%">Mua</td>
                            <td colspan="2" class="GDNN_Header" style="height: 30px; width: 7%">Bán</td>
                            <td class="Header_Price" rowspan="2" style="height: 30px; width: 10%">Room còn lại</td>
                            <td class="Header_Price" rowspan="2" style="height: 30px; width: 9%">Đang sở hữu</td>
                        </tr>
                        <tr>
                            <td class="Header_Price" style="font-size: 12px; font-family: arial; height: 30px;width: 7%">Khối lượng</td>
                            <td class="Header_Price" style="font-size: 12px; font-family: arial; height: 30px;width: 9%">Giá trị</td>
                            <td class="Header_Price" style="font-size: 12px; font-family: arial; height: 30px;width: 7%">Khối lượng</td>
                            <td class="Header_Price" style="font-size: 12px; font-family: arial; height: 30px;width: 9%">Giá trị</td>
                        </tr>
                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl01_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">10/09/2020</td>
	<td class="Item_Price" style="height: 30px;">-132,460&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-12,012,410,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">90.5<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">245,440&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">22,390,470,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">377,900&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">34,402,880,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">773,717,451&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.55%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl02_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">09/09/2020</td>
	<td class="Item_Price" style="height: 30px;">-97,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-8,749,379,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">90.5<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">389,930&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">35,189,064,740&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">486,930&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">43,938,443,740&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">774,592,880&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.77%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl03_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">08/09/2020</td>
	<td class="Item_Price" style="height: 30px;">-1,181,880&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-110,300,580,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">90.5<span class=Index_Down> (-1.1 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">85,010&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">7,739,260,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">1,266,890&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">118,039,840,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">773,508,341&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.55%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl04_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">07/09/2020</td>
	<td class="Item_Price" style="height: 30px;">68,380&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">6,428,025,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">91.5<span class=Index_Down> (-2.7 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">175,760&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">16,510,781,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">107,380&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">10,082,756,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">773,314,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.81%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl05_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">04/09/2020</td>
	<td class="Item_Price" style="height: 30px;">-100,450&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-9,383,090,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">94<span class=Index_Down> (-0.5 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">362,840&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">34,245,880,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">463,290&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">43,628,970,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">773,232,001&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.56%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl06_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">03/09/2020</td>
	<td class="Item_Price" style="height: 30px;">73,270&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">7,011,440,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">94.5<span class=Index_Up> (1.9 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">531,670&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">50,422,910,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">458,400&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">43,411,470,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,975,870&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.57%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl07_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">01/09/2020</td>
	<td class="Item_Price" style="height: 30px;">76,330&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">6,939,088,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">92.7<span class=Index_Up> (3.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">199,030&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">18,226,492,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">122,700&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">11,287,404,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">773,355,200&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.81%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl08_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">31/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-533,321&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-48,989,924,318&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">90<span class=Index_Up> (0.1 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">85,650&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">7,740,293,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">618,971&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">56,730,217,318&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,974,200&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.82%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl09_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">28/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-240,430&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-22,020,981,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">89.9<span class=Index_Down> (-1.2 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">60,940&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">5,581,762,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">301,370&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">27,602,743,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,440,879&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.84%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl10_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">27/08/2020</td>
	<td class="Item_Price" style="height: 30px;">323,590&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">29,381,380,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">91<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">359,830&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">32,669,700,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">36,240&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">3,288,320,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">773,083,590&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.56%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl11_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">26/08/2020</td>
	<td class="Item_Price" style="height: 30px;">189,450&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">17,220,780,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">91<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">421,520&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">38,294,150,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">232,070&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">21,073,370,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,859,350&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.57%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl12_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">25/08/2020</td>
	<td class="Item_Price" style="height: 30px;">38,640&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">3,476,587,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">91<span class=Index_Up> (2.2 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">302,160&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">27,385,383,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">263,520&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">23,908,796,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,673,489&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.83%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl13_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">24/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-229,160&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-20,161,288,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">89<span class=Index_Up> (3.4 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">330,710&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">29,092,561,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">559,870&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">49,253,849,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,712,129&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.83%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl14_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">21/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-298,960&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-25,748,250,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">86.1<span class=Index_Up> (0.1 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">143,180&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">12,333,210,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">442,140&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">38,081,460,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,772,313&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.57%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl15_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">20/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-337,050&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-29,078,100,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">86<span class=Index_Down> (-0.6 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">106,900&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">9,240,520,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">443,950&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">38,318,620,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,187,080&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.59%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl16_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">19/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-48,780&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-4,206,290,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">86.5<span class=Index_NoChange> (0.0 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/nochange_.jpg' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">230,160&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">20,048,400,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">278,940&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">24,254,690,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">772,193,650&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.59%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl17_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">18/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-412,020&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-35,745,240,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">86.5<span class=Index_Down> (-1.4 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">236,400&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">20,501,020,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">648,420&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">56,246,260,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">771,946,850&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.60%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl18_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">17/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-19,020&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-1,683,360,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">87.7<span class=Index_Up> (0.3 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">213,760&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">18,665,960,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">232,780&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">20,349,320,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">771,899,280&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.60%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl19_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #f2f2f2">
	<td class="Item_DateItem" style="height: 30px;">14/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-232,320&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-20,438,128,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">87.4<span class=Index_Down> (-0.7 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">177,150&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">15,579,414,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">409,470&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">36,017,542,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">771,367,139&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.87%&nbsp;</td>
</tr>

                
                    <tr id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl20_Tr1" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF">
	<td class="Item_DateItem" style="height: 30px;">13/08/2020</td>
	<td class="Item_Price" style="height: 30px;">-1,050&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">-95,230,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">88<span class=Index_Up> (0.7 %)</span> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle'> &nbsp;&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">370,300&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">32,671,350,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">371,350&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">32,766,580,000&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">771,762,291&nbsp;</td>
	<td class="Item_Price" style="height: 30px;">13.60%&nbsp;</td>
</tr>

                
                    </table>
            <div style=" border-bottom: solid 0px #dadada;
                padding-bottom: 10px; text-align: right; float: right">
                <div style="float: right;">
                    <table cellpadding="3" cellspacing="1" border="0" class="CafeF_Paging">
	<tr>
		<td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','1')" title=" Back to Page 1"> < </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','1')"  > 1 </a></td><td align="center" style="width: 20px"><span   ><strong> 2 </strong></span></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','3')"  > 3 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','4')"  > 4 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','5')"  > 5 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','6')"  > 6 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','7')"  > 7 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','8')"  > 8 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','9')"  > 9 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','10')"  > 10 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','11')"  > 11 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','12')"  > 12 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','13')"  > 13 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','14')"  > 14 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','15')"  > 15 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','16')"  > 16 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','17')"  > 17 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','18')"  > 18 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','19')"  > 19 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','20')"  > 20 </a></td><td align="center" style="width: 20px"><a  href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1','3')" title=" Next to Page 3"> > </a></td>
	</tr>
</table><span id="ctl00_ContentPlaceHolder1_ctl03_pager1"></span>
                </div>
            </div>
        </div>
    |0|hiddenField|__EVENTTARGET||0|hiddenField|__EVENTARGUMENT||156|hiddenField|__VIEWSTATE|/wEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ==|8|hiddenField|__VIEWSTATEGENERATOR|2E2252AF|79|asyncPostBackControlIDs||ctl00$ContentPlaceHolder1$ctl03$pager1,ctl00$ContentPlaceHolder1$ctl03$btSearch|0|postBackControlIDs|||129|updatePanelIDs||fctl00$ContentPlaceHolder1$LabelUpdatePanel,fctl00$ContentPlaceHolder1$LinkUpdatePanel,tctl00$ContentPlaceHolder1$ctl03$panelAjax|0|childUpdatePanelIDs|||126|panelsToRefreshIDs||ctl00$ContentPlaceHolder1$LabelUpdatePanel,ctl00$ContentPlaceHolder1$LinkUpdatePanel,ctl00$ContentPlaceHolder1$ctl03$panelAjax|2|asyncPostBackTimeout||90|28|formAction||/Lich-su-giao-dich-VIC-3.chn|
'''

if __name__=="__main__":
    lst_data = []
    s = soup(_str, features='lxml').table
    start = 0
    lst_data = []
    for tr in s.find_all('tr', recursive=False):
        if start > 1:
            data = {}
            for i, td in enumerate(tr.find_all('td', recursive=False)):
                print(td.text)
            #     if i % 9 == 0:
            #         data['Ngày'] =  td.text.replace(u'\xa0', u'')
            #     elif i % 9 == 1:
            #         data['Thay Đổi'] = float(td.text.split('(')[0])
            #         data["Thay Đổi Theo %"] = float(td.text.split('(')[1].strip()[:-2])
            #     elif i % 9 == 2:
            #         data['Số lệnh mua'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
            #     elif i % 9 == 3:
            #         data['Khối lượng đặt mua'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
            #     elif i % 9 == 4:
            #         data['KLTB 1 lệnh mua'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
            #     elif i % 9 == 5:
            #         data['Số lệnh bán'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
            #     elif i % 9 == 6:
            #         data['Khối lượng đặt bán'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
            #     elif i % 9 == 7:
            #         data['KLTB 1 lệnh bán'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
            #     elif i % 9 == 8:
            #         data['Chênh lệch KL đặt mua - đặt bán'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
            # lst_data.append(data)
        start += 1
