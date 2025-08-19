from django.contrib.gis.db import models
from django.core.validators import MinValueValidator


# Enumerations as TextChoices
class TypeRoute(models.TextChoices):
    NATIONALE = 'nationale', 'Nationale'
    REGIONALE = 'regionale', 'Régionale'
    DEPARTEMENTALE = 'departementale', 'Départementale'
    COMMUNALE = 'communale', 'Communale'
    PISTE = 'piste', 'Piste'
    RURALE = 'rurale', 'Rurale'


class TypeEglise(models.TextChoices):
    CATHOLIQUE = 'catholique', 'Catholique'
    PROTESTANT = 'protestant', 'Protestant'
    MUSULMAN = 'musulman', 'Musulman'
    PRESBYTERIENNE = 'presbyterienne', 'Presbytérienne'
    ADVENTISTE = 'adventiste', 'Adventiste'


class TypeStructure(models.TextChoices):
    PAROISSE = 'paroisse', 'Paroisse'
    SEMINAIRE = 'seminaire', 'Séminaire'
    MOSQUEE = 'mosquee', 'Mosquée'
    BASILIQUE = 'basilique', 'Basilique'


class TypeHebergement(models.TextChoices):
    HOTEL = 'hotel', 'Hôtel'
    AUBERGE = 'auberge', 'Auberge'


class TypeServicePublic(models.TextChoices):
    BOUTIQUE = 'boutique', 'Boutique'
    CENTRE_CULTUREL = 'centre_culturel', 'Centre Culturel'
    BOULANGERIE = 'boulangerie', 'Boulangerie'
    RESTAURANT = 'restaurant', 'Restaurant'
    BANQUE = 'banque', 'Banque'
    AUTRES = 'autres', 'Autres'


class TypeEtablissement(models.TextChoices):
    PUBLIC = 'public', 'Public'
    PRIVE_LAIC = 'prive_laic', 'Privé Laïc'
    PRIVE_CONFESSIONNEL = 'prive_confessionnel', 'Privé Confessionnel'


class TypeCentre(models.TextChoices):
    CENTRE_SANTE = 'centre_sante', 'Centre de Santé'
    CLINIQUE = 'clinique', 'Clinique'
    HOPITAL_ARRONDISSEMENT = 'hopital_arrondissement', 'Hôpital d\'Arrondissement'
    HOPITAL_REGIONAL = 'hopital_regional', 'Hôpital Régional'
    HOPITAL_DISTRICT = 'hopital_district', 'Hôpital de District'
    PHARMACIE = 'pharmacie', 'Pharmacie'


class TypeSecurite(models.TextChoices):
    GENDARMERIE = 'gendarmerie', 'Gendarmerie'
    POMPIER = 'pompier', 'Pompier'
    COMMISSARIAT = 'commissariat', 'Commissariat'
    POSTE_POLICE = 'poste_police', 'Poste de Police'


class TypeReligion(models.TextChoices):
    CATHOLIQUE = 'catholique', 'Catholique'
    PROTESTANTE = 'protestante', 'Protestante'
    ADVENTISTE = 'adventiste', 'Adventiste'
    MUSULMANE = 'musulmane', 'Musulmane'
    PRESBYTERIENNE = 'presbyterienne', 'Presbytérienne'
    AUCUNE = 'aucune', 'Aucune'


class TypeFormation(models.TextChoices):
    ACADEMIQUE = 'academique', 'Académique'
    PROFESSIONNELLE = 'professionnelle', 'Professionnelle'


class TypeEnseignement(models.TextChoices):
    BASE = 'base', 'Base'
    SECONDAIRE = 'secondaire', 'Secondaire'
    SUPERIEUR = 'superieur', 'Supérieur'


# class RoleUtilisateur(models.TextChoices):
#     UTILISATEUR_LAMBDA = 'utilisateur_lambda', 'Utilisateur Lambda'
#     DECIDEUR = 'decideur', 'Décideur'
#     TECHNICIEN = 'technicien', 'Technicien'
#     ADMINISTRATEUR = 'administrateur', 'Administrateur'


class TypeServiceProjet(models.TextChoices):
    EGLISE = 'eglise', 'Église'
    HEBERGEMENT = 'hebergement', 'Hébergement'
    SECURITE = 'securite', 'Sécurité'
    SERVICE_PUBLIQUE = 'service_publique', 'Service Publique'
    ENSEIGNEMENT = 'enseignement', 'Enseignement'
    SANTE = 'sante', 'Santé'


