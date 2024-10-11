from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message
class SnsTests(TestCase):

    # def test_check(self):
    #     x = True
    #     self.assertTrue(x)
    #     y = 100
    #     self.assertGreater(y,0)
    #     arr = [10,20,30]
    #     self.assertIn(20,arr)
    #     nn = None
    #     self.assertIsNone(nn)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user = cls.create_user()
        cls.create_message(user)

    @classmethod
    def create_user(cls):
        User(username='test',password='test',is_staff=True,is_active=True).save()
        user = User.objects.filter(username='test').first()
        return (user)
    
    @classmethod
    def create_message(cls,user):
        Message(content='test message',owner_id=user.id).save()
        Message(content='test message2',owner_id=user.id).save()
        Message(content='Ok',owner_id=user.id).save()
        Message(content='Good',owner_id=user.id).save()


    def test_check(self):
        user = User.objects.first()
        msg = Message.objects.filter(content="Ok").first()
        self.assertIs(msg.owner_id,user.id)
        self.assertEqual(msg.owner.username,user.username)

        c = Message.objects.all().count()
        self.assertEqual(c,4)

        msgs = Message.objects.filter(content__contains="test")

        self.assertIs(msgs.count(),2)

        msg1 = Message.objects.all().first()
        msg2 = Message.objects.all().last()

        self.assertIsNot(msg1,msg2)