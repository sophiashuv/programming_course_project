import requests
import lxml.html as lh
import pandas as pd
from json_working import*


def scrap_site(url):
    """
    The function takesb url and number of raws ferom table, makes request with url and returns parsed data
    which is ready fir writing to json.
    """
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    columns = []
    i = 0
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        columns.append((name[18:-16], []))

    for j in range(2, len(tr_elements)):
        jth_row = tr_elements[j]
        if len(jth_row) < 2:
            continue
        i = 0
        for t in jth_row.iterchildren():
            data = t.text_content()
            if " " * 4 in data:
                data = data[18:]
            if "/" in data:
                data = data[:data.index("/")-2]
            columns[i][1].append(data)
            i += 1

    columns = columns[:-1]
    table_data_dict = {title: column for (title, column) in columns}
    df = pd.DataFrame(table_data_dict)
    df.head()
    df.items()
    output_data = df.to_json(orient='records', force_ascii=False)
    return output_data


if __name__ == '__main__':
    url1 = 'https://www.webmd.com/diabetes/diabetes-types-insulin#1'
    table_1 = scrap_site(url1)
    write_in_json(table_1)
    rewrite_json(table_1, 'table_insulin.json')
