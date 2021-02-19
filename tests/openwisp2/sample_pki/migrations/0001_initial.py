# Generated by Django 3.0.6 on 2020-05-10 18:14

import collections

import django.db.models.deletion
import django.utils.timezone
import django_x509.base.models
import jsonfield.fields
import model_utils.fields
import swapper
from django.db import migrations, models

import openwisp_users.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        swapper.dependency('openwisp_users', 'Organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ca',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=64)),
                ('notes', models.TextField(blank=True)),
                (
                    'key_length',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('', ''),
                            ('512', '512'),
                            ('1024', '1024'),
                            ('2048', '2048'),
                            ('4096', '4096'),
                        ],
                        default=django_x509.base.models.default_key_length,
                        help_text='bits',
                        max_length=6,
                        verbose_name='key length',
                    ),
                ),
                (
                    'digest',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('', ''),
                            ('sha1', 'SHA1'),
                            ('sha224', 'SHA224'),
                            ('sha256', 'SHA256'),
                            ('sha384', 'SHA384'),
                            ('sha512', 'SHA512'),
                        ],
                        default=django_x509.base.models.default_digest_algorithm,
                        help_text='bits',
                        max_length=8,
                        verbose_name='digest algorithm',
                    ),
                ),
                (
                    'validity_start',
                    models.DateTimeField(
                        blank=True,
                        default=django_x509.base.models.default_validity_start,
                        null=True,
                    ),
                ),
                (
                    'validity_end',
                    models.DateTimeField(
                        blank=True,
                        default=django_x509.base.models.default_ca_validity_end,
                        null=True,
                    ),
                ),
                ('country_code', models.CharField(blank=True, max_length=2)),
                (
                    'state',
                    models.CharField(
                        blank=True, max_length=64, verbose_name='state or province'
                    ),
                ),
                (
                    'city',
                    models.CharField(blank=True, max_length=64, verbose_name='city'),
                ),
                (
                    'organization_name',
                    models.CharField(
                        blank=True, max_length=64, verbose_name='organization'
                    ),
                ),
                (
                    'organizational_unit_name',
                    models.CharField(
                        blank=True,
                        max_length=64,
                        verbose_name='organizational unit name',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        blank=True, max_length=254, verbose_name='email address'
                    ),
                ),
                (
                    'common_name',
                    models.CharField(
                        blank=True, max_length=64, verbose_name='common name'
                    ),
                ),
                (
                    'extensions',
                    jsonfield.fields.JSONField(
                        blank=True,
                        default=list,
                        dump_kwargs={'indent': 4},
                        help_text='additional x509 certificate extensions',
                        load_kwargs={'object_pairs_hook': collections.OrderedDict},
                        verbose_name='extensions',
                    ),
                ),
                (
                    'serial_number',
                    models.CharField(
                        blank=True,
                        help_text='leave blank to determine automatically',
                        max_length=48,
                        null=True,
                        verbose_name='serial number',
                    ),
                ),
                (
                    'certificate',
                    models.TextField(
                        blank=True, help_text='certificate in X.509 PEM format'
                    ),
                ),
                (
                    'private_key',
                    models.TextField(
                        blank=True, help_text='private key in X.509 PEM format'
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'passphrase',
                    models.CharField(
                        blank=True,
                        help_text='Passphrase for the private key, if present',
                        max_length=64,
                    ),
                ),
                ('details', models.CharField(blank=True, max_length=64, null=True)),
                (
                    'organization',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('openwisp_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
            ],
            options={
                'verbose_name': 'CA',
                'verbose_name_plural': 'CAs',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Cert',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=64)),
                ('notes', models.TextField(blank=True)),
                (
                    'key_length',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('', ''),
                            ('512', '512'),
                            ('1024', '1024'),
                            ('2048', '2048'),
                            ('4096', '4096'),
                        ],
                        default=django_x509.base.models.default_key_length,
                        help_text='bits',
                        max_length=6,
                        verbose_name='key length',
                    ),
                ),
                (
                    'digest',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('', ''),
                            ('sha1', 'SHA1'),
                            ('sha224', 'SHA224'),
                            ('sha256', 'SHA256'),
                            ('sha384', 'SHA384'),
                            ('sha512', 'SHA512'),
                        ],
                        default=django_x509.base.models.default_digest_algorithm,
                        help_text='bits',
                        max_length=8,
                        verbose_name='digest algorithm',
                    ),
                ),
                (
                    'validity_start',
                    models.DateTimeField(
                        blank=True,
                        default=django_x509.base.models.default_validity_start,
                        null=True,
                    ),
                ),
                (
                    'validity_end',
                    models.DateTimeField(
                        blank=True,
                        default=django_x509.base.models.default_cert_validity_end,
                        null=True,
                    ),
                ),
                ('country_code', models.CharField(blank=True, max_length=2)),
                (
                    'state',
                    models.CharField(
                        blank=True, max_length=64, verbose_name='state or province'
                    ),
                ),
                (
                    'city',
                    models.CharField(blank=True, max_length=64, verbose_name='city'),
                ),
                (
                    'organization_name',
                    models.CharField(
                        blank=True, max_length=64, verbose_name='organization'
                    ),
                ),
                (
                    'organizational_unit_name',
                    models.CharField(
                        blank=True,
                        max_length=64,
                        verbose_name='organizational unit name',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        blank=True, max_length=254, verbose_name='email address'
                    ),
                ),
                (
                    'common_name',
                    models.CharField(
                        blank=True, max_length=64, verbose_name='common name'
                    ),
                ),
                (
                    'extensions',
                    jsonfield.fields.JSONField(
                        blank=True,
                        default=list,
                        dump_kwargs={'indent': 4},
                        help_text='additional x509 certificate extensions',
                        load_kwargs={'object_pairs_hook': collections.OrderedDict},
                        verbose_name='extensions',
                    ),
                ),
                (
                    'serial_number',
                    models.CharField(
                        blank=True,
                        help_text='leave blank to determine automatically',
                        max_length=48,
                        null=True,
                        verbose_name='serial number',
                    ),
                ),
                (
                    'certificate',
                    models.TextField(
                        blank=True, help_text='certificate in X.509 PEM format'
                    ),
                ),
                (
                    'private_key',
                    models.TextField(
                        blank=True, help_text='private key in X.509 PEM format'
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'passphrase',
                    models.CharField(
                        blank=True,
                        help_text='Passphrase for the private key, if present',
                        max_length=64,
                    ),
                ),
                ('revoked', models.BooleanField(default=False, verbose_name='revoked')),
                (
                    'revoked_at',
                    models.DateTimeField(
                        blank=True, default=None, null=True, verbose_name='revoked at'
                    ),
                ),
                ('details', models.CharField(blank=True, max_length=64, null=True)),
                (
                    'ca',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='sample_pki.Ca',
                        verbose_name='CA',
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('openwisp_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
            ],
            options={
                'verbose_name': 'certificate',
                'verbose_name_plural': 'certificates',
                'abstract': False,
                'unique_together': {('ca', 'serial_number')},
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
    ]
