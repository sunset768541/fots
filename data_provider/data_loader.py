import numpy as np
import os
import glob
from abc import abstractmethod

class DataLoader(object):
	def get_images(self, data_dir):
		files = []
		for ext in ['jpg', 'png', 'jpeg', 'JPG']:
			files.extend(glob.glob('/home/sunset/learn/AI/fots/AI/ch4_training_images/*.jpg'))
		return files

	@abstractmethod
	def load_annotation(self, gt_file):
		print("reimplement by particular data loader")
		pass
