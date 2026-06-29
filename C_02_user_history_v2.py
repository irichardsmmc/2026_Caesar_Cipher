un_encrypted_messages = ['Hello', 'Creative Message']
encrypted_messages = ['Zwddg', 'Fuhdwlyh Phvvdjh']
un_decrypted_messages = ['Aopz pz h tlzzhnl', 'Gybnc kxn cdepp']
decrypted_messages_lists = ['Znoy oy g skyygmk, Ymnx nx f rjxxflj, Xlmw mw e qiwweki, Wklv lv d phvvdjh, Vjku ku c oguucig, Uijt jt b nfttbhf, This is a message, Sghr hr z ldrrzfd, Rfgq gq y kcqqyec, Qefp fp x jbppxdb, Pdeo eo w iaoowca, Ocdn dn v hznnvbz, Nbcm cm u gymmuay, Mabl bl t fxlltzx, Lzak ak s ewkksyw, Kyzj zj r dvjjrxv, Jxyi yi q cuiiqwu, Iwxh xh p bthhpvt, Hvwg wg o asggous, Guvf vf n zrffntr, Ftue ue m yqeemsq, Estd td l xpddlrp, Drsc sc k wocckqo, Cqrb rb j vnbbjpn, Bpqa qa i umaaiom', 'Fxamb jwm bcdoo, Ewzla ivl abcnn, Dvykz huk zabmm, Cuxjy gtj yzall, Btwix fsi xyzkk, Asvhw erh wxyjj, Zrugv dqg vwxii, Yqtfu cpf uvwhh, Xpset boe tuvgg, Words and stuff, Vnqcr zmc rstee, Umpbq ylb qrsdd, Tloap xka pqrcc, Sknzo wjz opqbb, Rjmyn viy nopaa, Qilxm uhx mnozz, Phkwl tgw lmnyy, Ogjvk sfv klmxx, Nfiuj reu jklww, Mehti qdt ijkvv, Ldgsh pcs hijuu, Kcfrg obr ghitt, Jbeqf naq fghss, Iadpe mzp efgrr, Hzcod lyo defqq']

# Show history (if avaliable)
if len(un_encrypted_messages) > 0:

    print("---Encrypted Messages---\n")

    for item in un_encrypted_messages:
        index = un_encrypted_messages.index(item)
        print(f'{item} --> {encrypted_messages[index]}\n')

if len(un_decrypted_messages) > 0:
    print("---Decrypted Messages---\n")

    for item in un_decrypted_messages:
        index = un_decrypted_messages.index(item)
        print(f'{item}: \n\n{decrypted_messages_lists[index]}\n')
