from opencv.fr.liveness.schemas import LivenessRequest, DeviceType
from pathlib import Path

from opencv.fr.persons.schemas import PersonBase
from pathlib import Path
import cv2,os
from opencv.fr import FR
from opencv.fr.search.schemas import SearchRequest, SearchMode, SearchOptions,DetectionRequest
from PIL import Image


BACKEND_URL = "https://us.opencv.fr"
DEVELOPER_KEY = "el7nS5lMmVhYzk4MDAtZWM3OC00ZDIxLTk5ZTktODk0ZDc0YTY1N2Iz"
SDK = FR(BACKEND_URL, DEVELOPER_KEY)

image_path = os.path.abspath("check/datafile.jpg")

liveness_request = LivenessRequest(image_path, DeviceType.IOS)

response = SDK.liveness.check_liveness(liveness_request)
print(response.score)
