from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

two_d_array = []

rows = 10
cols = 20

for row in range(rows):
    temp_arr = []
    for col in range(cols):
        temp_arr.append(Room(title=f'{row} {col}', description=f'{row} {col}'))
    two_d_array.append(temp_arr)
print(two_d_array[0][0].title)


for row in range(rows):
    for col in range(cols):
        two_d_array[row][col].save()


for row in range(rows):
    for col in range(cols):
        if row < rows - 1:
            two_d_array[row][col].connectRooms(two_d_array[row + 1][col], 's')
        if row > 0:
            two_d_array[row][col].connectRooms(two_d_array[row - 1][col], 'n')
        if col < cols - 1:
            two_d_array[row][col].connectRooms(two_d_array[row][col + 1], 'e')
        if col > 0:
            two_d_array[row][col].connectRooms(two_d_array[row][col - 1], 'w')

players = Player.objects.all()
for p in players:
    p.currentRoom = two_d_array[0][0].title
    p.save()

# r_outside = Room(title="Outside Cave Entrance",
#                  description="North of you, the cave mount beckons")

# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""")

# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""")

# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""")

# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()

# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")
