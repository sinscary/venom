import base64
import sys

class E:
    def encode(self,KeyToEncode):
        try:
            encoded_value = base64.b64encode(bytes((f'{KeyToEncode}'), 'utf-8'))
            return encoded_value.decode("utf-8")
        except Exception as err:
            print(f"Error occured while encoding: {err}")

if __name__ == '__main__':
    e = E()
    print(e.encode(sys.argv[1]))
