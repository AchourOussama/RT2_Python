def parler_enthousiasme(message,exclamation_mark=1,upperCase=False):
    if (upperCase):
        print(message.upper()+exclamation_mark*"!")
    else:
        print(message+exclamation_mark*"!")
message=input()
parler_enthousiasme(message,2,True)
