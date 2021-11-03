import json
from bs4 import BeautifulSoup as soup

_str = '''236|updatePanel|ctl00_ContentPlaceHolder1_LabelUpdatePanel|
<h1 itemprop="name" style="font-weight:bold;font-size:12px">LỊCH SỬ GIÁ - VNINDEX</h1><span style="color: rgb(255, 255, 204);">
</span>
|2739|updatePanel|ctl00_ContentPlaceHolder1_LinkUpdatePanel|
<div id="ctl00_ContentPlaceHolder1_divDataHistory" class="cf_ResearchDataHistory_Tab1_Sel">
<div class="ResearchDataHistory_BoxHeader"><div></div></div>
<div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(1);"><a href="/Lich-su-giao-dich-VNINDEX-1.chn#data" id="ctl00_ContentPlaceHolder1_aLSG">Lịch sử giá</a></div>
</div>
<div class="splitter"></div>
<div id="ctl00_ContentPlaceHolder1_divCungCau" class="cf_ThongKeDatLenh">
<div class="ResearchDataHistory_BoxHeader"><div></div></div>
<div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(2);">
<a href="/Lich-su-giao-dich-VNINDEX-2.chn#data" id="ctl00_ContentPlaceHolder1_aTKL">Thống kê đặt lệnh</a>
</div>
</div>
<div class="splitter" style='display:none'></div>

<div class="splitter"></div>
<div id="ctl00_ContentPlaceHolder1_divGDNN" class="cf_ResearchDataHistory" style="width: 145px;">
<div class="ResearchDataHistory_BoxHeader" style="background-image: url('http://cafef3.vcmedia.vn/v2/images/history_top_145.gif');"><div></div></div>
<div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(3);">
<a href="/Lich-su-giao-dich-VNINDEX-3.chn#data" id="ctl00_ContentPlaceHolder1_aNDTNG">Giao dịch khối ngoại</a>
</div>
</div>
<div class="splitter" style='display:none'></div>

<div class="splitter" style='display:none'></div>

<div class="splitter"></div>
<div id="ctl00_ContentPlaceHolder1_divGiaoDichTuDoanh" class="cf_ResearchDataHistory" style="width: 155px;">
<div class="ResearchDataHistory_BoxHeader" style="background-image: url('http://cafef3.vcmedia.vn/v2/images/history_top_155.gif');"><div></div></div>
<div class="ResearchDataHistory_BoxContent" onclick="javascript:changeTabXemLichSu(7);">
<a href="/Lich-su-giao-dich-VNINDEX-7.chn#data" id="ctl00_ContentPlaceHolder1_aGDTD">Giao dịch tự doanh</a>
</div>
</div>
|26885|updatePanel|ctl00_ContentPlaceHolder1_ctl03_panelAjax|

<div id="ctl00_ContentPlaceHolder1_ctl03_divHO" style="background-color:#FFF;width:100%;float:left" align="center">
<table cellpadding="2" cellspacing="0" width="100%" style="border-top: solid 1px #e6e6e6"
id="GirdTable2">
<tr style="border-bottom: solid 1px #e6e6e6; font-family: Arial; font-size: 10px;
font-weight: bold; color: #004276; background-color: #FFF" >
<td rowspan="2" class="Header_DateItem" style="width:6%">Ngày</td>

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
<td class="Item_DateItem">24/12/2020</td>
<td class="Item_Price10">1,067.52&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Down>-11.38 (-1.05 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">658,279,720&nbsp;</td>
<td class="Item_Price10">12,911,061,230,000&nbsp;</td>
<td class="Item_Price10">68,652,918&nbsp;</td>
<td class="LastItem_Price">1,097,867,980,500&nbsp;</td>
<td class="Item_Price10">1,083.83&nbsp;</td>
<td class="Item_Price10">1,084.76&nbsp;</td>
<td class="Item_Price10">1,046.89&nbsp;</td>
<td style="display:none;" class="Item_Price10">23,601,260&nbsp;</td>
<td style="display:none;" class="Item_Price10">657,668,110&nbsp;</td>
<td style="display:none;" class="Item_Price10">1,698,182&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl02_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">23/12/2020</td>
<td class="Item_Price10">1,078.90&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Down>-4.55 (-0.42 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">711,447,510&nbsp;</td>
<td class="Item_Price10">13,502,241,180,000&nbsp;</td>
<td class="Item_Price10">67,324,990&nbsp;</td>
<td class="LastItem_Price">1,257,813,122,660&nbsp;</td>
<td class="Item_Price10">1,087.89&nbsp;</td>
<td class="Item_Price10">1,094.09&nbsp;</td>
<td class="Item_Price10">1,077.92&nbsp;</td>
<td style="display:none;" class="Item_Price10">40,711,590&nbsp;</td>
<td style="display:none;" class="Item_Price10">612,993,166&nbsp;</td>
<td style="display:none;" class="Item_Price10">66,641,980&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl03_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">22/12/2020</td>
<td class="Item_Price10">1,083.45&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>2.37 (0.22 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">661,706,010&nbsp;</td>
<td class="Item_Price10">12,732,483,000,000&nbsp;</td>
<td class="Item_Price10">57,180,437&nbsp;</td>
<td class="LastItem_Price">1,654,108,948,620&nbsp;</td>
<td class="Item_Price10">1,081.85&nbsp;</td>
<td class="Item_Price10">1,084.23&nbsp;</td>
<td class="Item_Price10">1,077.06&nbsp;</td>
<td style="display:none;" class="Item_Price10">8,262,749&nbsp;</td>
<td style="display:none;" class="Item_Price10">529,093,685&nbsp;</td>
<td style="display:none;" class="Item_Price10">40,312,267&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl04_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">21/12/2020</td>
<td class="Item_Price10">1,081.08&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>13.62 (1.28 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">626,766,500&nbsp;</td>
<td class="Item_Price10">12,975,784,000,000&nbsp;</td>
<td class="Item_Price10">43,857,383&nbsp;</td>
<td class="LastItem_Price">1,038,990,766,200&nbsp;</td>
<td class="Item_Price10">1,071.62&nbsp;</td>
<td class="Item_Price10">1,081.60&nbsp;</td>
<td class="Item_Price10">1,067.46&nbsp;</td>
<td style="display:none;" class="Item_Price10">7,321,965&nbsp;</td>
<td style="display:none;" class="Item_Price10">538,336,831&nbsp;</td>
<td style="display:none;" class="Item_Price10">25,350,257&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl05_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">18/12/2020</td>
<td class="Item_Price10">1,067.46&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>15.69 (1.49 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">526,524,670&nbsp;</td>
<td class="Item_Price10">11,651,496,000,000&nbsp;</td>
<td class="Item_Price10">52,812,573&nbsp;</td>
<td class="LastItem_Price">1,244,704,251,350&nbsp;</td>
<td class="Item_Price10">1,055.75&nbsp;</td>
<td class="Item_Price10">1,068.56&nbsp;</td>
<td class="Item_Price10">1,051.77&nbsp;</td>
<td style="display:none;" class="Item_Price10">18,017,591&nbsp;</td>
<td style="display:none;" class="Item_Price10">383,391,847&nbsp;</td>
<td style="display:none;" class="Item_Price10">60,250,342&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl06_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">17/12/2020</td>
<td class="Item_Price10">1,051.77&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Down>-15.22 (-1.43 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">596,966,690&nbsp;</td>
<td class="Item_Price10">13,524,118,260,000&nbsp;</td>
<td class="Item_Price10">25,666,998&nbsp;</td>
<td class="LastItem_Price">687,578,071,300&nbsp;</td>
<td class="Item_Price10">1,065.85&nbsp;</td>
<td class="Item_Price10">1,066.99&nbsp;</td>
<td class="Item_Price10">1,051.42&nbsp;</td>
<td style="display:none;" class="Item_Price10">6,131,821&nbsp;</td>
<td style="display:none;" class="Item_Price10">542,191,367&nbsp;</td>
<td style="display:none;" class="Item_Price10">31,737,406&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl07_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">16/12/2020</td>
<td class="Item_Price10">1,066.99&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>11.72 (1.11 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">530,251,460&nbsp;</td>
<td class="Item_Price10">10,864,766,000,000&nbsp;</td>
<td class="Item_Price10">26,586,761&nbsp;</td>
<td class="LastItem_Price">729,734,433,000&nbsp;</td>
<td class="Item_Price10">1,058.34&nbsp;</td>
<td class="Item_Price10">1,066.99&nbsp;</td>
<td class="Item_Price10">1,055.27&nbsp;</td>
<td style="display:none;" class="Item_Price10">9,239,856&nbsp;</td>
<td style="display:none;" class="Item_Price10">437,157,855&nbsp;</td>
<td style="display:none;" class="Item_Price10">21,086,670&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl08_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">15/12/2020</td>
<td class="Item_Price10">1,055.27&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Down>-8.82 (-0.83 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">579,155,230&nbsp;</td>
<td class="Item_Price10">12,170,625,000,000&nbsp;</td>
<td class="Item_Price10">38,939,220&nbsp;</td>
<td class="LastItem_Price">978,862,006,400&nbsp;</td>
<td class="Item_Price10">1,062.02&nbsp;</td>
<td class="Item_Price10">1,067.45&nbsp;</td>
<td class="Item_Price10">1,052.01&nbsp;</td>
<td style="display:none;" class="Item_Price10">8,983,003&nbsp;</td>
<td style="display:none;" class="Item_Price10">444,753,252&nbsp;</td>
<td style="display:none;" class="Item_Price10">56,053,306&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl09_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">14/12/2020</td>
<td class="Item_Price10">1,064.09&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>18.13 (1.73 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">471,507,860&nbsp;</td>
<td class="Item_Price10">10,338,291,000,000&nbsp;</td>
<td class="Item_Price10">60,713,038&nbsp;</td>
<td class="LastItem_Price">1,891,557,607,530&nbsp;</td>
<td class="Item_Price10">1,048.97&nbsp;</td>
<td class="Item_Price10">1,064.09&nbsp;</td>
<td class="Item_Price10">1,045.96&nbsp;</td>
<td style="display:none;" class="Item_Price10">5,931,206&nbsp;</td>
<td style="display:none;" class="Item_Price10">389,367,231&nbsp;</td>
<td style="display:none;" class="Item_Price10">40,589,266&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl10_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">11/12/2020</td>
<td class="Item_Price10">1,045.96&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>15.05 (1.46 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">387,847,600&nbsp;</td>
<td class="Item_Price10">8,676,369,820,000&nbsp;</td>
<td class="Item_Price10">35,023,027&nbsp;</td>
<td class="LastItem_Price">1,517,419,327,700&nbsp;</td>
<td class="Item_Price10">1,033.19&nbsp;</td>
<td class="Item_Price10">1,045.96&nbsp;</td>
<td class="Item_Price10">1,030.06&nbsp;</td>
<td style="display:none;" class="Item_Price10">11,743,248&nbsp;</td>
<td style="display:none;" class="Item_Price10">306,621,270&nbsp;</td>
<td style="display:none;" class="Item_Price10">20,229,780&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl11_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">10/12/2020</td>
<td class="Item_Price10">1,030.91&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Down>-8.22 (-0.79 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">520,204,600&nbsp;</td>
<td class="Item_Price10">11,459,379,000,000&nbsp;</td>
<td class="Item_Price10">49,060,107&nbsp;</td>
<td class="LastItem_Price">1,490,818,881,400&nbsp;</td>
<td class="Item_Price10">1,041.65&nbsp;</td>
<td class="Item_Price10">1,044.10&nbsp;</td>
<td class="Item_Price10">1,030.91&nbsp;</td>
<td style="display:none;" class="Item_Price10">9,700,264&nbsp;</td>
<td style="display:none;" class="Item_Price10">418,414,989&nbsp;</td>
<td style="display:none;" class="Item_Price10">22,950,175&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl12_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">09/12/2020</td>
<td class="Item_Price10">1,039.13&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>9.87 (0.96 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">526,519,110&nbsp;</td>
<td class="Item_Price10">10,735,157,950,000&nbsp;</td>
<td class="Item_Price10">26,185,960&nbsp;</td>
<td class="LastItem_Price">704,345,590,000&nbsp;</td>
<td class="Item_Price10">1,031.19&nbsp;</td>
<td class="Item_Price10">1,039.55&nbsp;</td>
<td class="Item_Price10">1,030.24&nbsp;</td>
<td style="display:none;" class="Item_Price10">18,906&nbsp;</td>
<td style="display:none;" class="Item_Price10">403,521,708&nbsp;</td>
<td style="display:none;" class="Item_Price10">37,035,165&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl13_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">08/12/2020</td>
<td class="Item_Price10">1,029.26&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Down>-0.72 (-0.07 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">470,435,190&nbsp;</td>
<td class="Item_Price10">9,692,485,000,000&nbsp;</td>
<td class="Item_Price10">19,960,501&nbsp;</td>
<td class="LastItem_Price">560,963,458,800&nbsp;</td>
<td class="Item_Price10">1,029.98&nbsp;</td>
<td class="Item_Price10">1,032.58&nbsp;</td>
<td class="Item_Price10">1,025.63&nbsp;</td>
<td style="display:none;" class="Item_Price10">8,701&nbsp;</td>
<td style="display:none;" class="Item_Price10">385,171,774&nbsp;</td>
<td style="display:none;" class="Item_Price10">39,220,543&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl14_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">07/12/2020</td>
<td class="Item_Price10">1,029.98&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>8.49 (0.83 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">441,497,880&nbsp;</td>
<td class="Item_Price10">8,824,339,910,000&nbsp;</td>
<td class="Item_Price10">42,578,219&nbsp;</td>
<td class="LastItem_Price">943,735,002,350&nbsp;</td>
<td class="Item_Price10">1,024.34&nbsp;</td>
<td class="Item_Price10">1,030.41&nbsp;</td>
<td class="Item_Price10">1,022.14&nbsp;</td>
<td style="display:none;" class="Item_Price10">9,502,062&nbsp;</td>
<td style="display:none;" class="Item_Price10">344,938,569&nbsp;</td>
<td style="display:none;" class="Item_Price10">22,713,990&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl15_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">04/12/2020</td>
<td class="Item_Price10">1,021.49&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>1.69 (0.17 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">496,645,360&nbsp;</td>
<td class="Item_Price10">9,922,601,000,000&nbsp;</td>
<td class="Item_Price10">25,260,522&nbsp;</td>
<td class="LastItem_Price">547,496,442,280&nbsp;</td>
<td class="Item_Price10">1,019.80&nbsp;</td>
<td class="Item_Price10">1,025.17&nbsp;</td>
<td class="Item_Price10">1,018.67&nbsp;</td>
<td style="display:none;" class="Item_Price10">687,877&nbsp;</td>
<td style="display:none;" class="Item_Price10">389,972,225&nbsp;</td>
<td style="display:none;" class="Item_Price10">37,111,773&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl16_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">03/12/2020</td>
<td class="Item_Price10">1,019.80&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>5.48 (0.54 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">468,398,510&nbsp;</td>
<td class="Item_Price10">9,116,518,000,000&nbsp;</td>
<td class="Item_Price10">18,539,415&nbsp;</td>
<td class="LastItem_Price">579,305,383,050&nbsp;</td>
<td class="Item_Price10">1,016.73&nbsp;</td>
<td class="Item_Price10">1,020.35&nbsp;</td>
<td class="Item_Price10">1,014.06&nbsp;</td>
<td style="display:none;" class="Item_Price10">10,594,049&nbsp;</td>
<td style="display:none;" class="Item_Price10">366,928,843&nbsp;</td>
<td style="display:none;" class="Item_Price10">52,026,489&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl17_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">02/12/2020</td>
<td class="Item_Price10">1,014.32&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>5.45 (0.54 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">450,953,340&nbsp;</td>
<td class="Item_Price10">9,570,261,000,000&nbsp;</td>
<td class="Item_Price10">197,338,039&nbsp;</td>
<td class="LastItem_Price">4,513,129,664,850&nbsp;</td>
<td class="Item_Price10">1,008.77&nbsp;</td>
<td class="Item_Price10">1,015.86&nbsp;</td>
<td class="Item_Price10">1,007.91&nbsp;</td>
<td style="display:none;" class="Item_Price10">0&nbsp;</td>
<td style="display:none;" class="Item_Price10">0&nbsp;</td>
<td style="display:none;" class="Item_Price10">0&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl18_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">01/12/2020</td>
<td class="Item_Price10">1,008.87&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>20.16 (2.04 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">505,120,880&nbsp;</td>
<td class="Item_Price10">10,367,017,000,000&nbsp;</td>
<td class="Item_Price10">31,128,008&nbsp;</td>
<td class="LastItem_Price">944,414,725,100&nbsp;</td>
<td class="Item_Price10">988.71&nbsp;</td>
<td class="Item_Price10">1,008.87&nbsp;</td>
<td class="Item_Price10">988.71&nbsp;</td>
<td style="display:none;" class="Item_Price10">25,781,462&nbsp;</td>
<td style="display:none;" class="Item_Price10">390,300,888&nbsp;</td>
<td style="display:none;" class="Item_Price10">26,943,405&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl19_itemTR" style="font-family: Arial; font-size: 10px; font-weight: normal; background-color: #FFF;height:30px;padding-right:5px">
<td class="Item_DateItem">30/11/2020</td>
<td class="Item_Price10">1,003.08&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Down>-7.14 (-0.71 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/down_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">417,689,660&nbsp;</td>
<td class="Item_Price10">9,172,841,000,000&nbsp;</td>
<td class="Item_Price10">61,729,494&nbsp;</td>
<td class="LastItem_Price">1,635,852,492,420&nbsp;</td>
<td class="Item_Price10">1,011.82&nbsp;</td>
<td class="Item_Price10">1,012.50&nbsp;</td>
<td class="Item_Price10">1,002.61&nbsp;</td>
<td style="display:none;" class="Item_Price10">14,546,569&nbsp;</td>
<td style="display:none;" class="Item_Price10">338,104,890&nbsp;</td>
<td style="display:none;" class="Item_Price10">37,460,311&nbsp;</td>
</tr>


<tr id="ctl00_ContentPlaceHolder1_ctl03_rptData2_ctl20_altitemTR" style="font-family: Arial; font-weight: normal; background-color: #f2f2f2;height:30px;padding-right:5px">
<td class="Item_DateItem">27/11/2020</td>
<td class="Item_Price10">1,010.22&nbsp;</td>
<td class="Item_ChangePrice"><span class=Index_Up>4.25 (0.42 %)</span></td>
<td class="Item_Image"> <img src='http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/up_.gif' align='absmiddle' /> &nbsp;&nbsp;</td>
<td class="Item_Price10">356,355,590&nbsp;</td>
<td class="Item_Price10">7,877,425,300,000&nbsp;</td>
<td class="Item_Price10">48,708,029&nbsp;</td>
<td class="LastItem_Price">1,606,045,888,800&nbsp;</td>
<td class="Item_Price10">1,006.68&nbsp;</td>
<td class="Item_Price10">1,010.22&nbsp;</td>
<td class="Item_Price10">1,004.00&nbsp;</td>
<td style="display:none;" class="Item_Price10">3,300,497&nbsp;</td>
<td style="display:none;" class="Item_Price10">291,234,999&nbsp;</td>
<td style="display:none;" class="Item_Price10">24,350,435&nbsp;</td>
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

|0|hiddenField|__EVENTTARGET||0|hiddenField|__EVENTARGUMENT||156|hiddenField|__VIEWSTATE|/wEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ==|8|hiddenField|__VIEWSTATEGENERATOR|2E2252AF|79|asyncPostBackControlIDs||ctl00$ContentPlaceHolder1$ctl03$pager2,ctl00$ContentPlaceHolder1$ctl03$btSearch|0|postBackControlIDs|||129|updatePanelIDs||fctl00$ContentPlaceHolder1$LabelUpdatePanel,fctl00$ContentPlaceHolder1$LinkUpdatePanel,tctl00$ContentPlaceHolder1$ctl03$panelAjax|0|childUpdatePanelIDs|||126|panelsToRefreshIDs||ctl00$ContentPlaceHolder1$LabelUpdatePanel,ctl00$ContentPlaceHolder1$LinkUpdatePanel,ctl00$ContentPlaceHolder1$ctl03$panelAjax|2|asyncPostBackTimeout||90|32|formAction||/Lich-su-giao-dich-VNINDEX-1.chn|
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
                # if i % 14 == 0:
                #     txt = td.text.replace(u'\xa0', u'')
                #     data['Ngày'] =  txt.replace(u'\xa0', u'')
                # elif i % 14 == 1:
                #     data['Giá Đóng Cửa'] =   float(td.text.replace(u'\xa0', u'').replace(',', ''))
                # elif i % 14 == 2:
                #     txt = td.text.replace(u'\xa0', u'').replace(',', '')
                #     print(txt)
                #     data['Thay Đổi'] = float(txt.split('(')[0])
                #     data["Thay Đổi Theo %"] = float(txt.split('(')[1].strip()[:-2])
                # elif i % 14 == 4:
                #     data['KL Giao Dịch Khớp Lệnh'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                # elif i % 14 == 5:
                #     data['GT Giao Dịch Khớp Lệnh'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                # elif i % 14 == 6:
                #     data['KL Giao Dịch Thỏa Thuận'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                # elif i % 14 == 7:
                #     data['GT Giao Dịch Thỏa Thuận'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                # elif i % 14 == 8:
                #     data['Giá Mở Cửa'] =  float(td.text.replace(u'\xa0', u'').replace(',', ''))
                # elif i % 14 == 9:
                #     data['Giá Đóng Cửa'] =  float(td.text.replace(u'\xa0', u'').replace(',', ''))
                # elif i % 14 == 10:
                #     data['Giá Thấp Nhất'] =  float(td.text.replace(u'\xa0', u'').replace(',', ''))
            # print(data)
            # lst_data.append(data)
            break
        start += 1
