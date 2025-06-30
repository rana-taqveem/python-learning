def calculate_love_score(name1, name2):
    name1_chars = list(name1.lower())
    name2_chars = list(name2.lower())
    
    
    name1_of_true_Ts, name1_of_true_Rs, name1_of_true_Us, name1_of_true_Es = count_true_chars(name1_chars)
    name2_of_true_Ts, name2_of_true_Rs, name2_of_true_Us, name2_of_true_Es = count_true_chars(name2_chars)

    num_of_true_Ts = name1_of_true_Ts + name2_of_true_Ts
    num_of_true_Rs = name1_of_true_Rs + name2_of_true_Rs
    num_of_true_Us = name1_of_true_Us + name2_of_true_Us
    num_of_true_Es = name1_of_true_Es + name2_of_true_Es

    name1_of_love_Ts, name1_of_love_Rs, name1_of_love_Us, name1_of_love_Es = count_love_chars(name1_chars)
    name2_of_love_Ts, name2_of_love_Rs, name2_of_love_Us, name2_of_love_Es = count_love_chars(name2_chars)

    num_of_love_Ts = name1_of_love_Ts + name2_of_love_Ts
    num_of_love_Rs = name1_of_love_Rs + name2_of_love_Rs
    num_of_love_Us = name1_of_love_Us + name2_of_love_Us
    num_of_love_Es = name1_of_love_Es + name2_of_love_Es

    t_total = num_of_true_Ts+ num_of_true_Rs + num_of_true_Us + num_of_true_Es
    l_total = num_of_love_Ts+ num_of_love_Rs + num_of_love_Us + num_of_love_Es
    

    print(f'{t_total}{l_total}')
    
    
            

def count_true_chars(nameChars):

    num_of_Ts = 0
    num_of_Rs = 0
    num_of_Us = 0
    num_of_Es = 0

    for char in nameChars:
        if char == 't':
            num_of_Ts = num_of_Ts + 1
        elif char == 'r':
            num_of_Rs = num_of_Rs + 1
        elif char == 'u':
            num_of_Us = num_of_Us + 1
        elif char == 'e':
            num_of_Es = num_of_Es + 1

    return num_of_Ts, num_of_Rs, num_of_Us, num_of_Es


def count_love_chars(nameChars):

    num_of_Ls = 0
    num_of_Os = 0
    num_of_Vs = 0
    num_of_Es = 0

    for char in nameChars:
        if char == 'l':
            num_of_Ls = num_of_Ls + 1
        elif char == 'o':
            num_of_Os = num_of_Os + 1
        elif char == 'v':
            num_of_Vs = num_of_Vs + 1
        elif char == 'e':
            num_of_Es = num_of_Es + 1

    return num_of_Ls, num_of_Os, num_of_Vs, num_of_Es
            

calculate_love_score("Angela Yu", "Jack Bauer")