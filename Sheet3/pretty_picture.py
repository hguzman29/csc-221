from gasp import *

begin_graphics()

Circle((300, 200), 100)
Circle((260, 230), 28)
Circle((340, 230), 28)
Line((302,200), (285, 170))
Line((302, 170), (285, 170))
Arc((300, 165), 30 ,25, 315)

update_when('key_pressed')
end_graphics()