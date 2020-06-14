from skimage.io import imread
from skimage.transform import resize
from main import clf;

def predict(filename):
    res = ""
    new_data = []
    new_image = imread("E:\\BTLXLA\\uploads\\"+filename)
    new_img = resize(new_image, (64,64), anti_aliasing=True, mode='reflect')
    new_data.append(new_img.flatten())
    predict = clf.predict(new_data)
    predict = predict.tolist()
    for num in predict:
        if num == 0:
            res = "Dalmatian"
        if num == 1:
            res = "Dollar Bill"
        if num == 2:
            res = "Pizza"
        if num == 3:
            res = "Soccer Ball"
        if num == 4:
            res = "Sunflower"
    print(res)
    return res