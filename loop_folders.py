from pathlib import Path
import os
from loop_directory import loop_bulks

def loop_folders(chunks: list, Archived=False):
    for chunk in chunks:
        loop_bulks(chunk, Archived)

    

def chunks(paths: list, n):
    return [paths[i*n:(i+1)*n] for i in range((len(paths) + n - 1) // n)]

if __name__ == '__main__':
    path = Path.cwd() / 'dl'
    #print(path)

    path_archive = list(path.glob('**/ARCHIVE_SALES_*.dat'))
    ##archive_stem = list(map(lambda path: path.stem, path_archive))
    archived_chunks = chunks(path_archive,5)

    ## path_current = list(path.glob('**/*_SALES_DATA_NNME_*.dat'))
    ## current_stem = list(map(lambda path: path.stem, path_current))
    ## print(len(list(current_stem)))

    path_current1 = list(path.glob('**/*_SALES_DATA_*.dat'))

    current_chunks = chunks(path_current1, 1000)

    ##print(chunks[0])          
    ##current1_stem = list(map(lambda path: path.stem, path_current1))


    loop_folders(archived_chunks, True)
    loop_folders(current_chunks)
    ##print(len(list(current1_stem)))

    # missing = []
    # for item in current1_stem:
    #     if item not in current_stem:
    #         missing.append(item)
    # print(missing)

    # These three files are named differently from the others ['656_SALES_DATA_08072019', '666_SALES_DATA_08072019', '708_SALES_DATA_08072019']
    # under 2019/2019708    



