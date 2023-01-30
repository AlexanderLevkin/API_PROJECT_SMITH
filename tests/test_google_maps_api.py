from requests import Response

from utils.api import Google_maps_api

"""Создание изменения и удаление новой локации"""


class Test_create_place:

    def test_create_new_place(self):
        print("\nМетод POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        print(place_id)

        print("\nМетод GET POST")
        result_get: Response = Google_maps_api.get_new_place(place_id=place_id)

        print("\nМетод PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id=place_id)

        print("\nМетод GET PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id=place_id)

        print("\nМетод DELETE")
        result_delete: Response = Google_maps_api.del_new_place(place_id=place_id)

        print("\nМетод GET DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id=place_id)

