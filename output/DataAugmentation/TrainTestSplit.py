import shutil
import os
import numpy as np
import argparse
import random

def get_files_from_folder(path):

    files = os.listdir(path)
    return np.asarray(files)

def main(path_to_data, path_to_test_data, train_ratio):
    # get dirs
    print('Enters Main Program')
    dirs = next(os.walk(path_to_data))[2]
    print("---dirs: ",dirs)

    # calculates how many train data per class
    #data_counter_per_class = np.zeros((len(dirs)))
    data_counter = len(dirs)
    test_counter = int(np.round(data_counter*(1-train_ratio)))
    print("---train_ratio: ",train_ratio)
    print("---data_counter: ",data_counter)
    print("---test_counter: ",test_counter)
    print("---path_to_data: ",path_to_data)
    
    for i in range(test_counter):
        filename = random.choice(os.listdir(path_to_data))
        print("---filename",filename)
        filelocation = os.path.join(path_to_data,filename)
        print("---filelocation",filelocation)
        shutil.move(filelocation, path_to_test_data)
        


def parse_args():
  parser = argparse.ArgumentParser(description="Dataset divider")
  parser.add_argument("--data_path", required=True,
    help="Path to data")
  parser.add_argument("--test_data_path_to_save", required=True,
    help="Path to test data where to save")
  parser.add_argument("--train_ratio", required=True,
    help="Train ratio - 0.7 means splitting data in 70 % train and 30 % test")
  return parser.parse_args()

if __name__ == "__main__":
    print("Program Starts")
    args = parse_args()
    print(args)
    main(args.data_path, args.test_data_path_to_save, float(args.train_ratio))