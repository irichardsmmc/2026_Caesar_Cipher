from datetime import date

def string_check(question, valid_ans_list):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    result = ''

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:1]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


un_encrypted_messages = ['Hello', 'Creative Message']
encrypted_messages = ['Zwddg', 'Fuhdwlyh Phvvdjh']
un_decrypted_messages = ['Aopz pz h tlzzhnl', 'Gybnc kxn cdepp']
decrypted_messages_lists = ['Znoy oy g skyygmk, Ymnx nx f rjxxflj, Xlmw mw e qiwweki, Wklv lv d phvvdjh, Vjku ku c oguucig, Uijt jt b nfttbhf, This is a message, Sghr hr z ldrrzfd, Rfgq gq y kcqqyec, Qefp fp x jbppxdb, Pdeo eo w iaoowca, Ocdn dn v hznnvbz, Nbcm cm u gymmuay, Mabl bl t fxlltzx, Lzak ak s ewkksyw, Kyzj zj r dvjjrxv, Jxyi yi q cuiiqwu, Iwxh xh p bthhpvt, Hvwg wg o asggous, Guvf vf n zrffntr, Ftue ue m yqeemsq, Estd td l xpddlrp, Drsc sc k wocckqo, Cqrb rb j vnbbjpn, Bpqa qa i umaaiom', 'Fxamb jwm bcdoo, Ewzla ivl abcnn, Dvykz huk zabmm, Cuxjy gtj yzall, Btwix fsi xyzkk, Asvhw erh wxyjj, Zrugv dqg vwxii, Yqtfu cpf uvwhh, Xpset boe tuvgg, Words and stuff, Vnqcr zmc rstee, Umpbq ylb qrsdd, Tloap xka pqrcc, Sknzo wjz opqbb, Rjmyn viy nopaa, Qilxm uhx mnozz, Phkwl tgw lmnyy, Ogjvk sfv klmxx, Nfiuj reu jklww, Mehti qdt ijkvv, Ldgsh pcs hijuu, Kcfrg obr ghitt, Jbeqf naq fghss, Iadpe mzp efgrr, Hzcod lyo defqq']

encrypt_heading = "---Encrypted Messages---"
decrypt_heading = "---Decrypted Messages---"
encrypt_data = ""
decrypt_data = ""

# Show history (if avaliable)
if len(un_encrypted_messages) > 0:

    # Encrypted Messages Heading
    # print(encrypt_heading)

    # Print each unencrypted message with its encrypted version
    for item in un_encrypted_messages:
        index = un_encrypted_messages.index(item)
        # print(f'{item} --> {encrypted_messages[index]}\n')
        encrypt_data += f'{item} --> {encrypted_messages[index]}\n'

if len(un_decrypted_messages) > 0:

    # Decrypted Messages Heading
    # print(decrypt_heading)

    # Print each undecrypted message with all of its possible solutions
    for item in un_decrypted_messages:
        index = un_decrypted_messages.index(item)
        # print(f'{item}: \n - {decrypted_messages_lists[index]}\n')
        decrypt_data += f'{item}: \n - {decrypted_messages_lists[index]}\n'

# Ask user if they want to write data to file
save_query = string_check('Would you like to save your data to a file? ', ['yes', 'no'])

if save_query == 'yes':

    file_name = input("File Name: ")
    write_to = "{}.txt".format(file_name)

    text_file = open(write_to, "w+")

    date = date.today()
    heading = f"=== Caesar Cipher Data ({date}) ===\n"

    # list of strings
    to_write = [heading, encrypt_heading, encrypt_data, decrypt_heading, decrypt_data]

    # print the output
    for item in to_write:
        print(item)

    # write item to file
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

