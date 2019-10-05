from unbabel.models import Translation


def test_repr():
    translation = Translation(
        source_language="en",
        status="new",
        target_language="es",
        text="Test",
        text_format="text",
        translated_text="Test",
        uid=123
    )

    assert str(translation) == (
        '<Translation uid="123" status="new" text="Test" '
        'translated_text="Test">')
