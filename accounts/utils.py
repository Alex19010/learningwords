from django.contrib.auth import get_user_model
import random


def is_username_unique(username):
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        return False
    except User.DoesNotExist:
        return True


def set_random_username():
    chaw = '1234567890qwertyuiopasdfghjklzxcvbnm'
    username = ''
    num = 7
    new = False
    while new == False:
        while num >= 0:
            nums = random.randint(0, len(chaw)-1)
            username += chaw[nums]
            num -= 1
        if is_username_unique(username):
            new = True
        else:
            username = ''
    return username