import requests
import base64
import cv2 as cv
from monitor.access import get_access_token

# opencv 图片
def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = get_access_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    if response:
        data = response.json()
        num = data['vehicle_num']['car']
    return num
    # # 等待按键，然后关闭窗口
    cv.waitKey(0)
    cv.destroyAllWindows()
