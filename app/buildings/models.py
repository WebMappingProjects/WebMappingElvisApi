
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models



class AfricaRegion(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=20, blank=True, null=True)
    continent = models.CharField(max_length=30, blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    fips = models.CharField(max_length=2, blank=True, null=True)
    iso_2 = models.CharField(max_length=2, blank=True, null=True)
    iso_3 = models.CharField(max_length=3, blank=True, null=True)
    pop_1994 = models.BigIntegerField(blank=True, null=True)
    pop_grw_rt = models.FloatField(blank=True, null=True)
    pop_male = models.BigIntegerField(blank=True, null=True)
    pop_fem = models.BigIntegerField(blank=True, null=True)
    pop_0_14 = models.BigIntegerField(blank=True, null=True)
    pop_15_64 = models.BigIntegerField(blank=True, null=True)
    pop_65plus = models.BigIntegerField(blank=True, null=True)
    male_0_14 = models.BigIntegerField(blank=True, null=True)
    male_15_64 = models.BigIntegerField(blank=True, null=True)
    number_65plus = models.BigIntegerField(db_column='65plus', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    fem_0_14 = models.BigIntegerField(blank=True, null=True)
    fem_15_64 = models.BigIntegerField(blank=True, null=True)
    fem_65plus = models.BigIntegerField(blank=True, null=True)
    pop_urban = models.BigIntegerField(blank=True, null=True)
    pop_rural = models.BigIntegerField(blank=True, null=True)
    urb_male = models.BigIntegerField(blank=True, null=True)
    urb_fem = models.BigIntegerField(blank=True, null=True)
    rur_male = models.BigIntegerField(blank=True, null=True)
    rur_fem = models.BigIntegerField(blank=True, null=True)
    arable_pct = models.FloatField(blank=True, null=True)
    literacy = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rate0 = models.FloatField(blank=True, null=True)
    growth = models.FloatField(blank=True, null=True)
    colorcode = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'africa_region'


class AgencesDeVoyagesFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    quartier = models.CharField(max_length=50, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)
    coord_x = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    coord_y = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'agences_de_voyages_font_point'


class AmbassadesPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=59, blank=True, null=True)
    telephone = models.CharField(max_length=26, blank=True, null=True)
    postale = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    longitude = models.CharField(max_length=9, blank=True, null=True)
    latitude = models.CharField(max_length=9, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'ambassades_point'


class ArmeeFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=60, blank=True, null=True)
    type = models.CharField(max_length=60, blank=True, null=True)
    quartier = models.CharField(max_length=60, blank=True, null=True)
    arrondisse = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'armee_font_point'


class ArrondAireMetrop(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    departemen = models.CharField(max_length=30, blank=True, null=True)
    codedepart = models.CharField(max_length=6, blank=True, null=True)
    arrond = models.CharField(max_length=30, blank=True, null=True)
    codearrond = models.CharField(max_length=9, blank=True, null=True)
    arr_minatd = models.CharField(max_length=6, blank=True, null=True)
    cir_ad = models.CharField(max_length=30, blank=True, null=True)
    resultat = models.CharField(max_length=100, blank=True, null=True)
    nbinscrit = models.FloatField(blank=True, null=True)
    bulletinnu = models.FloatField(blank=True, null=True)
    suffrage = models.FloatField(blank=True, null=True)
    nbbv = models.FloatField(blank=True, null=True)
    responsabl = models.CharField(max_length=100, blank=True, null=True)
    nbreinscri = models.FloatField(blank=True, null=True)
    mi_prinx = models.BigIntegerField(blank=True, null=True)
    rdpc = models.FloatField(blank=True, null=True)
    sdf = models.FloatField(blank=True, null=True)
    udc = models.FloatField(blank=True, null=True)
    upc = models.FloatField(blank=True, null=True)
    undp = models.FloatField(blank=True, null=True)
    add = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'arrond_aire_metrop'


class AubergesCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.BigIntegerField(blank=True, null=True)
    telephonni = models.BigIntegerField(blank=True, null=True)
    quartier = models.CharField(max_length=30, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'auberges_custom_point'



class AxesVoiriesPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    numrue = models.IntegerField(blank=True, null=True)
    hierarchie = models.CharField(max_length=2, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nomrue = models.CharField(max_length=39, blank=True, null=True)
    axes_id = models.IntegerField(blank=True, null=True)
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    axes_field = models.IntegerField(db_column='axes_', blank=True, null=True)  # Field renamed because it ended with '_'.
    type_axe = models.CharField(max_length=20, blank=True, null=True)
    etat = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'axes_voiries_polyline'


class BacsFontPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    capacite = models.CharField(max_length=10, blank=True, null=True)
    cordx = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    cordy = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'bacs_font_point'


class BacsPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    capacite = models.CharField(max_length=10, blank=True, null=True)
    cordx = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    cordy = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'bacs_point'


class BanquesEtMicrofinancesCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.BigIntegerField(blank=True, null=True)
    telephoniq = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    quartier = models.CharField(max_length=50, blank=True, null=True)
    arrondisse = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'banques_et_microfinances_custom_point'


class BassinVersantMfoundiBasRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    bassin_id = models.IntegerField(blank=True, null=True)
    bassin_field = models.IntegerField(db_column='bassin_', blank=True, null=True)  # Field renamed because it ended with '_'.
    perimeter = models.FloatField(blank=True, null=True)
    n_bv = models.CharField(max_length=2, blank=True, null=True)
    cours_bv = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        db_table = 'bassin_versant_mfoundi_bas_region'


class BassinVersantMfoundiRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    nom_bassin = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'bassin_versant_mfoundi_region'


class BassinVersantNone(models.Model):
    area = models.FloatField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    bassin_id = models.IntegerField(blank=True, null=True)
    bassin_field = models.IntegerField(db_column='bassin_', blank=True, null=True)  # Field renamed because it ended with '_'.
    perimeter = models.FloatField(blank=True, null=True)
    n_bv = models.CharField(max_length=2, blank=True, null=True)
    cours_bv = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        db_table = 'bassin_versant_none'


class BassinVersantRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    bassin_id = models.IntegerField(blank=True, null=True)
    bassin_field = models.IntegerField(db_column='bassin_', blank=True, null=True)  # Field renamed because it ended with '_'.
    perimeter = models.FloatField(blank=True, null=True)
    n_bv = models.CharField(max_length=2, blank=True, null=True)
    cours_bv = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        db_table = 'bassin_versant_region'


class BatiDurPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    bati_d_id = models.IntegerField(blank=True, null=True)
    bati_d_field = models.IntegerField(db_column='bati_d_', blank=True, null=True)  # Field renamed because it ended with '_'.
    elevation = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        db_table = 'bati_dur_polyline'


class BatiLocauxPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    serre_id = models.IntegerField(blank=True, null=True)
    serre_field = models.IntegerField(db_column='serre_', blank=True, null=True)  # Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        db_table = 'bati_locaux_polyline'


class BatiPublicsPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    bati_p_field = models.IntegerField(db_column='bati_p_', blank=True, null=True)  # Field renamed because it ended with '_'.
    perimeter = models.FloatField(blank=True, null=True)
    bati_p_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'bati_publics_point'


class BatiPublicsRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    bati_p_field = models.IntegerField(db_column='bati_p_', blank=True, null=True)  # Field renamed because it ended with '_'.
    perimeter = models.FloatField(blank=True, null=True)
    bati_p_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'bati_publics_region'


class BatimentsYaoundePoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    batiment_i = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    batiment_field = models.IntegerField(db_column='batiment_', blank=True, null=True)  # Field renamed because it ended with '_'.
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'batiments_yaounde_point'


class BatimentsYaoundePolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    batiment_i = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    batiment_field = models.IntegerField(db_column='batiment_', blank=True, null=True)  # Field renamed because it ended with '_'.
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'batiments_yaounde_polyline'


class BatimentsYaoundeRegion(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    batiment_i = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    batiment_field = models.IntegerField(db_column='batiment_', blank=True, null=True)  # Field renamed because it ended with '_'.
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'batiments_yaounde_region'


class BouchesIncendiesYdeCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    matricule = models.CharField(max_length=31, blank=True, null=True)
    insertion = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    insertio0 = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    insertio1 = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    symbole = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'bouches_incendies_yde_custom_point'


class BouchesIncendiesYdePoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    matricule = models.CharField(max_length=31, blank=True, null=True)
    insertion = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    insertio0 = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    insertio1 = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    symbole = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'bouches_incendies_yde_point'


class BoulangeriesCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=75, blank=True, null=True)
    quartier = models.CharField(max_length=15, blank=True, null=True)
    arrondisse = models.CharField(max_length=15, blank=True, null=True)
    standing = models.CharField(max_length=15, blank=True, null=True)
    t_l_phone = models.BigIntegerField(db_column='t�l�phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    postale = models.BigIntegerField(blank=True, null=True)
    propri_tai = models.CharField(db_column='propri�tai', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'boulangeries_custom_point'


class BoulangeriesRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=75, blank=True, null=True)
    quartier = models.CharField(max_length=15, blank=True, null=True)
    arrondisse = models.CharField(max_length=15, blank=True, null=True)
    standing = models.CharField(max_length=15, blank=True, null=True)
    t_l_phone = models.BigIntegerField(db_column='t�l�phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    postale = models.BigIntegerField(blank=True, null=True)
    propri_tai = models.CharField(db_column='propri�tai', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'boulangeries_region'


class CampSicCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=60, blank=True, null=True)
    quartier = models.CharField(max_length=60, blank=True, null=True)
    arrondisse = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'camp_sic_custom_point'


class CentreSpecialDetatCivilFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    quartier = models.CharField(max_length=50, blank=True, null=True)
    arrondisse = models.CharField(max_length=50, blank=True, null=True)
    coord_x = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    coord_y = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'centre_special_detat_civil_font_point'


class CentresCulturelsCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    coord_x = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    coord_y = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    nom = models.CharField(max_length=49, blank=True, null=True)
    quartier = models.CharField(max_length=21, blank=True, null=True)
    promoteur = models.CharField(max_length=25, blank=True, null=True)
    t_l_phone = models.IntegerField(db_column='t�l�phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    e_mail = models.CharField(max_length=23, blank=True, null=True)
    postale = models.IntegerField(blank=True, null=True)
    offerts = models.CharField(max_length=100, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'centres_culturels_custom_point'


class CimetiereRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    cimeti_re = models.CharField(db_column='cimeti�re', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    localisati = models.CharField(max_length=25, blank=True, null=True)
    arrondiss = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'cimetiere_region'


class CinemaCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=49, blank=True, null=True)
    promoteur = models.CharField(max_length=25, blank=True, null=True)
    t_l_phone = models.IntegerField(db_column='t�l�phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    e_mail = models.CharField(max_length=23, blank=True, null=True)
    postale = models.IntegerField(blank=True, null=True)
    offerts = models.CharField(max_length=100, blank=True, null=True)
    quartier = models.CharField(max_length=21, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)
    coord_x = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    coord_y = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'cinema_custom_point'


class CitesMunicipalesCuyPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=24, blank=True, null=True)
    sup = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    estim_e_field = models.DecimalField(db_column='estim�e__', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=16, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'cites_municipales_cuy_point'


class CommissariatsYdeFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    num_ro = models.BigIntegerField(db_column='num�ro', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nom = models.CharField(max_length=100, blank=True, null=True)
    localisati = models.CharField(max_length=70, blank=True, null=True)
    contact = models.CharField(max_length=40, blank=True, null=True)
    commissari = models.CharField(max_length=40, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'commissariats_yde_font_point'


class ComplexesSportifsCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    coord_x = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    coord_y = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    noms = models.CharField(max_length=37, blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)
    quartier = models.CharField(max_length=21, blank=True, null=True)
    discipline = models.CharField(max_length=32, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)
    standing = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'complexes_sportifs_custom_point'


class ConsulatsPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=40, blank=True, null=True)
    postale = models.CharField(max_length=40, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'consulats_point'


class DelegationsCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    quartier = models.CharField(max_length=30, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'delegations_custom_point'


class DepAireMetrop(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    minatd = models.CharField(max_length=3, blank=True, null=True)
    code_prov = models.CharField(max_length=6, blank=True, null=True)
    departemen = models.CharField(max_length=6, blank=True, null=True)
    départemen = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    numéro = models.FloatField(blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    chef_lieu = models.CharField(max_length=30, blank=True, null=True)
    rdpc = models.FloatField(blank=True, null=True)
    sdf = models.FloatField(blank=True, null=True)
    udc = models.FloatField(blank=True, null=True)
    upc = models.FloatField(blank=True, null=True)
    undp = models.FloatField(blank=True, null=True)
    add = models.FloatField(blank=True, null=True)
    nbre_bv = models.FloatField(blank=True, null=True)
    population = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'dep_aire_metrop'




class EcoleNormaleDesInstituteursDenseignementGeneralPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    numero = models.CharField(max_length=5, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    localisati = models.CharField(max_length=20, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'ecole_normale_des_instituteurs_denseignement_general_point'


class EcolesMatPrimairePoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    code_ecole = models.CharField(max_length=10, blank=True, null=True)
    nom = models.CharField(max_length=60, blank=True, null=True)
    telephone = models.CharField(max_length=19, blank=True, null=True)
    bp = models.CharField(max_length=10, blank=True, null=True)
    quartier = models.CharField(max_length=30, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'ecoles_mat_primaire_point'


class EglisesCatholiquesFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=40, blank=True, null=True)
    postale = models.CharField(max_length=15, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    categorie = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'eglises_catholiques_font_point'


class EglisesPresbyteriennesFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    postale = models.CharField(max_length=15, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    categorie = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'eglises_presbyteriennes_font_point'


class EglisesProtestantesPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    telephonne = models.CharField(max_length=40, blank=True, null=True)
    postale = models.CharField(max_length=15, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    categorie = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'eglises_protestantes_point'


class EnseignementDeBaseFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    numero = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    nom = models.CharField(max_length=60, blank=True, null=True)
    telephone = models.CharField(max_length=19, blank=True, null=True)
    bp = models.CharField(max_length=10, blank=True, null=True)
    quartier = models.CharField(max_length=30, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'enseignement_de_base_font_point'


class EnseignementMaternelleCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    ecoles = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    postale = models.CharField(max_length=20, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)
    cordx = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    cordy = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'enseignement_maternelle_custom_point'


class EnseignementMaternelleRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    ecoles = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    postale = models.CharField(max_length=20, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)
    cordx = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    cordy = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'enseignement_maternelle_region'


class EnseignementPrimaireFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    publics = models.CharField(max_length=70, blank=True, null=True)
    quartier0 = models.CharField(max_length=30, blank=True, null=True)
    tel_phone = models.CharField(db_column='tel�phone', max_length=20, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bp = models.CharField(max_length=10, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'enseignement_primaire_font_point'


class EnseignementPrimaireRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    publics = models.CharField(max_length=70, blank=True, null=True)
    quartier0 = models.CharField(max_length=30, blank=True, null=True)
    tel_phone = models.CharField(db_column='tel�phone', max_length=20, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bp = models.CharField(max_length=10, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'enseignement_primaire_region'


class EnseignementSuperieurCustomPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    fax = models.CharField(max_length=11, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    arrondisse = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'enseignement_superieur_custom_point'


class EnseignementsSecondairesFinalPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    numero = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    etablissem = models.CharField(max_length=45, blank=True, null=True)
    localisati = models.CharField(max_length=34, blank=True, null=True)
    fondateur = models.CharField(max_length=31, blank=True, null=True)
    contact = models.CharField(max_length=35, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'enseignements_secondaires_final_point'


class EspaceVertEllipse(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    espace = models.CharField(max_length=20, blank=True, null=True)
    denominati = models.CharField(max_length=50, blank=True, null=True)
    etat = models.CharField(max_length=20, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'espace_vert_ellipse'


class EspaceVertRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    espace = models.CharField(max_length=20, blank=True, null=True)
    denominati = models.CharField(max_length=50, blank=True, null=True)
    etat = models.CharField(max_length=20, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'espace_vert_region'


class EspacesAmenagesRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    numeo_code = models.BigIntegerField(blank=True, null=True)
    lieu = models.CharField(max_length=30, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    creation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'espaces_amenages_region'


class EtalonnagePolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    zone = models.CharField(max_length=10, blank=True, null=True)
    circuit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'etalonnage_polyline'


class FeuTricoloreCustomPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    non = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'feu_tricolore_custom_point'


class FeuTricoloreEllipse(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    non = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'feu_tricolore_ellipse'


class FeuTricolorePolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    non = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'feu_tricolore_polyline'


class FeuTricoloreRegion(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    non = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'feu_tricolore_region'


class GaragesCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    t_l_phone = models.CharField(db_column='t�l�phone', max_length=20, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    postale = models.CharField(max_length=40, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    standing = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'garages_custom_point'


class GareFerroviaireCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=39, blank=True, null=True)
    sup = models.CharField(max_length=1, blank=True, null=True)
    estim_e_field = models.CharField(db_column='estim�e__', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.CharField(max_length=1, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=39, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'gare_ferroviaire_custom_point'


class GaresRoutieresCuyPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=39, blank=True, null=True)
    sup = models.CharField(max_length=1, blank=True, null=True)
    estim_e_field = models.CharField(db_column='estim�e__', max_length=1, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.CharField(max_length=1, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=39, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'gares_routieres_cuy_point'


class GendarmeriesPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    numero = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    d_nominati = models.CharField(db_column='d�nominati', max_length=80, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bo_te_post = models.CharField(db_column='bo�te_post', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    num_ro_t_l = models.CharField(db_column='num�ro_t�l', max_length=12, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sp_cialisa = models.CharField(db_column='sp�cialisa', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_rim_tre_field = models.CharField(db_column='p�rim�tre_', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    localisati = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'gendarmeries_point'


class HangarsPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    hangar_id = models.IntegerField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    hangar_field = models.IntegerField(db_column='hangar_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        db_table = 'hangars_polyline'


class HotelsFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom_h_tel = models.CharField(db_column='nom_h�tel', max_length=35, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    postale = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=40, blank=True, null=True)
    quartier = models.CharField(max_length=21, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)
    restaurant = models.IntegerField(blank=True, null=True)
    piscine = models.IntegerField(blank=True, null=True)
    appartemen = models.IntegerField(blank=True, null=True)
    chambre = models.IntegerField(blank=True, null=True)
    conf_rence = models.IntegerField(db_column='conf�rence', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    night_club = models.IntegerField(blank=True, null=True)
    suites = models.IntegerField(blank=True, null=True)
    bars = models.IntegerField(blank=True, null=True)
    golf = models.IntegerField(blank=True, null=True)
    standing = models.CharField(max_length=6, blank=True, null=True)
    tennis = models.IntegerField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'hotels_font_point'


class HussiersYdeCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    num_ro = models.DecimalField(db_column='num�ro', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nom = models.CharField(max_length=28, blank=True, null=True)
    charge = models.CharField(max_length=6, blank=True, null=True)
    localisati = models.CharField(max_length=74, blank=True, null=True)
    t_l_phone = models.CharField(db_column='t�l�phone', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    quartier = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'hussiers_yde_custom_point'


class ItinerairePrcPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    itineraire = models.BigIntegerField(blank=True, null=True)
    it = models.CharField(max_length=20, blank=True, null=True)
    lineaire = models.CharField(max_length=20, blank=True, null=True)
    etat = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'itineraire_prc_polyline'


class LacHorsCartoRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'lac_hors_carto_region'


class LacRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    lac_id = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    lac_field = models.IntegerField(db_column='lac_', blank=True, null=True)  # Field renamed because it ended with '_'.
    perimeter = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'lac_region'


class LaveriesFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.BigIntegerField(blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    standing = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'laveries_font_point'


class Layer(models.Model):
    topology = models.OneToOneField('Topology', models.DO_NOTHING, primary_key=True)  # The composite primary key (topology_id, layer_id) found, that is not supported. The first column is selected.
    layer_id = models.IntegerField()
    schema_name = models.CharField()
    table_name = models.CharField()
    feature_column = models.CharField()
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class LeMfoundiPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=32, blank=True, null=True)
    longueur = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    sens = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'le_mfoundi_polyline'


class LieuxRemarquablesCustomPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    descriptio = models.CharField(max_length=14, blank=True, null=True)
    nom = models.CharField(max_length=42, blank=True, null=True)

    class Meta:
        db_table = 'lieux_remarquables_custom_point'


class LieuxRemarquablesFontPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    descriptio = models.CharField(max_length=14, blank=True, null=True)
    nom = models.CharField(max_length=42, blank=True, null=True)

    class Meta:
        db_table = 'lieux_remarquables_font_point'


class LieuxRemarquablesPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    descriptio = models.CharField(max_length=14, blank=True, null=True)
    nom = models.CharField(max_length=42, blank=True, null=True)

    class Meta:
        db_table = 'lieux_remarquables_point'


class LigneBusPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    lineaire = models.CharField(max_length=10, blank=True, null=True)
    designatio = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'ligne_bus_polyline'


class LigneBusProjetPolyline(models.Model):
    geom = models.MultiLineStringField(srid=0, blank=True, null=True)
    num_ligne = models.CharField(max_length=10, blank=True, null=True)
    arret = models.BigIntegerField(blank=True, null=True)
    itineraire = models.CharField(max_length=254, blank=True, null=True)
    lineaire = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'ligne_bus_projet_polyline'


class LimiteMokoloPolyline(models.Model):
    geom = models.MultiLineStringField(srid=0, blank=True, null=True)
    sup = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'limite_mokolo_polyline'


class LimiteYde(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    minatd = models.CharField(max_length=3, blank=True, null=True)
    code_prov = models.CharField(max_length=6, blank=True, null=True)
    departemen = models.CharField(max_length=6, blank=True, null=True)
    départemen = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    numéro = models.FloatField(blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    chef_lieu = models.CharField(max_length=30, blank=True, null=True)
    rdpc = models.FloatField(blank=True, null=True)
    sdf = models.FloatField(blank=True, null=True)
    udc = models.FloatField(blank=True, null=True)
    upc = models.FloatField(blank=True, null=True)
    undp = models.FloatField(blank=True, null=True)
    add = models.FloatField(blank=True, null=True)
    nbre_bv = models.FloatField(blank=True, null=True)
    population = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'limite_yde'


class LimiteYde1Region(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'limite_yde1_region'


class LimitesDesCommunesYdeRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    population = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    malades = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    pourcentag = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'limites_des_communes_yde_region'


class MairiesYaoundeCustomPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=22, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'mairies_yaounde_custom_point'


class MarcheEligedzoaRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    nommarche = models.CharField(max_length=20, blank=True, null=True)
    nbreboutiq = models.CharField(max_length=20, blank=True, null=True)
    nbrehangar = models.CharField(max_length=20, blank=True, null=True)
    pricipalea = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'marche_eligedzoa_region'


class MarcheEligedzoaZoneActiviteRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    nommarche = models.CharField(max_length=20, blank=True, null=True)
    nbreboutiq = models.CharField(max_length=20, blank=True, null=True)
    nbrehangar = models.CharField(max_length=20, blank=True, null=True)
    pricipalea = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'marche_eligedzoa_zone_activite_region'


class MarcheMokoloRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'marche_mokolo_region'


class MarchesCommunauxCuyPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=31, blank=True, null=True)
    sup = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    estim_e_field = models.DecimalField(db_column='estim�e__', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=41, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'marches_communaux_cuy_point'


class MarchesCuyPoint(models.Model):
    geom = models.PointField(srid=0, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)
    designatio = models.CharField(max_length=20, blank=True, null=True)
    commune = models.CharField(max_length=20, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    superficie = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    age_util = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    cptoire = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    boutique = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    commer_ant = models.DecimalField(db_column='commer�ant', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hangard = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    principale = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'marches_cuy_point'


class MarchesPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=31, blank=True, null=True)
    sup = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    estim_e_field = models.DecimalField(db_column='estim�e__', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=41, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'marches_point'


class MarchesRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=31, blank=True, null=True)
    sup = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    estim_e_field = models.DecimalField(db_column='estim�e__', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=41, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'marches_region'


class MinisteresYaoundeCustomPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    nom = models.CharField(max_length=72, blank=True, null=True)
    sigle = models.CharField(max_length=10, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'ministeres_yaounde_custom_point'


class MonumentsEllipse(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)
    monument = models.CharField(max_length=25, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    creation = models.CharField(max_length=25, blank=True, null=True)
    significat = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        db_table = 'monuments_ellipse'


class MonumentsRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)
    monument = models.CharField(max_length=25, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    creation = models.CharField(max_length=25, blank=True, null=True)
    significat = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        db_table = 'monuments_region'


class MosqueesFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    telephonne = models.BigIntegerField(blank=True, null=True)
    postale = models.BigIntegerField(blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    categorie = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'mosquees_font_point'


class MursPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    mur_sp_field = models.IntegerField(db_column='mur_sp_', blank=True, null=True)  # Field renamed because it ended with '_'.
    elevation = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    mur_sp_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'murs_polyline'


class NationsUniesPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=97, blank=True, null=True)
    telephone = models.CharField(max_length=25, blank=True, null=True)
    postale = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'nations_unies_point'


class ParkingsCuy2007Polyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    libelle = models.CharField(max_length=25, blank=True, null=True)
    rue = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    field_total = models.DecimalField(db_column='_total', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it started with '_'.
    field_reserv_field = models.DecimalField(db_column='_reserv�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    pr_pt = models.CharField(max_length=10, blank=True, null=True)
    longueur = models.FloatField(blank=True, null=True)
    localisati = models.CharField(max_length=30, blank=True, null=True)
    observatio = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        db_table = 'parkings_cuy_2007_polyline'


class ParkingsCuyPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    localisati = models.CharField(max_length=30, blank=True, null=True)
    num_rue = models.CharField(max_length=8, blank=True, null=True)
    nature = models.CharField(max_length=25, blank=True, null=True)
    parking = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    offertes = models.BigIntegerField(blank=True, null=True)
    occup = models.BigIntegerField(blank=True, null=True)
    longueur = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'parkings_cuy_polyline'


class PharmaciesPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    numero = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    noms = models.CharField(max_length=100, blank=True, null=True)
    localisati = models.CharField(max_length=39, blank=True, null=True)
    pharmacien = models.CharField(max_length=57, blank=True, null=True)
    t_l_phone = models.CharField(db_column='t�l�phone', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bo_te_post = models.CharField(db_column='bo�te_post', max_length=17, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    quartier = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    arrondisse = models.CharField(max_length=15, blank=True, null=True)
    ouverture = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'pharmacies_point'


class PrefecturesSousPrefecturesCustomPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    nom = models.CharField(max_length=38, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'prefectures_sous-prefectures_custom_point'


class ProjetsRouteEllipse(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    lineaire = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'projets_route_ellipse'


class ProjetsRoutePolyline(models.Model):
    geom = models.MultiLineStringField(srid=0, blank=True, null=True)
    lineaire = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'projets_route_polyline'


class QuadrillageNone(models.Model):
    code_ville = models.IntegerField(blank=True, null=True)
    id_feuille = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    ces = models.FloatField(blank=True, null=True)
    cos = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    recule = models.CharField(max_length=20, blank=True, null=True)
    alignement = models.CharField(max_length=20, blank=True, null=True)
    obli_archi = models.CharField(max_length=20, blank=True, null=True)
    cloture = models.CharField(max_length=20, blank=True, null=True)
    baies = models.FloatField(blank=True, null=True)
    aveugle = models.FloatField(blank=True, null=True)
    interdits = models.CharField(max_length=200, blank=True, null=True)
    voirie = models.CharField(max_length=250, blank=True, null=True)
    min_lot = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'quadrillage_none'


class QuadrillagePoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    code_ville = models.IntegerField(blank=True, null=True)
    id_feuille = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    ces = models.FloatField(blank=True, null=True)
    cos = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    recule = models.CharField(max_length=20, blank=True, null=True)
    alignement = models.CharField(max_length=20, blank=True, null=True)
    obli_archi = models.CharField(max_length=20, blank=True, null=True)
    cloture = models.CharField(max_length=20, blank=True, null=True)
    baies = models.FloatField(blank=True, null=True)
    aveugle = models.FloatField(blank=True, null=True)
    interdits = models.CharField(max_length=200, blank=True, null=True)
    voirie = models.CharField(max_length=250, blank=True, null=True)
    min_lot = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'quadrillage_point'


class QuadrillageRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    code_ville = models.IntegerField(blank=True, null=True)
    id_feuille = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    ces = models.FloatField(blank=True, null=True)
    cos = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    recule = models.CharField(max_length=20, blank=True, null=True)
    alignement = models.CharField(max_length=20, blank=True, null=True)
    obli_archi = models.CharField(max_length=20, blank=True, null=True)
    cloture = models.CharField(max_length=20, blank=True, null=True)
    baies = models.FloatField(blank=True, null=True)
    aveugle = models.FloatField(blank=True, null=True)
    interdits = models.CharField(max_length=200, blank=True, null=True)
    voirie = models.CharField(max_length=250, blank=True, null=True)
    min_lot = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'quadrillage_region'


class QuartierRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    quartier = models.CharField(max_length=21, blank=True, null=True)
    arrondisse = models.CharField(max_length=30, blank=True, null=True)
    secondaire = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'quartier_region'


class QuartiersPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    texte = models.CharField(max_length=18, blank=True, null=True)
    equipement = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'quartiers_point'


class RadioYaoundeCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    long = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    lat = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    frequence = models.CharField(max_length=15, blank=True, null=True)
    typologie = models.CharField(max_length=20, blank=True, null=True)
    t_l_phone = models.DecimalField(db_column='t�l�phone', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    postale = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    localisati = models.CharField(max_length=100, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    arrondisse = models.CharField(max_length=15, blank=True, null=True)
    statut = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'radio_yaounde_custom_point'


class ReligionsYaoundeFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=40, blank=True, null=True)
    postale = models.CharField(max_length=15, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    categorie = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'religions_yaounde_font_point'


class ReligionsYaoundePoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=40, blank=True, null=True)
    postale = models.CharField(max_length=15, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    categorie = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'religions_yaounde_point'


class ReseauEpPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    ep = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'reseau_ep_polyline'


class RestaurantsYaoundeFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    coord_x = models.IntegerField(blank=True, null=True)
    coord_y = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=27, blank=True, null=True)
    t_lephone = models.CharField(db_column='t�lephone', max_length=11, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    postale = models.IntegerField(blank=True, null=True)
    quartier = models.CharField(max_length=21, blank=True, null=True)
    standing = models.CharField(max_length=33, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'restaurants_yaounde_font_point'


class RivieresPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=32, blank=True, null=True)
    longueur = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    sens = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'rivieres_polyline'


class RivieresRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=32, blank=True, null=True)
    longueur = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    sens = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'rivieres_region'


class RouteEnProjetPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    nom_rue = models.CharField(max_length=10, blank=True, null=True)
    lineraire = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'route_en_projet_polyline'


class SanitaireYaoundePoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=51, blank=True, null=True)
    statut = models.CharField(max_length=16, blank=True, null=True)
    categorie = models.CharField(max_length=33, blank=True, null=True)
    promoteur = models.CharField(max_length=31, blank=True, null=True)
    t_lephone = models.CharField(db_column='t�lephone', max_length=21, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    postale = models.CharField(max_length=21, blank=True, null=True)
    de_sante = models.IntegerField(blank=True, null=True)
    de_sante0 = models.CharField(max_length=21, blank=True, null=True)
    district = models.CharField(max_length=11, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    coord_x = models.FloatField(blank=True, null=True)
    coord_y = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'sanitaire_yaounde_point'


class SapeursPompierPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    quartier = models.CharField(max_length=25, blank=True, null=True)
    arrondisse = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'sapeurs_pompier_point'


class ServicesCuyPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    n_field = models.BigIntegerField(db_column='n_', blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=43, blank=True, null=True)
    sup = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    estim_e_field = models.DecimalField(db_column='estim�e__', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=29, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'services_cuy_point'


class StationsSevicesFontPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.BigIntegerField(blank=True, null=True)
    telephonni = models.BigIntegerField(blank=True, null=True)
    quartier = models.CharField(max_length=20, blank=True, null=True)
    arrondisse = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'stations_sevices_font_point'


class SupZoneUrbaRegion(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    sup = models.IntegerField(blank=True, null=True)
    arrond = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sup_zone_urba_region'


class TerrainsDeSportsCustomPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    coord_x = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    coord_y = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    noms = models.CharField(max_length=37, blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)
    standing = models.CharField(max_length=30, blank=True, null=True)
    quartier = models.CharField(max_length=21, blank=True, null=True)
    discipline = models.CharField(max_length=32, blank=True, null=True)
    commune = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'terrains_de_sports_custom_point'


class ToilettesPubliquesCuyPoint(models.Model):
    geom = models.PointField(srid=32632, blank=True, null=True)
    n_field = models.DecimalField(db_column='n_', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it ended with '_'.
    designatio = models.CharField(max_length=23, blank=True, null=True)
    sup = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    estim_e_field = models.DecimalField(db_column='estim�e__', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    age_utile = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    actualisee = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    neuf_au_m_field = models.DecimalField(db_column='neuf_au_m�', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualis_e = models.DecimalField(db_column='actualis�e', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_field = models.DecimalField(db_column='___', max_digits=30, decimal_places=15, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    observatri = models.CharField(max_length=19, blank=True, null=True)
    quartier = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'toilettes_publiques_cuy_point'


class Topology(models.Model):
    name = models.CharField(unique=True)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        db_table = 'topology'


class VoieFerreePolyline(models.Model):
    geom = models.MultiLineStringField(srid=32632, blank=True, null=True)
    voifer_id = models.IntegerField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    voifer_field = models.IntegerField(db_column='voifer_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        db_table = 'voie_ferree_polyline'


class VoiriesYaoundePoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    voirie_field = models.IntegerField(db_column='voirie_', blank=True, null=True)  # Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    voirie_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'voiries_yaounde_point'


class VoiriesYaoundePolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    voirie_field = models.IntegerField(db_column='voirie_', blank=True, null=True)  # Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    tnode_field = models.IntegerField(db_column='tnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fnode_field = models.IntegerField(db_column='fnode_', blank=True, null=True)  # Field renamed because it ended with '_'.
    rpoly_field = models.IntegerField(db_column='rpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lpoly_field = models.IntegerField(db_column='lpoly_', blank=True, null=True)  # Field renamed because it ended with '_'.
    voirie_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'voiries_yaounde_polyline'


class WorldFontPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=20, blank=True, null=True)
    continent = models.CharField(max_length=30, blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    fips = models.CharField(max_length=2, blank=True, null=True)
    iso_2 = models.CharField(max_length=2, blank=True, null=True)
    iso_3 = models.CharField(max_length=3, blank=True, null=True)
    pop_1994 = models.BigIntegerField(blank=True, null=True)
    pop_grw_rt = models.FloatField(blank=True, null=True)
    pop_male = models.BigIntegerField(blank=True, null=True)
    pop_fem = models.BigIntegerField(blank=True, null=True)
    pop_0_14 = models.BigIntegerField(blank=True, null=True)
    pop_15_64 = models.BigIntegerField(blank=True, null=True)
    pop_65plus = models.BigIntegerField(blank=True, null=True)
    male_0_14 = models.BigIntegerField(blank=True, null=True)
    male_15_64 = models.BigIntegerField(blank=True, null=True)
    number_65plus = models.BigIntegerField(db_column='65plus', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    fem_0_14 = models.BigIntegerField(blank=True, null=True)
    fem_15_64 = models.BigIntegerField(blank=True, null=True)
    fem_65plus = models.BigIntegerField(blank=True, null=True)
    pop_urban = models.BigIntegerField(blank=True, null=True)
    pop_rural = models.BigIntegerField(blank=True, null=True)
    urb_male = models.BigIntegerField(blank=True, null=True)
    urb_fem = models.BigIntegerField(blank=True, null=True)
    rur_male = models.BigIntegerField(blank=True, null=True)
    rur_fem = models.BigIntegerField(blank=True, null=True)
    arable_pct = models.FloatField(blank=True, null=True)
    literacy = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rate0 = models.FloatField(blank=True, null=True)
    growth = models.FloatField(blank=True, null=True)
    colorcode = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'world_font_point'


class WorldPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=20, blank=True, null=True)
    continent = models.CharField(max_length=30, blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    fips = models.CharField(max_length=2, blank=True, null=True)
    iso_2 = models.CharField(max_length=2, blank=True, null=True)
    iso_3 = models.CharField(max_length=3, blank=True, null=True)
    pop_1994 = models.BigIntegerField(blank=True, null=True)
    pop_grw_rt = models.FloatField(blank=True, null=True)
    pop_male = models.BigIntegerField(blank=True, null=True)
    pop_fem = models.BigIntegerField(blank=True, null=True)
    pop_0_14 = models.BigIntegerField(blank=True, null=True)
    pop_15_64 = models.BigIntegerField(blank=True, null=True)
    pop_65plus = models.BigIntegerField(blank=True, null=True)
    male_0_14 = models.BigIntegerField(blank=True, null=True)
    male_15_64 = models.BigIntegerField(blank=True, null=True)
    number_65plus = models.BigIntegerField(db_column='65plus', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    fem_0_14 = models.BigIntegerField(blank=True, null=True)
    fem_15_64 = models.BigIntegerField(blank=True, null=True)
    fem_65plus = models.BigIntegerField(blank=True, null=True)
    pop_urban = models.BigIntegerField(blank=True, null=True)
    pop_rural = models.BigIntegerField(blank=True, null=True)
    urb_male = models.BigIntegerField(blank=True, null=True)
    urb_fem = models.BigIntegerField(blank=True, null=True)
    rur_male = models.BigIntegerField(blank=True, null=True)
    rur_fem = models.BigIntegerField(blank=True, null=True)
    arable_pct = models.FloatField(blank=True, null=True)
    literacy = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rate0 = models.FloatField(blank=True, null=True)
    growth = models.FloatField(blank=True, null=True)
    colorcode = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'world_polyline'


class WorldRegion(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=20, blank=True, null=True)
    continent = models.CharField(max_length=30, blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    fips = models.CharField(max_length=2, blank=True, null=True)
    iso_2 = models.CharField(max_length=2, blank=True, null=True)
    iso_3 = models.CharField(max_length=3, blank=True, null=True)
    pop_1994 = models.BigIntegerField(blank=True, null=True)
    pop_grw_rt = models.FloatField(blank=True, null=True)
    pop_male = models.BigIntegerField(blank=True, null=True)
    pop_fem = models.BigIntegerField(blank=True, null=True)
    pop_0_14 = models.BigIntegerField(blank=True, null=True)
    pop_15_64 = models.BigIntegerField(blank=True, null=True)
    pop_65plus = models.BigIntegerField(blank=True, null=True)
    male_0_14 = models.BigIntegerField(blank=True, null=True)
    male_15_64 = models.BigIntegerField(blank=True, null=True)
    number_65plus = models.BigIntegerField(db_column='65plus', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    fem_0_14 = models.BigIntegerField(blank=True, null=True)
    fem_15_64 = models.BigIntegerField(blank=True, null=True)
    fem_65plus = models.BigIntegerField(blank=True, null=True)
    pop_urban = models.BigIntegerField(blank=True, null=True)
    pop_rural = models.BigIntegerField(blank=True, null=True)
    urb_male = models.BigIntegerField(blank=True, null=True)
    urb_fem = models.BigIntegerField(blank=True, null=True)
    rur_male = models.BigIntegerField(blank=True, null=True)
    rur_fem = models.BigIntegerField(blank=True, null=True)
    arable_pct = models.FloatField(blank=True, null=True)
    literacy = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rate0 = models.FloatField(blank=True, null=True)
    growth = models.FloatField(blank=True, null=True)
    colorcode = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'world_region'


class Z1C121CPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    zone1 = models.CharField(max_length=10, blank=True, null=True)
    number_2_1_c = models.CharField(db_column='2_1_c', max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        db_table = 'z1_c_1_2_1_c_polyline'


class Z1C122CPoint(models.Model):
    geom = models.PointField(blank=True, null=True)
    zone = models.CharField(max_length=10, blank=True, null=True)
    circuit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'z1_c_1_2_2_c_point'


class Z1C122CPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    zone = models.CharField(max_length=10, blank=True, null=True)
    circuit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'z1_c_1_2_2_c_polyline'


class Z1C131CPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    zone = models.CharField(max_length=10, blank=True, null=True)
    circuit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'z1_c_1_3_1_c_polyline'


class Z1C132CPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    zone = models.CharField(max_length=10, blank=True, null=True)
    circuit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'z1_c_1_3_2_c_polyline'


class Z1C133CPolyline(models.Model):
    geom = models.MultiLineStringField(blank=True, null=True)
    zone = models.CharField(max_length=10, blank=True, null=True)
    circuit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'z1_c_1_3_3_c_polyline'


class ZoneAdressageRegion(models.Model):
    geom = models.MultiPolygonField(srid=32632, blank=True, null=True)
    nom_zone = models.CharField(max_length=20, blank=True, null=True)
    super = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    class Meta:
        db_table = 'zone_adressage_region'


class ZonesProscritesEllipse(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    zone = models.CharField(max_length=10, blank=True, null=True)
    itineraire = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'zones_proscrites_ellipse'
