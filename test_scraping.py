from bs4 import BeautifulSoup
import requests
import os
from time import time
from multiprocessing.pool import ThreadPool

def zip_scraping(url, folder='dl'):

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    cwd = os.getcwd()
    path = os.path.join(cwd,folder)
    files = os.listdir(cwd)
    # print(cwd)    
    # print(files)
    if folder not in files:
        os.mkdir(path)
        print(f"{folder} folder was created")
    table = []

    for link in soup.find_all('a'):
        url = link.get('href')
        if url.endswith('.zip'):

            file_name_start_pos = url.rfind("/") + 1
            file_name = url[file_name_start_pos:]

            if file_name not in path:
                file_path = os.path.join(path, file_name)
                table.append((url,file_path))
                #print(file_name)

    #print(table)
    return table


# z = zipfile.ZipFile(io.StringIO(item))# z.extractall("/dl")
def download_zipFile(url_and_path):
    url, path = url_and_path
    # file_name_start_pos = url.rfind("/") + 1
    # file_path = os.path.join(path, url[file_name_start_pos:])
    print(url_and_path)
    try:  
        with open(path, "wb") as zip:
            req = requests.get(url)
            zip.write(req.content)
    except Exception as e:
        print("Could not download file {}".format(url))
        print(e)
    else:
        print(f"{path} was created")




if __name__ == '__main__':
    start = time()
    url = "https://valuation.property.nsw.gov.au/embed/propertySalesInformation"
    url_and_path_list = zip_scraping(url)
    print(len(url_and_path_list))
    results = ThreadPool(len(url_and_path_list)).imap_unordered(download_zipFile, url_and_path_list)
    # download_zipFile(url_and_path_list[0])
    for r in results:
        print(r)
    print(f"Time to download: {time() - start}")
