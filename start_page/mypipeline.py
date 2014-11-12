from django.contrib.auth.models import User

def load_user(uid, *args, **kwargs):
    try:
        user = User.objects.get(email=uid)
        return {'user':user}
    except:
        return None
