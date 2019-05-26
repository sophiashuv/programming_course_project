# -*- coding: utf-8 -*-
import requests
import lxml.html as lh
import pandas as pd
from scripts.json_reading_writing import*


def scrap_site(url, raws_amount):
    """
    Takes url and number of raws erom table, makes request with url and returns parsed data
    which is ready fir writing to json.
    (str,int)->str
    """
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    columns = []
    i = 0
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        columns.append((name, []))
    for j in range(1, len(tr_elements)):
        jth_row = tr_elements[j]
        # If row is not of size, the //tr data is not from our table
        if len(jth_row) != raws_amount:
            break
        i = 0
        for t in jth_row.iterchildren():
            data = t.text_content()
            if i > 0:
                # Convert any numerical value to integers
                try:
                    data = int(data)
                except:
                    pass
            columns[i][1].append(data)
            i += 1
    table_data_dict = {title: column for (title, column) in columns}
    df = pd.DataFrame(table_data_dict)
    df.head()
    df.items()
    output_data = df.to_json(orient='records', force_ascii=False)
    return output_data


if __name__ == '__main__':
    url1 = 'https://diagnoz.in.ua/tsukrovyj-diabet/tablytsya-hlibnyh-odynyts-dlya-diabetykiv-1-i-2-typu-kalkulyator-rozrahunok/'
    table_1 = scrap_site(url1, 2)
    rewrite_json(table_1, 'table2.json')
