from django import forms
from kosanapp.apps.kelola.models import query_kosan

class KelolaForm(forms.ModelForm):
    class Meta:
        model = query_kosan
        fields = ("nama_kosan", "alamat_kosan", "fasilitas")


    def clean_nama_kosan(self):
        name = self.cleaned_data['nama_kosan']

        if self.instance and self.instance.nama_kosan == name:
            return name

        if query_kosan.objects.filter(nama_kosan=name).exists():
            raise forms.ValidationError("kosan dengan nama ini sudah ada")

        return name