# Generated by Django 2.0.8 on 2018-08-15 00:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
from wagtail.migrations import AlterStreamField


class AlterStreamFieldB529A3A1(AlterStreamField):
    """
    This migration applies to these fields:
    - StreamModel.body

    Before state:
    ('wagtail.core.blocks.StreamBlock',
     [[('section', ('wagtail.core.blocks.RichTextBlock', ()))]])

    After state:
    ('wagtail.core.blocks.StreamBlock',
     [[('section',
        ('wagtail.core.blocks.StructBlock',
         [[('title', ('wagtail.core.blocks.CharBlock', ())),
           ('body', ('wagtail.core.blocks.RichTextBlock', ()))]]))]])

    Diff:
    ---
    +++
    @@ -1,2 +1,5 @@
     ('wagtail.core.blocks.StreamBlock',
    - [[('section', ('wagtail.core.blocks.RichTextBlock', ()))]])+ [[('section',
    +    ('wagtail.core.blocks.StructBlock',
    +     [[('title', ('wagtail.core.blocks.CharBlock', ())),
    +       ('body', ('wagtail.core.blocks.RichTextBlock', ()))]]))]])

    """

    def transform_values(self, values):
        """
        This method receives the list of values of the field in the old format
        and should return the list of values of the field in the new format

        [
            {
                'type': ...,
                'value': ...,
                'id': ...,
            },
            ...,
        ]
        """
        return [self.transform_value(value) for value in values]

    def transform_value(self, value):
        """
        This method receives each individual value of the field in the old
        format and should return a value in the new format

        {
            'type': ...,
            'value': ...,
            'id': ...,
        }
        """
        raise NotImplementedError('Please define the transform_value method of AlterStreamFieldB529A3A1')


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0001_initial'),
    ]

    operations = [
        AlterStreamFieldB529A3A1(
            model_name='streammodel',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock())]))]),
        ),
    ]
