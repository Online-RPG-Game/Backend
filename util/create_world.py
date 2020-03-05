from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

two_d_array = []

tiles = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 0],
    [5, 0, 0, 7, 5, 0, 7, 0, 0, 7, 0, 7, 0, 5, 0, 0, 0, 0, 0, 0],
    [5, 0, 6, 6, 5, 0, 0, 0, 6, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 6, 6, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 5, 5, 0, 5, 5, 0, 0, 5, 5, 0, 0, 7, 0, 0, 0, 0],
    [0, 6, 6, 6, 0, 6, 5, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

rows = 10
cols = 20
counter = 1

for row in range(rows):
    temp_arr = []
    for col in range(cols):
        temp_arr.append(
            Room(id=counter, title=f'{row} {col}', description=tiles[row][col]))
        counter += 1
    two_d_array.append(temp_arr)


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
    p.currentRoom = two_d_array[0][0].id
    p.save()
