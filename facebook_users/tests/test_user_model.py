from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class AssociateFriends(TestCase):
  def setUp(self):
    self.test_users = [
            {"name": "Alondra Krause", "id": 6316816636194673}, {"name": "Eliana Cordova", "id": 2467825702628370}, {"name": "Tori Howell", "id": 1117789108273389}, 
            {"name": "Rey Dickson", "id": 2418890580099085}, {"name": "Phoenix Andrews", "id": 9163667750244648}, {"name": "Talon Farmer", "id": 2999009655073479}, 
            {"name": "Carolina Cortez", "id": 9038707755843264}, {"name": "Penelope Velazquez", "id": 6991266520965726}, {"name": "Giancarlo Manning", "id": 2749147975847501}, 
            {"name": "Camron Oliver", "id": 3707558171063215}, {"name": "Moriah Cross", "id": 4588976795742594}
            ]
    self.user_set = set()

    for user in self.test_users:
      new_user = User.objects.create(facebook_user_id= user["id"], name = user["name"])
      self.user_set.add(new_user)


    self.test_user = User.objects.create(facebook_user_id = 8416816632134673)
    #Again, randomly generated
    self.test_user.name = "Zelde Erskine"

  def test_friends(self):
    self.test_user.set_friends(self.user_set)
    # todo: assertion
