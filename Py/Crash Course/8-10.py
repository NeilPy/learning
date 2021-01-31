def make_great(magicians, complet_magicians):
    while magicians:
        current_magicians = magicians.pop()
        complet_magicians.append('Great ' + current_magicians)


def show_magicians(complet_magicians):
    for complet_magician in complet_magicians:
        print(complet_magician)


magicians = ['Joe', 'Sem', 'Reak', 'Mike']
complet_magicians = []
make_great(magicians, complet_magicians)
show_magicians(complet_magicians)

