from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .MelliCodeValidate import *
from .models import DemographicInfo


DEGREES = [
    ('دیپلم', 'دیپلم'),
    ('فوق دیپلم', 'فوق دیپلم'),
    ('لیسانس', 'لیسانس'),
    ('فوق لیسانس', 'فوق لیسانس'),
    ('دکترا', 'دکترا'),
    ('بی سواد', 'بی سواد')
]

error_msg = {
    'required': 'این فیلد الزامی است'
}

class DataForm(forms.Form):
    first_name = forms.CharField(
        label='نام:',
        validators=[
            RegexValidator(
                regex=regex_fa,
                message='فقط حروف فارسی مجاز است',
                code='invalid'
            )
        ],
        error_messages=error_msg
    )

    last_name = forms.CharField(
        label='نام خانوادگی:',
        validators=[
            RegexValidator(
                regex=regex_fa,
                message='فقط حروف فارسی مجاز است',
                code='invalid'
            )
        ],
        error_messages=error_msg
    )

    national_code = forms.CharField(
        label='کد ملی:',
        error_messages=error_msg
    )

    phone_number = forms.CharField(
        label='شماره تلفن:',
        validators=[
            RegexValidator(
                regex=regex_ir_phone,
                message='شماره تلفن معتبر نیست',
                code='invalid'
            )
        ],
        error_messages=error_msg
    )

    cell_number = forms.CharField(
        label='شماره موبایل:',
        validators=[
            RegexValidator(
                regex=regex_ir_cell,
                message='شماره موبایل معتبر نیست',
                code='invalid'
            )
        ],
        error_messages=error_msg
    )

    education_degree = forms.ChoiceField(label='مدرک تحصیلی:', choices=DEGREES)

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.use_required_attribute = False
        # no "required" html attributes on required fields,
        # because I want to show validation error rather than browser validation.
    
    def clean_national_code(self):
        value = self.cleaned_data['national_code']
        if not IrCodeValidator(value):
            raise ValidationError(_('کد ملی معتبر نیست'))

        # if self.edit == False:
        #     if DemographicInfo.objects.filter(national_code=value):
        #         raise ValidationError(_('رکوردی با این کد ملی  موجود است'))

        return value
