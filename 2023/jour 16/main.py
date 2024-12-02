# Exercice 1
data = open("2023/jour 16/input.txt", "r").read().split('\n')

seen = {(0, 0) : [(1, 0)]}
beams = [((0, 0), (1, 0))] # Position / Direction


while len(beams) > 0 :
    beam_pos, beam_dir = beams.pop()
    elem = data[beam_pos[1]][beam_pos[0]]

    # print(f"Nouveau cas avec {beam_pos} en direction de {beam_dir} sur un elem {elem}")
    
    if elem in '|.' and beam_dir[0] == 0 : # On va vers le haut ou vers le bas et aucun obstacle
        new_pos = (beam_pos[0], beam_pos[1] + beam_dir[1])
        if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
            if new_pos in seen and not beam_dir in seen[new_pos] :
                seen[new_pos].append(beam_dir)
                beams.append((new_pos, beam_dir))
            elif new_pos not in seen :
                seen[new_pos] = [beam_dir]
                beams.append((new_pos, beam_dir))

    elif elem in '-.' and beam_dir[1] == 0 : # On va vers la droite ou la gauche et aucun obstacle
        new_pos = (beam_pos[0] + beam_dir[0], beam_pos[1])
        if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
            if new_pos in seen and not beam_dir in seen[new_pos] :
                seen[new_pos].append(beam_dir)
                beams.append((new_pos, beam_dir))
            elif new_pos not in seen :
                seen[new_pos] = [beam_dir]
                beams.append((new_pos, beam_dir))

    elif elem in '|' and beam_dir[1] == 0 : # On va vers la droite ou la gauche et on rencontre un pipe
        for dir in [-1, 1] :
            new_pos = (beam_pos[0], beam_pos[1] + dir)
            new_beam_dir = (0, dir)
            if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
                if new_pos in seen and not new_beam_dir in seen[new_pos] :
                    seen[new_pos].append(new_beam_dir)
                    beams.append((new_pos, new_beam_dir))
                elif new_pos not in seen :
                    seen[new_pos] = [new_beam_dir]
                    beams.append((new_pos, new_beam_dir))

    elif elem in '-' and beam_dir[0] == 0 : # On va vers le haut ou le bas et on rencontre un pipe
        for dir in [-1, 1] :
            new_pos = (beam_pos[0] + dir, beam_pos[1])
            new_beam_dir = (dir, 0)
            if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
                if new_pos in seen and not new_beam_dir in seen[new_pos] :
                    seen[new_pos].append(new_beam_dir)
                    beams.append((new_pos, new_beam_dir))
                elif new_pos not in seen :
                    seen[new_pos] = [new_beam_dir]
                    beams.append((new_pos, new_beam_dir))
    
    elif elem in '\\/' : # On rencontre un mirroir
        if elem == '\\' :
            new_dir = (beam_dir[1], beam_dir[0])
        elif elem == '/' :
            new_dir = (beam_dir[1] * -1, beam_dir[0] * -1)
        else :
            print(f"problème avec {elem}")
        new_pos = (beam_pos[0] + new_dir[0], beam_pos[1] + new_dir[1])
        if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
            if new_pos in seen and not new_dir in seen[new_pos] :
                seen[new_pos].append(new_dir)
                beams.append((new_pos, new_dir))
            elif new_pos not in seen :
                seen[new_pos] = [new_dir]
                beams.append((new_pos, new_dir))

print(len(seen.keys()))


# Exercice 2
data = open("2023/jour 16/input.txt", "r").read().split('\n')

max = 0

h = [((x, 0), (0, 1)) for x in range(len(data[0]))] # Haut
b = [((x, len(data)-1), (0, -1)) for x in range(len(data[0]))] # Bas
d = [((len(data[0])-1, y), (-1, 0)) for y in range(len(data))] # Droite
g = [((0, y), (1, 0)) for y in range(len(data))] # Gauche

debuts = h + b + d + g
for deb in debuts :
    seen = {deb[0] : [deb[1]]}
    beams = [(deb[0], deb[1])] # Position / Direction

    while len(beams) > 0 :
        beam_pos, beam_dir = beams.pop()
        elem = data[beam_pos[1]][beam_pos[0]]

        # print(f"Nouveau cas avec {beam_pos} en direction de {beam_dir} sur un elem {elem}")
        
        if elem in '|.' and beam_dir[0] == 0 : # On va vers le haut ou vers le bas et aucun obstacle
            new_pos = (beam_pos[0], beam_pos[1] + beam_dir[1])
            if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
                if new_pos in seen and not beam_dir in seen[new_pos] :
                    seen[new_pos].append(beam_dir)
                    beams.append((new_pos, beam_dir))
                elif new_pos not in seen :
                    seen[new_pos] = [beam_dir]
                    beams.append((new_pos, beam_dir))

        elif elem in '-.' and beam_dir[1] == 0 : # On va vers la droite ou la gauche et aucun obstacle
            new_pos = (beam_pos[0] + beam_dir[0], beam_pos[1])
            if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
                if new_pos in seen and not beam_dir in seen[new_pos] :
                    seen[new_pos].append(beam_dir)
                    beams.append((new_pos, beam_dir))
                elif new_pos not in seen :
                    seen[new_pos] = [beam_dir]
                    beams.append((new_pos, beam_dir))

        elif elem in '|' and beam_dir[1] == 0 : # On va vers la droite ou la gauche et on rencontre un pipe
            for dir in [-1, 1] :
                new_pos = (beam_pos[0], beam_pos[1] + dir)
                new_beam_dir = (0, dir)
                if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
                    if new_pos in seen and not new_beam_dir in seen[new_pos] :
                        seen[new_pos].append(new_beam_dir)
                        beams.append((new_pos, new_beam_dir))
                    elif new_pos not in seen :
                        seen[new_pos] = [new_beam_dir]
                        beams.append((new_pos, new_beam_dir))

        elif elem in '-' and beam_dir[0] == 0 : # On va vers le haut ou le bas et on rencontre un pipe
            for dir in [-1, 1] :
                new_pos = (beam_pos[0] + dir, beam_pos[1])
                new_beam_dir = (dir, 0)
                if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
                    if new_pos in seen and not new_beam_dir in seen[new_pos] :
                        seen[new_pos].append(new_beam_dir)
                        beams.append((new_pos, new_beam_dir))
                    elif new_pos not in seen :
                        seen[new_pos] = [new_beam_dir]
                        beams.append((new_pos, new_beam_dir))
        
        elif elem in '\\/' : # On rencontre un mirroir
            if elem == '\\' :
                new_dir = (beam_dir[1], beam_dir[0])
            elif elem == '/' :
                new_dir = (beam_dir[1] * -1, beam_dir[0] * -1)
            else :
                print(f"problème avec {elem}")
            new_pos = (beam_pos[0] + new_dir[0], beam_pos[1] + new_dir[1])
            if new_pos[0] >= 0 and new_pos[0] < len(data[0]) and new_pos[1] >= 0 and new_pos[1] < len(data) :
                if new_pos in seen and not new_dir in seen[new_pos] :
                    seen[new_pos].append(new_dir)
                    beams.append((new_pos, new_dir))
                elif new_pos not in seen :
                    seen[new_pos] = [new_dir]
                    beams.append((new_pos, new_dir))

    score = len(seen.keys())
    if score > max :
        max = score

print(max)
