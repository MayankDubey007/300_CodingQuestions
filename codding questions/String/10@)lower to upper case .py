# from logging.config import stopListening


def L2U(st):
    st1=""
    for i in st:
        st1 += chr(ord(i)-32)
    print(st1)
    
def U2L(st):
    st1=""
    for i in st:
        st1 += chr(ord(i)+32)
    print(st1)
    
st1 = input("enter string to change into Upper Case : ")
L2U(st1)
st2 = input("enter string to change into Lowwer Case : ")
U2L(st2)
# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))