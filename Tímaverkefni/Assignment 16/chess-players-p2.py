def get_filename_from_user():
    filename = input("Enter filename: ")
    return filename

def create_key(name):
    last, first = name.split(",")
    fullname = "{} {}".format(first.strip(),last.strip())
    return fullname

def process_value_data(chess_player_data):
    rank = int(chess_player_data[0])
    country = chess_player_data[2].strip()
    points = int(chess_player_data[3])
    birth_year = int(chess_player_data[4])
    return [rank,country,points,birth_year]

def create_country_dict(chess_player_dict):
    country_dict = {}
    for key, value in chess_player_dict.items():
        country = value[1]
        if country in country_dict:
            country_dict[country].append(key)
        else:
            country_dict[country] = [key]
    return country_dict

def create_birth_year_dict(chess_player_dict):
    birth_year_dict = {}
    for key, value in chess_player_dict.items():
        birth_year = value[3]
        if birth_year in birth_year_dict:
            birth_year_dict[birth_year].append(key)
        else:
            birth_year_dict[birth_year] = [key]
    return birth_year_dict

def get_data_from_file(filename):
    chess_player_dict = {}
    try:
        with open(filename) as file_content:
            for line in file_content:
                line = line.split(";")
                key = create_key(line[1])
                value = process_value_data(line)
                chess_player_dict[key] = value
    except FileNotFoundError:
        pass
    return chess_player_dict

def get_average_for_country(names,player_dict):
    sum = 0
    for player in names:
        sum += player_dict[player][2]
    return sum/len(names)

def get_average_for_birth_year(names,player_dict):
    sum = 0
    for player in names:
        sum += player_dict[player][2]
    return sum/len(names)

def print_header(header_text):
    print(header_text)
    print("-"*len(header_text))

def print_result(chess_player_dict,country_dict,birth_year_dict):
    print_header("Players by country:")
    for key, value in sorted(country_dict.items()):
        average = get_average_for_country(value,chess_player_dict)
        print("{} ({}) ({:.1f}):".format(key,len(value),average))
        for name in value:
            print("{:>40}{:>10d}".format(name, chess_player_dict[name][2]))
    print_header("Players by birth year:")
    for key, value in sorted(birth_year_dict.items()):
        average = get_average_for_birth_year(value,chess_player_dict)
        print("{} ({}) ({:.1f}):".format(key,len(value),average))
        for name in value:
            print("{:>40}{:>10d}".format(name, chess_player_dict[name][2]))

def main():
    file_name = get_filename_from_user()
    chess_player_dict = get_data_from_file(file_name)
    country_dict = create_country_dict(chess_player_dict)
    birth_year_dict = create_birth_year_dict(chess_player_dict)
    print_result(chess_player_dict,country_dict,birth_year_dict)

main()