# Base Models
class Region(models.Model):
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    superficie = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    
    class Meta:
        verbose_name = "Région"
        verbose_name_plural = "Régions"
    
    def __str__(self):
        return self.nom


class Departement(models.Model):
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    superficie = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='departements')
    
    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"
    
    def __str__(self):
        return self.nom


class Conseiller(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    fin_mandat = models.DateField()
    role = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='conseillers')
    
    class Meta:
        verbose_name = "Conseiller"
        verbose_name_plural = "Conseillers"
    
    def __str__(self):
        return f"{self.nom} - {self.role}"


class Commune(models.Model):
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    superficie = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    maire = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='communes')
    
    class Meta:
        verbose_name = "Commune"
        verbose_name_plural = "Communes"
    
    def __str__(self):
        return self.nom


# Infrastructure Models
class Route(models.Model):
    geom = models.MultiLineStringField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    longueur = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    type = models.CharField(max_length=20, choices=TypeRoute.choices)
    # commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='routes')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='routes')


    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"
    
    def __str__(self):
        return f"{self.nom} ({self.get_type_display()})"


class Hydrographie(models.Model):
    geom = models.MultiLineStringField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    longueur = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    # commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='hydrographies')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='hydrographies')
    
    class Meta:
        verbose_name = "Hydrographie"
        verbose_name_plural = "Hydrographies"
    
    def __str__(self):
        return self.nom


# Service Models
class Sante(models.Model):
    geom = models.PointField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='services_sante')
    
    class Meta:
        verbose_name = "Service de Santé"
        verbose_name_plural = "Services de Santé"
    
    def __str__(self):
        return self.nom


class CentreSante(Sante):
    type = models.CharField(max_length=30, choices=TypeCentre.choices)
    
    class Meta:
        verbose_name = "Centre de Santé"
        verbose_name_plural = "Centres de Santé"


class Pharmacie(Sante):
    nom_pharmacien = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Pharmacie"
        verbose_name_plural = "Pharmacies"


class Enseignement(models.Model):
    geom = models.PointField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    nom_responsable = models.CharField(max_length=100)
    effectif = models.PositiveIntegerField()
    type = models.CharField(max_length=30, choices=TypeEtablissement.choices)
    religion = models.CharField(max_length=20, choices=TypeReligion.choices)
    enseignement = models.CharField(max_length=20, choices=TypeEnseignement.choices)
    formation = models.CharField(max_length=20, choices=TypeFormation.choices)
    meilleur_diplome = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='etablissements_enseignement')
    
    class Meta:
        verbose_name = "Établissement d'Enseignement"
        verbose_name_plural = "Établissements d'Enseignement"
    
    def __str__(self):
        return self.nom


class Eglise(models.Model):
    geom = models.PointField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    type = models.CharField(max_length=20, choices=TypeEglise.choices)
    structure = models.CharField(max_length=20, choices=TypeStructure.choices)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='eglises')
    
    class Meta:
        verbose_name = "Église"
        verbose_name_plural = "Églises"
    
    def __str__(self):
        return self.nom


class Securite(models.Model):
    geom = models.PointField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    nombre_agent = models.PositiveIntegerField()
    type = models.CharField(max_length=20, choices=TypeSecurite.choices)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='services_securite')
    
    class Meta:
        verbose_name = "Service de Sécurité"
        verbose_name_plural = "Services de Sécurité"
    
    def __str__(self):
        return self.nom


class Hebergement(models.Model):
    geom = models.PointField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    nb_chambres = models.PositiveIntegerField()
    type = models.CharField(max_length=20, choices=TypeHebergement.choices)
    standing = models.CharField(max_length=50)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='hebergements')
    
    class Meta:
        verbose_name = "Hébergement"
        verbose_name_plural = "Hébergements"
    
    def __str__(self):
        return self.nom


class ServicePublique(models.Model):
    geom = models.PointField(srid=4326,blank=True, null=True)
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TypeServicePublic.choices)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='services_publiques')
    
    class Meta:
        verbose_name = "Service Publique"
        verbose_name_plural = "Services Publiques"
    
    def __str__(self):
        return self.nom


class Projet(models.Model):
    nom_contractant = models.CharField(max_length=100)
    description = models.TextField()
    montant = models.PositiveIntegerField()
    date_debut = models.DateField()
    date_livraison = models.DateField()
    service = models.CharField(max_length=20, choices=TypeServiceProjet.choices)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='projets')
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
    
    def __str__(self):
        return f"{self.nom_contractant} - {self.description[:50]}"

