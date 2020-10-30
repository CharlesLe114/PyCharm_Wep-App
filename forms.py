from django import forms

from rango.models import Product


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Your title"
                                }
                                )
                            )
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Your descriptions",
                                          "class": "new-class-name two",
                                          "id": "my-id-for-textarea",
                                          "rows": 20,
                                          "column": 20
                                      }
                                  )
                                  )
    price = forms.DecimalField(initial=199.99)
