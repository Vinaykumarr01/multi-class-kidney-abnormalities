from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from users.models import UserRegistrationModel


# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})



def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/viewregisterusers.html', context={'data': data})




def ActivaUsers(request):
    if request.method == 'GET':
        user_id = request.GET.get('uid')
        
        if user_id:  # Ensure user_id is not None
            status = 'activated'
            print("Activating user with ID =", user_id)
            UserRegistrationModel.objects.filter(id=user_id).update(status=status)

        # Redirect to the view where users are listed after activation
        return redirect('RegisterUsersView')  # Replace with your actual URL name

def DeleteUsers(request):
    if request.method == 'GET':
        user_id = request.GET.get('uid')
        
        if user_id:  # Ensure user_id is not None
            print("Deleting user with ID =", user_id)
            UserRegistrationModel.objects.filter(id=user_id).delete()

        # Redirect to the view where users are listed after deletion
        return redirect('RegisterUsersView')  # Replace with your actual URL name
def adminhome(request):
    return render(request,'admins/AdminHome.html')


from django.shortcuts import render
import os

# ---------------- DATASET VIEW ----------------
from django.shortcuts import render
import os

def dataset_view(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # ✅ CORRECT DATASET PATH
    dataset_base = os.path.join(
        BASE_DIR,
        "dataset",
        "content",
        "dataset"
    )

    splits = ["train", "val"]
    classes = ["Normal", "Cyst", "Tumor", "Stone"]

    dataset_stats = {}
    grand_total = 0

    for cls in classes:
        dataset_stats[cls] = {"train": 0, "val": 0, "total": 0}

        for split in splits:
            path = os.path.join(dataset_base, split, cls)
            if os.path.exists(path):
                count = len(os.listdir(path))
                dataset_stats[cls][split] = count
                dataset_stats[cls]["total"] += count
                grand_total += count

    context = {
        "dataset_stats": dataset_stats,
        "grand_total": grand_total
    }

    return render(request, "admins/dataset_view.html", context)




# ---------------- MODEL STATUS ----------------
def model_status(request):
    context = {
        "model_name": "YOLOv8 Classification Model",
        "architecture": "YOLOv8n-cls",
        "input_size": "224 x 224",
        "classes": ["Normal", "Cyst", "Tumor", "Stone"],
        "accuracy": "99.8%",
        "last_trained": "Recently",
        "framework": "PyTorch + Ultralytics",
        "deployment": "Django Web Application"
    }
    return render(request, "admins/model_status.html", context)


