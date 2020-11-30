from demo import single_pic_proc
import os
import time
import shutil
import numpy as np
import json
from glob import glob
from PIL import Image




if __name__ == '__main__':
    image_files = glob('./test_images/*.*')
    result_dir = './test_result'
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)

    for image_file in sorted(image_files):
        t = time.time()
        result, image_framed = single_pic_proc(image_file)
        output_file = os.path.join(result_dir, image_file.split('/')[-1])
        txt_file = os.path.join(result_dir, image_file.split('/')[-1].split('.')[0]+'.txt')
        print(txt_file)
        txt_f = open(txt_file, 'w')
        Image.fromarray(image_framed).save(output_file)
        print("Mission complete, it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")
        for key in result:
            print(result[key][1])
            txt_f.write(result[key][1]+'\n')
        txt_f.close()

        # 
    text_files = glob('./test_result/*.txt')
    for text_file in sorted(text_files):
        res=[]
        for line in text_file:
            res.append(line[:-1]) 
        res[4]=res[4][6:]
        res[5]=res[5][1:]

        final={"Name":res[3],
        "DOB":res[4],
        "Gender":res[5],
        "AADHAR Number":res[6]}

        with open ("result.json","w") as output:
            json.dump(final,output)
