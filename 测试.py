
import requests

url = "https://aweme.snssdk.com/aweme/v1/search/item/?keyword=漫画&offset=10&count=10&source=video_search&is_pull_refresh=1&hot_search=0&ts=1546931874&js_sdk_version=&app_type=normal&openudid=8cec4b81deae6417&version_name=4.0.0&device_type=OPPO R11&ssmix=a&iid=57005283726&os_api=19&mcc_mnc=46007&device_id=59343989226&resolution=720*1280&device_brand=OPPO &aid=1128&manifest_version_code=400&app_name=aweme&_rticket=1546931874668&os_version=4.4.2&device_platform=android&version_code=400&update_version_code=4002&ac=wifi&dpi=240&uuid=863064010113316&language=zh&channel=aweGW"
page = requests.get(url)

print(page.text)



