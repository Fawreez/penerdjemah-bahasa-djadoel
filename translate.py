import argparse

def new_to_old(sentence):
    result = []
    sentence = sentence.lower()

    for i in range(len(sentence)):
        
        if sentence[i] == "j":
            result.append("dj")
        elif sentence[i] == "u":
            result.append("oe")
        elif sentence[i] == "c":
            result.append("tj")
        elif sentence[i] == "n" and i+1 < len(sentence):
            if sentence[i+1] == "y":
                result.append("nj")
            else:
                result.append(sentence[i])
        elif sentence[i] == "s" and i+1 < len(sentence):
            if sentence[i+1] == "y":
                result.append("sj")
            else:
                result.append(sentence[i])
        elif sentence[i] == "y" and (sentence[i-1] == "n" or sentence[i-1] == "s") and i-1 >= 0:
            result.append("")
        elif sentence[i] == "y":
            result.append("j")
        elif sentence[i] == "k" and i+1 < len(sentence):
            if  sentence[i+1] == "h":
                result.append("ch")
            else:
                result.append(sentence[i])
        elif sentence[i] == "h" and sentence[i-1] == "k" and i-1 >= 0:
            result.append("")
        else:
            result.append(sentence[i])
    
    return "".join(w for w in result)


def __command_line_wrapper():
    parser = argparse.ArgumentParser(description='Menerjemahkan kalimat dari ejaan modern ke ejaan lama')
    parser.add_argument('kalimat', type=str, metavar='kalimat', help='Kalimat yang ingin anda terjemahkan')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='Mencetak dengan ringkas')
    group.add_argument('-v', '--verbose', action='store_true', help='Mencetak dengan lengkap')
    args = parser.parse_args()

    sentence = args.kalimat
    new_sentence = new_to_old(sentence)
    
    if args.quiet:
        print(new_sentence)
    elif args.verbose:
        print(f"Kalimat setelah diterjemahkan: {new_sentence}")
    else:
        print(f"Hasil terjemah: {new_sentence}")


if __name__ == "__main__":
    __command_line_wrapper()
