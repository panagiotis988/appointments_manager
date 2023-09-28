import re
import phonenumbers


class ValidateUpdateCustomerForm:

    def validate_string_input(self, value):
        if value.isalpha():
            return True
        else:
            return False

    def validate_mobile(self, value):
        try:
            phone_number = phonenumbers.parse(value, 'GR')
            if phonenumbers.is_valid_number(phone_number):
                return True
            else:
                return False
        except phonenumbers.NumberParseException:
            return False

    def validate_email(self, value):
        if re.match(r"[^@α-ζΑ-Ζ]+@[^@α-ζΑ-Ζ]+\.[^@α-ζΑ-Ζ]+", value) or value == '':
            return True
        else:
            return False

    def validate_form(self, fname, lname, mobile, city, email):
        if not self.validate_string_input(fname):
            return {'status': False, 'error_field': 'firstname'}

        if not self.validate_string_input(lname):
            return {'status': False, 'error_field': 'lastname'}

        if not self.validate_mobile(mobile):
            return {'status': False, 'error_field': 'mobile'}

        if not self.validate_string_input(city):
            return {'status': False, 'error_field': 'city'}

        if not self.validate_email(email):
            return {'status': False, 'error_field': 'email'}

        return {'status': True, 'error_field': ''}
