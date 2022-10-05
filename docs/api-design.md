## Breweries
* Get a list of breweries
* Detailed view of breweries (get information)
* Create a brewery
* Update a brewery
* Delete a brewery

## Beers
* List beers all beers by city
* Detailed view of beers 
* Create a beer
* Update a beer
* Delete a beer

---

## Favorites
* List of favorite beers/breweries for a user
* Add a favorite
* Delete a favorite

## Users
* View User details
* Update user information
* Sign up/Create User
* Delete User
* Log in/out (create/delete token)

---

## Breweries
### Get a list of breweries

* Endpoint path: /{city}/breweries/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A list of breweries
* Response shape:
    ```json
    {
      "breweries": [
        {
          "brewery_id": string,
          "name": string,
          "street": string,
          "city": string,
          "state": string,
          "zip_code": int,
          "phone": string,
          "image_url": string,
        }
      ]
    }
    ```

### Get a detailed view of a brewery

* Endpoint path: /{city}/breweries/{brewery_id}/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A detailed view of a brewery
* Response shape:
    ```json
    {
      "brewery": [
        {
          "brewery_id": int,
          "name": string,
          "street": string,
          "city": string,
          "state": string,
          "zip_code": int,
          "phone": string,
          "image_url": string,
          "description": string,
          "website": string,
          "beers": [
            {
            "href": /{city}/breweries/{brewery_id}/beers/{beer_id}/,
            "image_url": string,
            "name": string,
            "beer_id": string,
          }
          ]

        }
      ]
    }
    ```

### Create a brewery

* Endpoint path: /{city}/breweries/
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Create a brewery
* Response shape:
    ```json
    {
      "breweries": [
        {
          "brewery_id": string,
          "name": string,
          "street": string,
          "city": string,
          "state": string,
          "zip_code": int,
          "phone": string,
          "image_url": string,
          "description": string,
          "website": string,
        }
      ]
    }
    ```

### Update a brewery

* Endpoint path: /{city}/breweries/{brewery_id}/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Update a brewery
* Response shape:
    ```json
    {
      "breweries": [
        {
          "name": string,
          "street": string,
          "city": string,
          "state": string,
          "zip_code": int,
          "phone": string,
          "image_url": string,
          "description": string,
          "website": string,
        }
      ]
    }
    ```

### Delete a brewery

* Endpoint path: /{city}/breweries/{brewery_id}/
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Delete a brewery
* Response shape:
    ```json
    {
      "deleted": true,
    }
    ```

## Beers
### Get a list of beers

* Endpoint path: /{city}/beers/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A list of beers
* Response shape:
    ```json
    {
      "beers": [
        {
          "beer_id": string,
          "name": string,
          "description": string,
          "brewery": foreign_key,
          "type": string,
          "image_url": string,
        }
      ]
    }
    ```


### Get a detailed view of a beer

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A detailed view of a beer
* Response shape:
    ```json
    {
      "beer": [
        {
          "beer_id": string,
          "name": string,
          "description": string,
          "brewery": foreign_key,
          "type": string,
          "ibu": string,
          "abv": string,
          "image_url": string,
        }
      ]
    }
    ```


### Create a beer

* Endpoint path: /{city}/beers/
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Create a beer
* Response shape:
    ```json
    {
      "beer": [
        {
          "beer_id": string,
          "name": string,
          "description": string,
          "brewery": foreign_key,
          "type": string,
          "ibu": string,
          "abv": string,
          "image_url": string,
        }
      ]
    }
    ```

### Update a beer

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Update a beer
* Response shape:
    ```json
    {
      "beer": [
        {
          "name": string,
          "description": string,
          "brewery": foreign_key,
          "type": string,
          "ibu": string,
          "abv": string,
          "image_url": string,
      ]
    }
    ```

### Delete a beer

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Delete a beer
* Response shape:
    ```json
    {
      "deleted": true,
    }
    ```

## Users
### Get a detailed view of a User

* Endpoint path: /user/{user_id}/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A detailed view of a brewery
* Response shape:
    ```json
    {
        {
          "user_id": int,
          "name": string,
          "username": string,
          "favorite_beers": [
            {
            "href": /{city}/breweries/{brewery_id}/beers/{beer_id}/,
            "image_url": string,
            "name": string,
            "beer_id": string,
            "created_on": date,
          }
          ],
          "favorite_breweries": [
            {
            "href": /{city}/breweries/{brewery_id}/,
            "image_url": string,
            "name": string,
            "brewery_id": string,
            "created_on": date,
          }
          ],
        }
    }
    ```


### Create a User/Sign Up

* Endpoint path: /user/
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Create a brewery
* Response shape:
    ```json
    {
      {
          "name": string,
          "username": string,
          "password": string,
      }
    }
    ```

### Update a User

* Endpoint path: /user/{user_id}/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Update a brewery
* Response shape:
    ```json
    {
      {
          "name": string,
          "username": string,
          "password": string,
      }
    }
    ```

### Delete a User

* Endpoint path: /user/{user_id}/
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Delete a User
* Response shape:
    ```json
    {
      "deleted": true,
    }
    ```

### Login

* Endpoint path: /user/token
* Endpoint method: POST

* Request shape (form):
  * username: string
  * password: string

* Response: Account information and a token
* Response shape (JSON):
    ```json
    {
      "account": {
        «key»: type»,
      },
      "token": string
    }
    ```

### Logout

* Endpoint path: /user/token
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):
    ```json
    true
    ```

## Favourites
### Favourite beers

* Endpoint path: /{user_id}/favorites/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: get a list of favourites for a user
* Response shape:
    ```json
    {
        {  
            "fav_id": string,
            "user_id": string,
            "beer_id": string,
            "brewery_id": string,
            "image_url": string,
            "name": string,
            "created_on": date,
    }
    ```

### Add Favourite beers

* Endpoint path: /{user_id}/favorites/
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Add a favourite
* Response shape:
    ```json
    {
        {  
            "image_url": string,
            "name": string,
            "user_id": string,
            "beer_id": string,
            "brewery_id": string,
    }
    ```

### Delete Favourite beers

* Endpoint path: /{user_id}/favorites/{fav_id}
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Delete a favourite
* Response shape:
    ```json
    {
        {  

    }
    ```