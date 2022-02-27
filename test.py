import os

from tesserocr import PyTessBaseAPI
from jiwer import wer

def read_files(folder):
    files = os.listdir(folder)
    files_with_paths = list()
    for file in files:
        filename = os.path.splitext(os.path.basename(file))[0]
        files_with_paths.append((filename, folder + '/' + file))
    return files_with_paths


def ocr(images, out_folder):
    ocr_results = list()
    with PyTessBaseAPI() as api:
        for img in images:
            api.Init("/home/karen/master-ocr/ocr-test/", lang="hye")
            api.SetImageFile(img[1])
            ocr_text = api.GetUTF8Text()

            file_path = out_folder + '/' + img[0] + '.txt'
            file = open(file_path ,'w+')
            file.write(ocr_text)
            file.close()

            print('filename: ', img[0])
            print('file_path: ', file_path)
            # print('ocr_text: ', ocr_text)

            ocr_results.append((img[0], file_path))

def wer(original_files, ocr_files):

if __name__ == '__main__':
    output_folder = 'ocr_texts'
    if not os.path.exists(output_folder):
        print("Creating output folder: ", output_folder)
        os.mkdir(output_folder)
    images = read_files('data/test_jpgs')
    original_files = read_files('data/original_texts')
    ocr_result = ocr(images, output_folder)

    print(ocr_result)


