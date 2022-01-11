"""
Phát hiện biển số xe từ một ảnh đầu vào
"""
from lp_detection import lp_detect_using_contour
from character_segmentation import segment_characters
from lp_recognition import lp_recognize

import cv2
import numpy as np
from keras.models import load_model

"""
Hàm nhận đầu vào là ảnh upload từ server

cần convert sang cv2
"""
def lp_recognition_image(image):
    # đọc từ request sẽ như thế này
    # img = cv2.imdecode(np.fromstring(request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
    # truyền vào thì sẽ thế này
    img = cv2.imdecode(np.fromstring(image, np.uint8), cv2.IMREAD_UNCHANGED)

    # đọc model CNN
    loaded_model = load_model('weights/dkt_model.h5')

    # biến kết quả
    predict_plate = ""

    # phát hiện vùng chứa biển số
    img_plate = lp_detect_using_contour(image=img)

    # nếu tìm được biển
    if img_plate is not None:
        # phân đoạn ký tự
        char_list = segment_characters(image=img_plate)

        # nếu không phân tách được ký tự
        if len(char_list) == 0:
            return predict_plate

        # nhận dạng ký tự
        predict_plate = lp_recognize(model=loaded_model, char_list=char_list)

    return predict_plate