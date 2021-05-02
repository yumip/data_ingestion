import os
from read_dat import read_dat
from insert_property_list import insert_property_list

# def loop_directory(directory: str):
#     for filename in os.listdir(directory):
#         if filename.endswith(".DAT"):
#             file_directory = os.path.join(directory, filename)
#             # print(filename)
#             read_dat(file_directory)


def loop_directory(directory: str):
	value_list=[]
	for filename in os.listdir(directory):
		if filename.endswith(".DAT"):
			file_directory = os.path.join(directory, filename)
            # print(filename)
			value_list = read_dat(file_directory, value_list)

	insert_property_list(value_list)
	#print(value_list)

if __name__ == '__main__':
	loop_directory('../20210426/')
