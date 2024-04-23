from ..models import User
class UserService:
    
    def create_kid_user(self, username, email, password):
        newuser = User.objects.create(username=username, email=email)
        newuser.is_active = True
        newuser.role = User.ROLES[1]
        newuser.set_password(password)
        newuser.first_name = newuser.last_name = username
        newuser.save()

    def get_user_data(self, user_id):
        user = User.objects.get(pk=user_id)
        return {'username': user.username}
