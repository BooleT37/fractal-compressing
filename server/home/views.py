import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from logic.ImageRecoder import recode_image as recode_image_fn

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TARGET_IMAGE_NAME = "target_image.png"
BLANK_IMAGE_NAME = "blank_image.png"
RECODED_IMAGE_NAME = "recoded_image.png"
ENCODE_DATA_PATH = os.path.join(BASE_DIR, f'../static/encoded_data.json')


def index(request):
    target_image_uploaded = has_bool_value(request.GET, 'target_image_uploaded')
    blank_image_uploaded = has_bool_value(request.GET, 'blank_image_uploaded')
    image_recoded = has_bool_value(request.GET, 'image_recoded')
    return render(
        request,
        "index.html",
        {
            'target_image_uploaded': "True" if target_image_uploaded else "",
            'blank_image_uploaded': "True" if blank_image_uploaded else "",
            'image_recoded': "True" if image_recoded else ""
        })


@csrf_exempt
def upload_target_image(request):
    write_image_to_disc(request.FILES['target_image'], TARGET_IMAGE_NAME)
    print(request.POST.items())
    blank_image_uploaded = has_bool_value(request.POST, 'blank_image_uploaded')
    blank_image_uploaded_query = "&blank_image_uploaded=1" if blank_image_uploaded else ""
    return HttpResponseRedirect(f'/home?target_image_uploaded=1{blank_image_uploaded_query}')


@csrf_exempt
def upload_blank_image(request):
    write_image_to_disc(request.FILES['blank_image'], BLANK_IMAGE_NAME)
    print(request.POST.items())
    target_image_uploaded = has_bool_value(request.POST, 'target_image_uploaded')
    target_image_uploaded_query = "target_image_uploaded=1&" if target_image_uploaded else ""
    return HttpResponseRedirect(f'/home?{target_image_uploaded_query}blank_image_uploaded=1')


@csrf_exempt
def recode_image(request):
    recode_image_fn(
        get_image_path(TARGET_IMAGE_NAME),
        get_image_path(BLANK_IMAGE_NAME),
        get_image_path(RECODED_IMAGE_NAME),
        ENCODE_DATA_PATH
    )
    return HttpResponseRedirect('/home?target_image_uploaded=1&blank_image_uploaded=1&image_recoded=1')


@csrf_exempt
def iterate_recode(request):
    recode_image_fn(
        get_image_path(TARGET_IMAGE_NAME),
        get_image_path(RECODED_IMAGE_NAME),
        get_image_path(RECODED_IMAGE_NAME),
        ENCODE_DATA_PATH
    )
    return HttpResponseRedirect('/home?target_image_uploaded=1&blank_image_uploaded=1&image_recoded=1')


def write_image_to_disc(image_file, name):
    with open(get_image_path(name), 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)
        destination.close()


def has_bool_value(query_dict, key):
    return key in query_dict and query_dict.get(key) != ''


def get_image_path(image_name):
    return os.path.abspath(os.path.join(BASE_DIR, f'../static/images/{image_name}'))
