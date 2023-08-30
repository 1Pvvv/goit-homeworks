import os
import shutil
import logging

from time import time
from threading import Thread, RLock
from concurrent.futures import ThreadPoolExecutor


target_folder = "Хлам"
lock = RLock()

def is_folder_empty(folder_path):
	return len(os.listdir(folder_path)) == 0

def search_target_folder(folder_name):
	path = os.getcwd()
	for root, dirs, files in os.walk(path):
		if root.endswith(folder_name):
			logging.debug('Target folder found')
			return root

def check_for_same_file_name(src, dst):
	count = 0
	dir_name, old_name = os.path.split(dst)
	file_name, extention = os.path.splitext(old_name)
	while os.path.exists(f'{os.path.join(dir_name, file_name)}{extention}'):
		file_name = f'{old_name}_{count}'
		count += 1
	dst = os.path.join(dir_name, f'{file_name}{extention}')
	return src, dst

def move_file_with_lock(src, dst):
	with lock:
		try:
			shutil.move(*check_for_same_file_name(src, dst))
		except FileNotFoundError:
			os.mkdir(os.path.dirname(dst))
			shutil.move(*check_for_same_file_name(src, dst))
		logging.debug('moved file: %s', os.path.basename(dst))

def move_files(from_path):
	threads = []

	for root, dirs, files in os.walk(from_path):
		for file in files:
			_file = file.split('.')

			if len(_file) > 1:
				dst_path = os.path.join(from_path, _file[-1], file)
			else:
				dst_path = os.path.join(from_path, file)

			src = os.path.join(root, file)

			thread = Thread(target=move_file_with_lock, args=(src, dst_path))
			threads.append(thread)
			thread.start()

	for thread in threads:
		thread.join()

	logging.debug('All files moved')

def move_files_in_pool(from_path):
	args = []

	for root, dirs, files in os.walk(from_path):
		for file in files:
			_file = file.split('.')

			if len(_file) > 1:
				dst_path = os.path.join(from_path, _file[-1], file)
			else:
				dst_path = os.path.join(from_path, file)

			src = os.path.join(root, file)

			arg = (src, dst_path)
			args.append(arg)
	
	return args

def clear_empty_folders(target_path):
	for root, dirs, files in os.walk(target_path, topdown=False):
		if is_folder_empty(root):
			os.rmdir(root)
	logging.debug('Empty folders cleared')


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
	timer = time()

	path = search_target_folder(target_folder)

	if path:
		# just Threads
		# move_files(path)

		# ThreadPoolExecutor
		with ThreadPoolExecutor(max_workers=9) as executor:
			results = [executor.submit(move_file_with_lock, *d) for d in move_files_in_pool(path)]

		clear_empty_folders(path)
	else:
		logging.debug(f'There is no "{target_folder}" dir')

	logging.debug(f'Done {time() - timer}')
