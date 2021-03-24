import os
import re
import shutil

myreg = re.compile(r'((?<=((S|s)01(E|e)))0?\d\d?)|((?<=(1x))0?\d\d?)')
folreg = re.compile(r'E0?\d\d?')

# episode names of The Morning Show S1
ep = ["In The Dark Night of the Soul It's Always 3:30 in the Morning", "A Seat at the Table", "Chaos is the New Cocaine", "That Woman",
      "No One's Gonna Harm You, Not While I'm Around", "The Pendulum Swings", "Open Waters", "Lonely at the Top", "Play the Queen", "The Interview"]

for folder, sub, files in os.walk('.'):
    for f in files:

        # if it's the program file
        if(f == 'Sitcoms.py'):
            continue

        extension = f[len(f)-3:len(f)]
        number = myreg.search(f).group()
        i = int(number)
        repstr = os.path.join(
            os.getcwd(), f'TMSS01E{number} - {ep[i-1]}.{extension}')
        srcstr = os.path.join(os.getcwd(), f)
        os.rename(srcstr, repstr)
