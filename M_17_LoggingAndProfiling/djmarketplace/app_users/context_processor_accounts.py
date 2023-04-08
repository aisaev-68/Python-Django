from app_users.models import Profile


def user_profile(request):
    st = Profile.objects.select_related('user').filter(user_id=request.user.pk).first()
    return {'user_profile': st}