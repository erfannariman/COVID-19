def import_data():
    """
    this scripts import the COVID-19 geographic distribution data from ECDC
    it also catches errors if you try to download data which is not uploaded yet
    in that case it will read the data from the day before
    """
    
    try:
        date = dt.datetime.today().strftime('%Y-%m-%d')
        df = pd.read_excel(f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{date}.xlsx')
    except HTTPError as e:
        print('File on ECDC not found, reading in data from day before')
        date = (dt.datetime.today() - dt.timedelta(days=1)).strftime('%Y-%m-%d')
        df = pd.read_excel(f'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{date}.xlsx')
        
    return df


def 