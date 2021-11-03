# curl 'https://api.simplize.vn/api/company/analysis-metrics/VMD' \
#   -H 'Connection: keep-alive' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' \
#   -H 'Accept: application/json, text/plain, */*' \
#   -H 'DNT: 1' \
#   -H 'Authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2dXZpZXRodW5nLjk4Lmh1c3RAZ21haWwuY29tIiwiYXV0aCI6IlJPTEVfVVNFUiIsInVpZCI6MjIyLCJleHAiOjE2MzIyNDA0MTN9.RJNIDBJKgLFRxiM1T_Oz4CFhQXE8eQbGUjW45Spr3A_bMuwoTCCCjoewgeK1v3yJDkgd5_nIVx69GmOzsBA1vw#' \
#   -H 'sec-ch-ua-mobile: ?1' \
#   -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36' \
#   -H 'Origin: https://simplize.vn' \
#   -H 'Sec-Fetch-Site: same-site' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Referer: https://simplize.vn/' \
#   -H 'Accept-Language: vi,en-US;q=0.9,en;q=0.8' \
#   --compressed
import unicodedata
import requests
import yaml
import json

def normalize(title):
    norm_title =  unicodedata.normalize('NFKD', title).encode('ascii', 'ignore')
    return norm_title.decode().strip().replace(',', '').replace(' ', '_')

def getAnalysisMetricByTicker(ticker):
    endpoint = "https://api.simplize.vn/api/company/analysis-metrics/{}".format(ticker)
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2dXZpZXRodW5nLjk4Lmh1c3RAZ21haWwuY29tIiwiYXV0aCI6IlJPTEVfVVNFUiIsInVpZCI6MjIyLCJleHAiOjE2MzE4NjU3MTR9.Oyx-ub-h4aDajzhLKxJ-45K_HC9JtEjFSZTojIou79Ey8rUgpjKUXbYZoQq6wSqULd59fg0aXAaLNj3LZuzgww#"}

    res = requests.get(endpoint,headers=headers).json().get('data')

    result = {}
    result['ticker'] = res['ticker']
    result['industry'] = normalize(res['pbRatio']['industryActivity'])
    result['summary'] = {
        'intrinsic_value': res['intrinsicValue']['intrinsicValue']['value'],
        'current_price': res['intrinsicValue']['priceClose']['value'],
        'fair_value_lower': res['intrinsicValue']['fairValueMedian']['x'],
        'fair_value_upper': res['intrinsicValue']['fairValueMedian']['y'],
        'delta': res['intrinsicValue']['fairValueDelta'],
    }
    result['peRatio'] = {
        'ratio_current': res['peRatio']['ratio'],
        'ratio_5y_average': res['peRatio']['ratio5yAverage'],
        'ratio_5y_average_industry': res['peRatio']['ratioMedian5yIndustry'],
        'ratio_5y_average_market': res['peRatio']['ratioMedian5yMarket']
    }   
    result['pbRatio'] = {
        'ratio_current': res['pbRatio']['ratio'],
        'ratio_5y_average': res['pbRatio']['ratio5yAverage'],
        'ratio_5y_average_industry': res['pbRatio']['ratioMedian5yIndustry'],
        'ratio_5y_average_market': res['pbRatio']['ratioMedian5yMarket']
    }
    result['evEbitdaRatio'] = {
        'ratio_current': res['evEbitdaRatio']['ratio'],
        'ratio_5y_average': res['evEbitdaRatio']['ratio5yAverage'],
        'ratio_5y_average_industry': res['evEbitdaRatio']['ratioMedian5yIndustry'],
        'ratio_5y_average_market': res['evEbitdaRatio']['ratioMedian5yMarket']
    }
    result['evSalesRatio'] = {
        'ratio_current': res['evSalesRatio']['ratio'],
        'ratio_5y_average': res['evSalesRatio']['ratio5yAverage'],
        'ratio_5y_average_industry': res['evSalesRatio']['ratioMedian5yIndustry'],
        'ratio_5y_average_market': res['evSalesRatio']['ratioMedian5yMarket']
    }
    result['pegRatio'] = {
        'ratio_current': res['pegRatio']['ratio'],
        'forecasted_growth_rate': res['pegRatio']['forecastedGrowthRate'],
        'year_growth_rate': res['pegRatio']['yearGrowthRate'],
    }

    return result

if __name__ == "__main__":
    print(getAnalysisMetricByTicker('VIC'))