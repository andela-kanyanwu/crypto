from django.shortcuts import render
from django.views.generic import View


def crypt_encode(data, key):
    data_to_encode = bytearray(data)
    key_to_encode = bytearray(key)
    encoded_data = bytearray(len(data_to_encode))

    for i in range(len(data_to_encode)):
        encoded_data[i] = data_to_encode[i] ^ key_to_encode[i%len(key)]

    return str(encoded_data)

def hex_to_bytearray(hex_value):
    hex_value_array = str(hex_value).split(':')
    result = bytearray(len(hex_value_array))

    for hex_num in hex_value_array:
        pass


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        data = request.POST.get('data', False)
        key = request.POST.get('key', False)
        encoded_data = request.POST.get('encoded_data', False)

        #To encode
        if data and key:
            data_to_encode = str(data)
            key_to_encode = str(key)
            encoded_data_buffer = crypt_encode(data_to_encode, key_to_encode)
            hex_encoded_data = ""

            for i in encoded_data_buffer:
                hex_encoded_data =  hex_encoded_data + i.encode('hex') + ':'

            hex_encoded_data = hex_encoded_data.rstrip(':')    
            print hex_encoded_data
            # return render hex_encoded_data on the template

        #To decode
        if encoded_data and key:
            decoded_data_buffer = crypt_encode(encoded_data, key)
            
        