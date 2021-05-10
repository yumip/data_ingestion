import os
from read_dat import read_dat_current, read_dat_archived
from insert_property_list import insert_property_list
from copy_property_list import copy_property_list


def loop_directory(directory: str, archived = False):
	value_list=[]
	for filename in os.listdir(directory):
		if filename.endswith(".DAT"):
			file_directory = os.path.join(directory, filename)
            # print(filename)
			# value_list = read_dat_current(file_directory, value_list)
			value_list = read_dat_archived(file_directory, value_list) if archived else read_dat_current(file_directory, value_list)
			#print(len(value_list))
	# print(value_list[:10])
	# copy_from		
	copy_property_list(value_list)
	## executemany
	#insert_property_list(value_list)
	#print(value_list)


def loop_bulks(bulk_list: list, archived=False):
	value_list = []
	for file_name in bulk_list:
        # print(filename)
		# value_list = read_dat_current(file_directory, value_list)
		value_list = read_dat_archived(file_name, value_list) if archived else read_dat_current(file_name, value_list)
			#print(len(value_list))
	# print(value_list[:10])
	# copy_from
	copy_property_list(value_list)

	## executemany
	#insert_property_list(value_list)
	print(bulk_list[0].stem, bulk_list[-1].stem)	
	# print(list(map(lambda path: path.stem, bulk_list)))

if __name__ == '__main__':
	#loop_directory('../20210426/')
	loop_directory('dl/1991/', True)
