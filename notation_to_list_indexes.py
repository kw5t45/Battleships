def convert_notation_to_index(notation):


    letter_xx = notation[0]
    number_yy = notation[1::]  # True

    chars = ["A","B","C","D","E","F","G","H","I","J"]

    x_axis = str(chars.index(letter_xx) + 1)

    return [number_yy, x_axis]