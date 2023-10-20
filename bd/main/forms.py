from django import forms
from django.utils.safestring import mark_safe


class RechercheForm(forms.Form):
    isbn = forms.CharField(required=False, label='ISBN', widget=forms.TextInput(attrs={'placeholder': 'ISBN'}))
    titre = forms.CharField(required=False, label='Titre', widget=forms.TextInput(attrs={'placeholder': 'Titre'}))
    numero = forms.CharField(required=False, label='Numéro',
                             widget=forms.TextInput(attrs={'placeholder': 'Numéro du tome'}))
    serie = forms.CharField(required=False, label='Série', widget=forms.TextInput(attrs={'placeholder': 'Série'}))
    scenariste = forms.CharField(required=False, label='Scénariste',
                                 widget=forms.TextInput(attrs={'placeholder': 'Scénariste'}))
    dessinateur = forms.CharField(required=False, label='Dessinateur',
                                  widget=forms.TextInput(attrs={'placeholder': 'Dessinateur'}))
    editeur = forms.CharField(required=False, label='Éditeur', widget=forms.TextInput(attrs={'placeholder': 'Éditeur'}))
    edition = forms.CharField(required=False, label='Édition', widget=forms.TextInput(attrs={'placeholder': 'Édition'}))
    annee = forms.CharField(required=False, label="Année d'achat",
                            widget=forms.TextInput(attrs={'placeholder': "Année d'achat"}))
    dedicace = forms.CharField(required=False, label='Dédicace',
                               widget=forms.TextInput(attrs={'placeholder': 'Dédicace'}))
    exlibris = forms.CharField(required=False, label='Ex Libris',
                               widget=forms.TextInput(attrs={'placeholder': 'Ex Libris'}))
    synopsis = forms.CharField(required=False, label='Synopsis',
                               widget=forms.TextInput(attrs={'placeholder': 'Synopsis'}))

    def as_custom_table_2(self):
        html = '\t<table>\n'
        html += '\t\t\t\t\t<tr>\n'
        i = 0
        for field in self:
            if i % 2 == 0 and i > 0:
                html += '\t\t\t\t\t</tr>\n'
                html += '\t\t\t\t\t<tr>\n'

            html += f'\t\t\t\t\t\t<td><label for="{field.id_for_label}">{field.label}&nbsp;:</label></td>\n'
            html += f'\t\t\t\t\t\t<td>{field}</td>\n'

            i += 1

        html += '\t\t\t\t\t</tr>\n'
        html += '\t\t\t\t</table>\n'

        return mark_safe(html)

    def as_custom_table_3(self):
        html = '\t<table>\n'
        html += '\t\t\t\t\t<tr>\n'
        i = 0
        for field in self:
            if i % 3 == 0 and i > 0:
                html += '\t\t\t\t\t</tr>\n'
                html += '\t\t\t\t\t<tr>\n'

            html += f'\t\t\t\t\t\t<td><label for="{field.id_for_label}">{field.label}&nbsp;:</label></td>\n'
            html += f'\t\t\t\t\t\t<td>{field}</td>\n'

            i += 1

        html += '\t\t\t\t\t</tr>\n'
        html += '\t\t\t\t</table>\n'

        return mark_safe(html)
