import requests
import base64
import cv2 as cv
from monitor.access import get_access_token

# opencv 图片
def smokmask_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = get_access_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(request_url, data=params, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
        data = response.json()

        # 确保 'person_info' 存在
        if 'person_info' not in data:
            print("Expected 'person_info' key is missing in the response")
            return 0, 0

        people_smoking_count = 0
        people_without_mask_count = 0

        for person in data['person_info']:
            face_mask_info = person['attributes'].get('face_mask', {})
            smoke_info = person['attributes'].get('smoke', {})

            if face_mask_info.get('name', '') == '无口罩':
                people_without_mask_count += 1
            if smoke_info.get('name', '') == '吸烟':
                people_smoking_count += 1
        return  people_without_mask_count,people_smoking_count

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"JSON decoding error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")

    return 0, 0  # 如果有错误发生，返回 0 计数

# 示例使用
# 假设img是您要检测的图像

    # # 等待按键，然后关闭窗口
    # cv.waitKey(0)
    # cv.destroyAllWindows()
