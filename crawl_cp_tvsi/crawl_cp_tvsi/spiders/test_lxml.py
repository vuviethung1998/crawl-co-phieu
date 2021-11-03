from bs4 import BeautifulSoup as soup
html = '''    <div class="nav third table-bigger" style="border-bottom: none; margin-bottom: 7px;">
                <ul>
                    <li class="item active" id="duration_quater" ><a onclick="changePage(1,0)" style="font-size:14px;">Qu&#253;</a></li>
                    <li class="item" id="duration_year" ><a onclick="changePage(1,1)" style="font-size:14px;">Năm</a></li>
                        <li class="item">
                            <a style="display: inline-block; padding-right: 0;" onclick="changePage(2,1)">
                                <i class="fa fa-caret-left" aria-hidden="true"></i>
                            </a>
                            &nbsp;
                                <a style="display: inline-block; padding-left: 0;opacity:.3">
                                    <i class="fa fa-caret-right" aria-hidden="true"></i>
                                </a>
                        </li>
                </ul>
            </div>
            <div class="table-data" style="margin-top: 0px; margin-bottom: 24px;">
                    <table>
                        <tbody>
                            <tr style="border-bottom: 1px solid #A2A2A2;">
                                <td style="padding-bottom: 15px;">&nbsp;</td>
                                <td>Biểu đồ:</td>
                                            <td style="text-align: right">2015<br>(Đ&#227; kiểm to&#225;n)</td>    
                                            <td style="text-align: right">2016<br>(Đ&#227; kiểm to&#225;n)</td>    
                                            <td style="text-align: right">2017<br>(Đ&#227; kiểm to&#225;n)</td>    
                                            <td style="text-align: right">2018<br>(Đ&#227; kiểm to&#225;n)</td>    
                                            <td style="text-align: right">2019<br>(Đ&#227; kiểm to&#225;n)</td>    
                            </tr>
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">Tổng t&#224;i sản</td>
                                <td ><div id="tongtaisan" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                         <td style="text-align: right">534,729.67</td>
                                         <td style="text-align: right">599,823.06</td>
                                         <td style="text-align: right">643,817.64</td>
                                         <td style="text-align: right">662,377.48</td>
                                         <td style="text-align: right">666,365.50</td>
                            </tr>
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">Vốn chủ sở hữu</td>
                                <td ><div id="vonchusohuu" style="height:30px;max-width:35px; margin: 0 auto"></div></td>
                                        <td style="text-align: right">306,549.64</td>
                                        <td style="text-align: right">315,049.77</td>
                                        <td style="text-align: right">329,495.84</td>
                                        <td style="text-align: right">327,735.63</td>
                                        <td style="text-align: right">335,773.76</td>
                            </tr>
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">Doanh thu thuần</td>
                                <td ><div id="doanhthuthuan" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                            
                                        <td style="text-align: right">707,016.26</td>
                                        <td style="text-align: right">702,107.38</td>
                                        <td style="text-align: right">735,337.16</td>
                                        <td style="text-align: right">713,685.05</td>
                                        <td style="text-align: right">781,060.89</td>
                            </tr>
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">Lợi nhuận gộp</td>
                                <td ><div id="loinhuangop" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                        <td style="text-align: right">48,906.82</td>
                                        <td style="text-align: right">52,109.40</td>
                                        <td style="text-align: right">61,272.76</td>
                                        <td style="text-align: right">67,922.42</td>
                                        <td style="text-align: right">70,743.89</td>
                            </tr>
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">LN từ hoạt động SXKD</td>
                                <td ><div id="loinhuanthdsxkd" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                        <td style="text-align: right">9,319.06</td>
                                        <td style="text-align: right">21,505.36</td>
                                        <td style="text-align: right">31,702.05</td>
                                        <td style="text-align: right">28,145.25</td>
                                        <td style="text-align: right">21,384.58</td>
                            </tr>
                        
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">Lợi nhuận sau thuế</td>
                                <td ><div id="loinhuanst" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                        <td style="text-align: right">10,579.68</td>
                                        <td style="text-align: right">21,261.50</td>
                                        <td style="text-align: right">29,362.72</td>
                                        <td style="text-align: right">30,143.23</td>
                                        <td style="text-align: right">21,080.87</td>
                            </tr>
                        
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">Lợi &#237;ch cổ đ&#244;ng c&#244;ng ty mẹ</td>
                                <td ><div id="loiichctyme" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                        <td style="text-align: right">10,579.68</td>
                                        <td style="text-align: right">21,261.50</td>
                                        <td style="text-align: right">29,362.72</td>
                                        <td style="text-align: right">30,143.23</td>
                                        <td style="text-align: right">21,080.87</td>
                            </tr>
                        
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">Bi&#234;n l&#227;i gộp (trailing 4 qu&#253;) %</td>
                                <td ><div id="bienlaigop" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                            <td style="text-align: right">6.92</td>
                                            <td style="text-align: right">7.42</td>
                                            <td style="text-align: right">8.33</td>
                                            <td style="text-align: right">9.52</td>
                                            <td style="text-align: right">9.06</td>
                            
                            </tr>
                        
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">EPS (trailing 4 qu&#253;) VNĐ</td>
                                <td ><div id="eps" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                        <td style="text-align: right">0.43</td>
                                        <td style="text-align: right">0.87</td>
                                        <td style="text-align: right">1.20</td>
                                        <td style="text-align: right">1.23</td>
                                        <td style="text-align: right">0.86</td>
                            </tr>
                        
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">ROA (trailing 4 qu&#253;) %</td>
                                <td ><div id="ROA" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                        <td style="text-align: right">1.79</td>
                                        <td style="text-align: right">3.75</td>
                                        <td style="text-align: right">4.72</td>
                                        <td style="text-align: right">4.62</td>
                                        <td style="text-align: right">3.17</td>
                            </tr>
                            <tr>
                                <td style="text-align: left; padding-left: 0; padding-top: 17px;">ROE (trailing 4 qu&#253;) %</td>
                                <td ><div id="ROE" style="height:30px;max-width:35px;margin: 0 auto"></div></td>
                                        <td style="text-align: right">3.45</td>
                                        <td style="text-align: right">6.84</td>
                                        <td style="text-align: right">9.11</td>
                                        <td style="text-align: right">9.17</td>
                                        <td style="text-align: right">6.35</td>
                            </tr>                               
                        </tbody>
                    </table>
            </div>
<script>
    function changePage(curPage,_period) {
        loadPopupShow();
        $.ajax({
            url: "/Enterprises/ChiTieuQuanTrong",
            data: { symbol: "TPC", period: _period, currentPage: curPage},
            cache: false,
            type: "GET",
            dataType: "html",
            success: function (data, textStatus, XMLHttpRequest) {
                $("#chitieuquantrong").html(data); // HTML DOM replace
                if (_period == 0) {
                    document.getElementById("duration_quater").className = "item active";
                    document.getElementById("duration_year").className = "item";
                } else {
                    document.getElementById("duration_quater").className = "item";
                    document.getElementById("duration_year").className = "item active";

                }
                loadPopupHide();
            }
        });
    }
    chartChitieutaichinh();
    function chartChitieutaichinh(){
        var dps_tongtaisan=[],dps_vonchusohuu=[],dps_doanhthuthuan=[],
            dps_loinhuangop=[],dps_loinhuanthdsxkd=[],dps_loinhuanst=[],
            dps_loiichctyme=[],dps_bienlaigop=[],dps_eps=[],dps_ROA=[],dps_ROE=[];
        var balance_arr = [{"quater":0,"year":2015,"symbol":"TPC","tongtaisan":534729673815,"vonchusohuu":306549638068,"Audited":true},{"quater":0,"year":2016,"symbol":"TPC","tongtaisan":599823061921,"vonchusohuu":315049765940,"Audited":true},{"quater":0,"year":2017,"symbol":"TPC","tongtaisan":643817636139,"vonchusohuu":329495837123,"Audited":true},{"quater":0,"year":2018,"symbol":"TPC","tongtaisan":662377479493,"vonchusohuu":327735634421,"Audited":true},{"quater":0,"year":2019,"symbol":"TPC","tongtaisan":666365498081,"vonchusohuu":335773762203,"Audited":true}];
        var income_arr = [{"quater":0,"year":2015,"symbol":"TPC","doanhthuthuan":707016258476,"loinhuangop":48906818301,"loinhuanthdsxkd":9319061117,"loinhuanst":10579683995,"loiichctyme":10579683995,"loinhuantruocthue":13420547120},{"quater":0,"year":2016,"symbol":"TPC","doanhthuthuan":702107381535,"loinhuangop":52109401941,"loinhuanthdsxkd":21505362276,"loinhuanst":21261501471,"loiichctyme":21261501471,"loinhuantruocthue":26445339374},{"quater":0,"year":2017,"symbol":"TPC","doanhthuthuan":735337164685,"loinhuangop":61272761505,"loinhuanthdsxkd":31702047493,"loinhuanst":29362715659,"loiichctyme":29362715659,"loinhuantruocthue":36905599440},{"quater":0,"year":2018,"symbol":"TPC","doanhthuthuan":713685054261,"loinhuangop":67922415580,"loinhuanthdsxkd":28145245977,"loinhuanst":30143231298,"loiichctyme":30143231298,"loinhuantruocthue":37922673701},{"quater":0,"year":2019,"symbol":"TPC","doanhthuthuan":781060893734,"loinhuangop":70743887084,"loinhuanthdsxkd":21384578988,"loinhuanst":21080874983,"loiichctyme":21080874983,"loinhuantruocthue":25975374343}];
        var ratio_arr=[{"quater":0,"year":2015,"symbol":"TPC","eps":433.050589310224,"bienlaigop":0.0691735412229706,"ROA":0.017858622381374,"ROE":0.0345090557502125},{"quater":0,"year":2016,"symbol":"TPC","eps":870.281734878674,"bienlaigop":0.074218564441061,"ROA":0.0374799703906357,"ROE":0.0684090149826668},{"quater":0,"year":2017,"symbol":"TPC","eps":1201.88290367538,"bienlaigop":0.0833260774072907,"ROA":0.0472205769798366,"ROE":0.0911113675105778},{"quater":0,"year":2018,"symbol":"TPC","eps":1233.83118848185,"bienlaigop":0.0951714137412219,"ROA":0.0461542551143521,"ROE":0.0917278998438284},{"quater":0,"year":2019,"symbol":"TPC","eps":862.888280867155,"bienlaigop":0.0905740994735971,"ROA":0.0317305533708094,"ROE":0.0635435612223777}];
        // balance sheet
        for(var i = 0; i < balance_arr.length; i++) {
            if(balance_arr[i].tongtaisan < 0){
                dps_tongtaisan.push({ y: balance_arr[i].tongtaisan / 1000000000, color: "red" });
            }else{
                dps_tongtaisan.push({ y: balance_arr[i].tongtaisan / 1000000000});
            }
            if(balance_arr[i].vonchusohuu < 0){
                dps_vonchusohuu.push({ y: balance_arr[i].vonchusohuu / 1000000000, color: "red" });
            }else{
                dps_vonchusohuu.push({ y: balance_arr[i].vonchusohuu / 1000000000});
            }
        }
        // income sheet
        for(var i = 0; i < income_arr.length; i++) {
            if(income_arr[i].doanhthuthuan < 0){
                dps_doanhthuthuan.push({ y: income_arr[i].doanhthuthuan / 1000000000, color: "red" });
            }else{
                dps_doanhthuthuan.push({ y: income_arr[i].doanhthuthuan / 1000000000});
            }

            if(income_arr[i].loinhuangop < 0){
                dps_loinhuangop.push({ y: income_arr[i].loinhuangop / 1000000000, color: "red" });
            }else{
                dps_loinhuangop.push({ y: income_arr[i].loinhuangop / 1000000000});
            }

            if(income_arr[i].loinhuanthdsxkd < 0){
                dps_loinhuanthdsxkd.push({ y: income_arr[i].loinhuanthdsxkd / 1000000000, color: "red" });
            }else{
                dps_loinhuanthdsxkd.push({ y: income_arr[i].loinhuanthdsxkd / 1000000000});
            }

            if(income_arr[i].loinhuanst < 0){
                dps_loinhuanst.push({ y: income_arr[i].loinhuanst / 1000000000, color: "red" });
            }else{
                dps_loinhuanst.push({ y: income_arr[i].loinhuanst / 1000000000});
            }

            if(income_arr[i].loiichctyme < 0){
                dps_loiichctyme.push({ y: income_arr[i].loiichctyme / 1000000000, color: "red" });
            }else{
                dps_loiichctyme.push({ y: income_arr[i].loiichctyme / 1000000000});
            }
        }
        // ratios sheet
        for(var i = 0; i < ratio_arr.length; i++) {
            if(ratio_arr[i].eps < 0){
                dps_eps.push({ y: ratio_arr[i].eps, color: "red" });
            }else{
                dps_eps.push({ y: ratio_arr[i].eps});
            }

            if(ratio_arr[i].bienlaigop < 0){
                dps_bienlaigop.push({ y: ratio_arr[i].bienlaigop, color: "red" });
            }else{
                dps_bienlaigop.push({ y: ratio_arr[i].bienlaigop});
            }

            if(ratio_arr[i].ROA < 0){
                dps_ROA.push({ y: ratio_arr[i].ROA, color: "red" });
            }else{
                dps_ROA.push({ y: ratio_arr[i].ROA});
            }

            if(ratio_arr[i].ROE < 0){
                dps_ROE.push({ y: ratio_arr[i].ROE, color: "red" });
            }else{
                dps_ROE.push({ y: ratio_arr[i].ROE});
            }
        }
        chartChiTieu("tongtaisan",dps_tongtaisan);
        chartChiTieu("vonchusohuu",dps_vonchusohuu);
        chartChiTieu("doanhthuthuan",dps_doanhthuthuan);
        chartChiTieu("loinhuangop",dps_loinhuangop);
        chartChiTieu("loinhuanthdsxkd",dps_loinhuanthdsxkd);
        chartChiTieu("loinhuanst",dps_loinhuanst);
        chartChiTieu("loiichctyme",dps_loiichctyme);
        chartChiTieu("bienlaigop",dps_bienlaigop);
        chartChiTieu("eps",dps_eps);
        chartChiTieu("ROA",dps_ROA);
        chartChiTieu("ROE",dps_ROE);
    }
    function chartChiTieu(id, dps){
        $('#'+id).highcharts({
            chart: {
                type: 'column',
                backgroundColor: "transparent",
                margin: [0, 0, 0, 0],
                spacingTop: 0,
                spacingBottom: 0,
                spacingLeft: 0,
                spacingRight: 0
            },
            title: {
                text: null
            },
            xAxis: {
                tickLength: 0,
                visible: false,
                tickPixelInterval: 1,
                title: {
                    text: null
                }
            },
            yAxis: {
                visible: false,
                title: {
                    text: null
                }
            },
            tooltip: {
                enabled: false
            },
            plotOptions: {
                column: {
                    allowPointSelect: true,
                    pointPadding: 0,
                    borderWidth: 0,
                    size: '100%',
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                }
            },

            //credits: {
            //    enabled: false
            //},
            series: [{
                showInLegend: false,
                data: dps
            }]
        });
    }
</script>'''

