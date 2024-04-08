#!/usr/bin/env python3
import argparse
import shutil
import os
import sys
from datetime import date
from pathlib import Path


"""
Makes a backup in the name schame backup-<date>.zip in the given backup_path.
The folder $HOME/Documents is backed up.
"""
def backup(backup_path):
	print("Start backup")
	# When given a folder, the name schema backup-%s.zip is used.
	if os.path.isdir(backup_path):
		zip_filename_standalone = "backup-%s.zip" % (date.today())
		print("Directory given: Using filename %s" % (zip_filename_standalone))
		zip_filename = os.path.join(backup_path, zip_filename_standalone)
	# At the moment only folders are accepted for backup
	else:
		print("Only folders are accepted for backup --backup-path")
		sys.exit(3)
	print("Create zipfile %s.zip" % zip_filename)
	zip_filename_without_zip = os.path.splitext(zip_filename)[0]
	# Using filename without .zip, because .zip will be attached by the make_archive!
	zip_filename = shutil.make_archive(zip_filename_without_zip, 'zip', str(Path.home()), 'Documents')
	print("Sucessfully zipped files to %s" % zip_filename)
	return


"""
Restore a backup that was created with backup, by unzipping everything to $HOME/Documents,
but $HOME/Documents is moved to $HOME/Documents.1 to not lose it, when something with the
restore went wrong.
"""
def restore(backup_path):
	if not os.path.exists(backup_path):
		print("The path given by --backup-path doesn't exist")
		sys.exit(1)
	if not os.path.isfile(backup_path):
		print("Path given by --backup-path is no file, but this is necessary for restore")
		sys.exit(2)
	print("Start restore")
	print("Saving Documents folder to Documents.1 in case something went wrong...")
	folder_to_backup = "%s/%s" % (Path.home(), "Documents")
	shutil.move(folder_to_backup, folder_to_backup + ".1")
	print("Unpack %s to folder %s " % (backup_path, folder_to_backup))
	shutil.unpack_archive(filename=backup_path, extract_dir=Path.home())


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--mode", help="The mode of the tool: backup or restore, default is backup", default="backup", dest="mode")
	parser.add_argument("--backup-path", help="Path of the backup, include filename if used for restore", dest="backup_path", required=True)
	args = parser.parse_args()
	mode = args.mode
	backup_path = args.backup_path

	if mode == "backup":
		backup(backup_path)

	elif mode == "restore":
		restore(backup_path)


if __name__ == "__main__":
	main()
