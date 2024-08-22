from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def users_list(request):
    users = User.objects.all()
    return JsonResponse({'data':list(users.values('username', 'active'))})

@csrf_exempt
def user_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        active = data.get('active', True)
        user = User(username=username, active=active)
        user.set_password(password)
        user.save()
        return JsonResponse({"message":"Success"}, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=data['id'])
        except:
            return JsonResponse({"message":"User not found"}, status=404)
        user.username = data.get('username')
        user.active = data.get('active')
        user.set_password(data.get('password'))
        user.save()
        return JsonResponse({"message":"Success"}, status=200)
    
        
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=data['id'])
        except:
            return JsonResponse({"message":"User not found"}, status=404)
        user.delete()
        return JsonResponse({"message":"Success"}, status=204)
    

@csrf_exempt
def get_details(request):
    if request.method ==  'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=data['id'])
        except:
            return JsonResponse({"message":"User not found"}, status=404)
        return JsonResponse({"data":{'id': user.id, 'username': user.username, 'active': user.active}})

        