if __name__=="__main__":
    s = soup(html, features='lxml').table

    rows = s.find_all('tr')
    lst_data = []

    for i in range(5):
        data = {'Năm': 0, 'Tổng tài sản': 0, "Vốn chủ sở hữu": 0,
                "Doanh thu thuần": 0, "Lợi nhuận gộp": 0, "LN từ hoạt động SXKD": 0,
                "Lợi nhuận sau thuế": 0, "Lợi ích cổ đông công ty mẹ": 0,
                "Biên lãi gộp (trailing 4 quý) %": 0, "EPS (trailing 4 quý)": 0,
                "ROA (trailing 4 quý) %": 0, "ROE (trailing 4 quý) %": 0}
        lst_data.append(data)

    for irow in range(len(rows)):
        cols = rows[irow].find_all("td")

        if irow == 0:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Năm'] = int(cols[icol].text.split('(')[0].replace(',', ''))
        elif irow == 1:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Tổng tài sản'] = float(cols[icol].string.replace(',', ''))
        elif irow == 2:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Vốn chủ sở hữu'] = float(cols[icol].string.replace(',', ''))
        elif irow == 3:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Doanh thu thuần'] = float(cols[icol].string.replace(',', ''))
        elif irow == 4:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Lợi nhuận gộp'] = float(cols[icol].string.replace(',', ''))
        elif irow == 5:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['LN từ hoạt động SXKD'] = float(cols[icol].string.replace(',', ''))
        elif irow == 6:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Lợi nhuận sau thuế'] = float(cols[icol].string.replace(',', ''))
        elif irow == 7:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Lợi ích cổ đông công ty mẹ'] = float(cols[icol].string.replace(',', ''))
        elif irow == 8:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['Biên lãi gộp (trailing 4 quý) %'] = float(cols[icol].string.replace(',', ''))
        elif irow == 9:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['EPS (trailing 4 quý)'] = float(cols[icol].string.replace(',', ''))
        elif irow == 10:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['ROA (trailing 4 quý) %'] = float(cols[icol].string.replace(',', ''))
        elif irow == 11:
            for icol in range(len(cols)):
                if icol > 1:
                    lst_data[icol-2]['ROE (trailing 4 quý) %'] = float(cols[icol].string.replace(',', ''))

    print(lst_data)
