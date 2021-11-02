from django.db import models
from client.models import Client


# la table des voitures 
class Voiture (models.Model) :
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    marque_voiture = models.CharField(max_length=30,null=True)
    modele_du_voiture = models.CharField(max_length=30,null=True)
    image_de_voiture = models.ImageField(blank=True)
    date_de_l_annonce = models.DateTimeField(auto_now_add=True)
    nombre_de_place = models.IntegerField(null=True)
    TYPE_DE_VOITURE = [
        ('CITADINE','citadine'),
        ('CABRIOLET','cabriolet'),
        ('COUPÉ','coupé'),
        ('SUV','suv'),
        ('BERLINE','berline'),
        ('BREAK','break'),
        ('UTILITAIRE','utilitaire'),
        ('MONOSPACE','monospace'),
        ('AUTRES','autres'),
    ]
    type_de_voiture = models.CharField(choices=TYPE_DE_VOITURE, max_length=20, null=True)
    prix = models.FloatField(null=True)
    reserver = models.BooleanField(default=False, null=True)
    louer = models.BooleanField(default=False, null=True)



    def __str__(self) :
        return "{} {}".format(self.marque_voiture, self.modele_du_voiture)