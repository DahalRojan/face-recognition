from fastapi import APIRouter, UploadFile, status
from ai.recognition.schemas import (
    FaceRecognitionResponse,
    )
from ai.recognition.core import Recognition
from ai.core.file import File

router = APIRouter(prefix='/face-recognition', tags=['Face Recognition'])

@router.post(
    '/verify/image2image',
    status_code=status.HTTP_200_OK,
    response_model=FaceRecognitionResponse
)
def face_verification_image2image(
    image1: UploadFile ,
    image2: UploadFile ,
):
    first_image_path = File.handle_upload(image1)
    second_image_path = File.handle_upload(image2)
    return Recognition(path=second_image_path).compare_images(first_image_path, second_image_path)


@router.post(
        '/verify/image2url',
        response_model=FaceRecognitionResponse
)
def face_verification_image2url(
        image: UploadFile,
        url: str
):
    image_path = File.handle_upload(image)
    image_url = File.handle_download(url)
    return Recognition.compare_images(image_path, image_url)

@router.post(
    '/verify/url2url',
    response_model=FaceRecognitionResponse
)
def face_verification_url2url(
    url1: str,
    url2: str
):
    url_path1 = File.handle_download(url1)
    url_path2 = File.handle_download(url2)
    return Recognition.compare_images(url_path1, url_path2)






    