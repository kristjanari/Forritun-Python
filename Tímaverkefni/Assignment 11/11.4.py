
# Main program starts here - DO NOT change it
def get_emails():
    email = ""
    listi = []
    while True:
        email = input("Email address: ")
        if email.lower() == "q":
            break
        listi.append(email)
    return listi

def get_names_and_domains(listi):
    túpla = [tuple(i.split("@")) for i in listi]
    return túpla


email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)