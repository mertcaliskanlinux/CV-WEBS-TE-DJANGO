from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Home(models.Model):
    title = models.CharField(max_length=100,verbose_name='BAŞLIK')
    name = models.CharField(max_length=100, verbose_name='AD')
    last_name = models.CharField(max_length=100, verbose_name='SOYAD')
    image = models.ImageField(upload_to = "media/%Y%m%d/")
    description = models.TextField()
    proverb = models.CharField(max_length=300)
    subject_image  = models.ImageField(upload_to = "media/%Y%m%d/")
    

    def __str__(self):
        return self.title

class About(models.Model):
    image_1 = models.ImageField()
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True ,null=True)
    subtitle = models.CharField(max_length=100)
    expertise = models.CharField(max_length=50)
    summary = RichTextField(blank=True ,null=True)
    right_subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to ="media/%Y%m%d/",blank=True,null=True,default=0)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    gmail = models.URLField(max_length=200, blank=True)



    def __str__(self):
        return self.title
    

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/%Y%m%d/", verbose_name='Proje Kapak Fotoğrafı')
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=25)
    image_title = models.CharField(max_length=100,verbose_name='Resim Başlığı')
    image_SS = models.ImageField(upload_to="post/%Y%m%d/", verbose_name='Projenin Ekran Görüntüsü')
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_new", kwargs={"pk": self.pk})
    



class Contact(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField (upload_to="post/%Y%m%d/", verbose_name='BÜYÜK RESİMLER', default="media/kırmızıtsihrt.jpeg")
    first_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email
