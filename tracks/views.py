from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status

SongsData = [
    {"id": 1, "title": "Billie Jean", "artist": "Michael Jackson", "album": "Thriller", "release_date": "1982", "genre": "R&B"},
    {"id": 2, "title": "Purple Rain", "artist": "Prince", "album": "Purple Rain", "release_date": "1984", "genre": "R&B"},
    {"id": 3, "title": "Super Freak", "artist": "Rick James", "album": "Street Songs", "release_date": "1981", "genre": "R&B"},
    {"id": 4, "title": "I Wanna Dance with Somebody", "artist": "Whitney Houston", "album": "I'm your baby tonight", "release_date": "1981", "genre": "R&B"},
    {"id": 5, "title": "Rock with You", "artist": "Michael Jackson", "album": "Off The Wall", "release_date": "1979", "genre": "R&B"},
    {"id": 6, "title": "Sweet Child o' Mine", "artist": "Guns N' Roses", "album": "Appetite for Destruction", "release_date": "1987", "genre": "R&B"},
]

@api_view(['GET'])
def tracks_list(request):

    return Response(SongsData)





@api_view(['GET'])
def track_detail(request, pk):
    try:
        song = next((song for song in SongsData if song["id"] == pk))
        return Response(song, status=status.HTTP_200_OK)
    except StopIteration:
        return Response({"error": "Song not found."}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
@api_view(['POST'])
def create_song(request):
    new_song = request.data
    new_song["id"] = len(SongsData) + 1
    SongsData.append(new_song)
    return Response(new_song, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_song(request, pk):
    try:
        song_index = next((index for index, song in enumerate(SongsData) if song["id"] == pk))
        SongsData[song_index].update(request.data)
        return Response(SongsData[song_index], status=status.HTTP_200_OK)
    except StopIteration:
        return Response({"error": "Song not found."}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_song(request, pk):
    try:
        song_index = next((index for index, song in enumerate(SongsData) if song["id"] == pk))
        del SongsData[song_index]
        return Response(status=status.HTTP_204_NO_CONTENT)
    except StopIteration:
        return Response({"error": "Song not found."}, status=status.HTTP_404_NOT_FOUND)