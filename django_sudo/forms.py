"""
django_sudo.forms
~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django import forms
from django.utils.translation import ugettext_lazy as _


class SudoForm(forms.Form):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SudoForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        if not self.user.check_password(self.data['password']):
            raise forms.ValidationError(_('Incorrect password'))
        return self.data['password']
