from django.db import models
from core.models import IndexedTimeStampedModel
from users.models import User
# Create your models here.

class Subrediti(models.Model):
    title = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    criador = models.ForeignKey('users.User', related_name='subreditis', on_delete=models.CASCADE)
    slug = models.SlugField()#usado para deixar o url mais legivel
    def __str__(self):
        return self.title

class Thread(IndexedTimeStampedModel):
    title = models.CharField(max_length=50)
    autor = models.ForeignKey('users.User', related_name='threads', on_delete=models.CASCADE)
    Subrediti = models.ForeignKey('Subrediti', related_name='threads', on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Post(IndexedTimeStampedModel):
    content = models.TextField()
    autor = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)#aqui não usamos a key direto, pois ele ainda não estava importado
    thread = models.ForeignKey('Thread', related_name="posts", on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return ("{} - {} - {}").format(self.id, self.thread, self.author)


class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='subscription', on_delete=models.CASCADE)#aqui podemos usar a key direto, pois já estava importado
    sub = models.ForeignKey(Subrediti, related_name='subscription', on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)#vai dizer se ta inscrito ou não
    class Meta:
        unique_together = [('sub', 'user')]#impede que a mesma subscription seja criado com o mesmo usuário e o mesmo subrediti

    def __str__(self):
        return ("{} - {}".format(self.sub, self.user))