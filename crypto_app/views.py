from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def crypt_encode_decode(data, key):
    data_to_encode = bytearray(data)
    key_to_encode = bytearray(key)
    encoded_data = bytearray(len(data_to_encode))

    for i in range(len(data_to_encode)):
        encoded_data[i] = data_to_encode[i] ^ key_to_encode[i % len(key)]

    return str(encoded_data)

def string_to_hex(string_value):
    hex_buffer = ""
    for i in string_value:
        hex_buffer = hex_buffer + i.encode('hex') + ':'
    return hex_buffer.rstrip(':')

def hex_to_string(hex_value):
    hex_value_str = str(hex_value).replace(':', '')
    result = bytearray.fromhex(hex_value_str)
    return str(result)


# Create your views here.
class HomeView(View):
    def get(self, request):
        decoded_data = request.session.get('decoded_data', "")
        encoded_data = request.session.get('encoded_data', "")
        key = request.session.get('key_to_encode', "")
        request.session.clear()
        return render(request, 'index.html',
                       {"decoded_data": decoded_data,
                        "encoded_data": encoded_data,
                        "key": key}
                      )

    def post(self, request):
        data = request.POST.get('data', False)
        key = request.POST.get('key', False)
        encoded_data = request.POST.get('encoded_data', False)

        request.session['key_to_encode'] = str(key)

        #To encode
        if data and key:
            data_to_encode = str(data)
            encoded_data_buffer = crypt_encode_decode(data_to_encode, str(key))
            hex_encoded_data = string_to_hex(encoded_data_buffer)
            request.session['encoded_data'] = hex_encoded_data
            return HttpResponseRedirect(reverse('home'))

        #To decode
        if encoded_data and key:
            encoded_data_str = hex_to_string(str(encoded_data))
            decoded_data_buffer = crypt_encode_decode(encoded_data_str, str(key))
            request.session['decoded_data'] = decoded_data_buffer
            return HttpResponseRedirect(reverse('home'))
