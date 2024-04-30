# Generated by Django 4.2.11 on 2024-04-27 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avancement',
            fields=[
                ('etat_avancement', models.CharField(max_length=200, null=True)),
                ('idavancement', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('Domaine_dactivite', models.CharField(max_length=200, null=True)),
                ('iddomaine_dactivite', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Chef_de_Projet',
            fields=[
                ('Chef_de_Projet_name', models.CharField(max_length=200, null=True)),
                ('Chef_de_Projet_Prenom', models.CharField(max_length=200)),
                ('Chef_de_Projet_mail', models.CharField(max_length=200)),
                ('Chef_de_Projet_mot_de_passe', models.CharField(max_length=200)),
                ('idChef_de_Projet', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('Nom_Client', models.CharField(max_length=200, null=True)),
                ('Adresse', models.CharField(max_length=200)),
                ('idClient', models.AutoField(primary_key=True, serialize=False)),
                ('Domaine_dactivite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Cycle_de_devellopement',
            fields=[
                ('type', models.CharField(max_length=200, null=True)),
                ('Date_debut', models.CharField(max_length=200)),
                ('Date_Fin', models.CharField(max_length=200)),
                ('Priorite', models.CharField(max_length=200)),
                ('idphase', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe_de_Projet',
            fields=[
                ('Nom_Employe', models.CharField(max_length=200, null=True)),
                ('Services', models.CharField(max_length=200)),
                ('idProjet', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Equipements',
            fields=[
                ('Nom_Equipement', models.CharField(max_length=200, null=True)),
                ('type_Equipement', models.CharField(max_length=200)),
                ('statut_Equipement', models.CharField(max_length=200)),
                ('Numero_Equipement', models.CharField(max_length=200, null=True)),
                ('idequipement', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Famille_de_Projet',
            fields=[
                ('Nom_Famille', models.CharField(max_length=200, null=True)),
                ('idFamille', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Livrable',
            fields=[
                ('nom_livrable', models.CharField(max_length=200, null=True)),
                ('Ref_livrable', models.CharField(max_length=200, null=True)),
                ('Type', models.CharField(max_length=200, null=True)),
                ('idlivrable', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ModelProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('nom', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200)),
                ('Date_debut', models.DateTimeField(null=True)),
                ('Date_fin', models.DateTimeField(null=True)),
                ('id_projet', models.AutoField(primary_key=True, serialize=False)),
                ('chef_de_projet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.chef_de_projet')),
                ('famille_projet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.famille_de_projet')),
                ('nom_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.client')),
                ('type_process', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.process')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('Nom_Site', models.CharField(max_length=200, null=True)),
                ('idsite', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('date_achevement', models.DateTimeField(blank=True, null=True)),
                ('acheve', models.BooleanField(default=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.modelprocess')),
                ('projet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projet')),
            ],
        ),
        migrations.AddField(
            model_name='modelprocess',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='home.process'),
        ),
        migrations.AddField(
            model_name='modelprocess',
            name='projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projet'),
        ),
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('num_etape', models.CharField(max_length=200, null=True)),
                ('nom_etape', models.CharField(max_length=200, null=True)),
                ('Statut', models.CharField(max_length=200, null=True)),
                ('Commentaire', models.CharField(max_length=200, null=True)),
                ('idEtape', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cycle_de_devellopement')),
            ],
        ),
        migrations.AddField(
            model_name='cycle_de_devellopement',
            name='nom_livrable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.livrable'),
        ),
    ]