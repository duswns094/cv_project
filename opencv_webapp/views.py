from django.shortcuts import render, redirect
from .forms import SimpleUploadForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})

def simple_upload(request):
    if request.method == 'POST':
    # print(request.POST) : <QueryDict: {'csrfmiddlewaretoken': [‘~~~’], 'title': ['upload_1']}>
    # print(request.FILES) : <MultiValueDict: {'image': [<InMemoryUploadedFile: ses.jpg (image/jpeg)>]}>
    # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            myfile = request.FILES['image'] # 메모리에 한시적으로 저장되어있는 파일 객체
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            # myfile.name : 'ses.jpg' (사용자가 업로드한 파일 원본의 이름)
            # filename : 'ses_UPArih4.jpg' (서버에 업로드가 끝난 파일의 이름, 중복될 시 자동으로 변경됨)
            # 서버에 업로드가 끝난 이미지 파일의 URL을 얻어내 Template에게 전달
            # print('\n\n=============================\n\n')
            # print(myfile.name, type(myfile.name))
            # print(myfile, type(myfile))
            # print(filename, type(filename))
            # print(uploaded_file_url, type(uploaded_file_url))
            # print('\n\n=============================\n\n')
            uploaded_file_url = fs.url(filename) # '/media/ses.jpg'
            # fs.delete(filename)

            context = {'form': form, 'uploaded_file_url': uploaded_file_url} # filled form
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else: # request.method == 'GET' (DjangoBasic 실습과 유사한 방식입니다.) -> 폼을 유저에게 보여주는 부분이기 때문에.
        form = SimpleUploadForm()
        context = {'form': form} # empty form
        return render(request, 'opencv_webapp/simple_upload.html', context)
