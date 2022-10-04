## Breweries
* Get a list of breweries
* Detailed view of breweries (get information)
* Create a brewery
* Update a brewery
* Delete a brewery

## Beers
* List beers all beers by city
* Detailed view of beers w/ reviews list of that beer
* Create a beer
* Update a beer
* Delete a beer

## Users
* View User details
  * List of favorite beers
  * List of favorite breweries
  * List of User beer reviews
  * List of User brewery reviews
* Update user information
* Sign up/Create User
* Delete User
* Log in/out (create/delete token)

## Brewery Reviews - in the same microservice as Users
* List reviews by user
* List reviews by brewery
* Detailed view of a specific review
* Create a brewery review
* Update a brewery review
* Delete a delete a brewery review

## Beer Reviews - in the same microservice as Users
* List reviews by user
* List reviews by beer
* Detailed view of a specific review
* Create a beer review
* Update a beer review
* Delete a delete a beer review

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
          "review": [
            {
                "rating": string,
                "text": string,
                "image": string,
                "created_on": date,
            }
          ]
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
          "beer_reviews": [
            {
            "href": /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{review_id},
            "image_url": string,
            "title": string,
            "description": string,
            "rating": int,
            "beer_id": string,
            "beer_name": string,
            "brewery_name": string,
            "created_on": date,
          }
          ],
          "brewery_reviews": [
            {
            "href": /{city}/breweries/{brewery_id}/reviews/{review_id},
            "image_url": string,
            "title": string,
            "description": string,
            "rating": int,
            "brewery_id": string,
            "brewery_name": string,
            "created_on": date,
          }
          ]
        
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


## Brewery Reviews - in the same microservice as Users
### Get a list view of brewery reviews by user

* Endpoint path: /user/{user_id}/brewery_reviews/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A list view of a brewery reviews by user
* Response shape:
    ```json
    {
          "brewery_reviews": [
            {
            "href": /{city}/breweries/{brewery_id}/reviews/{brewery_review_id},
            "image_url": string,
            "username": string,
            "title": string,
            "description": string,
            "rating": int,
            "brewery_id": string,
            "brewery_name": string,
            "created_on": date,
          }
          ]
    }
    ```
### Get a list view of brewery reviews by brewery

* Endpoint path: /{city}/breweries/{brewery_id}/reviews/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A list view of a brewery reviews by brewery
* Response shape:
    ```json
    {
          "brewery_reviews": [
            {
            "href": /{city}/breweries/{brewery_id}/reviews/{brewery_review_id},
            "image_url": string,
            "username": string,
            "title": string,
            "description": string,
            "rating": int,
            "brewery_id": string,
            "brewery_name": string,
            "created_on": date,
          }
          ]
    }
    ```


### Get a detailed view of a brewery review by User

* Endpoint path: /{city}/breweries/{brewery_id}/reviews/{review_id}/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A detailed view of a brewery review
* Response shape:
    ```json
    {
      "brewery_review_id": int,
      "href": /{city}/breweries/{brewery_id}/reviews/{brewery_review_id},
      "image_url": string,
      "username": string,
      "title": string,
      "description": string,
      "rating": int,
      "brewery_id": string,
      "brewery_name": string,
      "created_on": date,  
    }
    ```

### Create a brewery review

* Endpoint path: /{city}/breweries/{brewery_id}/reviews/
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Create a brewery
* Response shape:
    ```json
    {
      "image_url": string,
      "username": string,
      "title": string,
      "description": string,
      "rating": int,
      "brewery_id": string,
      "brewery_name": string,
    }
    ```

### Update a brewery review

* Endpoint path: /{city}/breweries/{brewery_id}/reviews/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Update a brewery
* Response shape:
    ```json
   {
      "image_url": string,
      "username": string,
      "title": string,
      "description": string,
      "rating": int,
      "brewery_id": string,    
      "brewery_name": string,
    }
    ```

### Delete a User

* Endpoint path: /{city}/breweries/{brewery_id}/reviews/
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Delete a brewery review
* Response shape:
    ```json
    {
      "deleted": true,
    }
    ```


## Beer Reviews - in the same microservice as Users
### Get a list view of Beer reviews by User

* Endpoint path: /user/{user_id}/beer_reviews/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A list view of a beer reviews by user
* Response shape:
    ```json
    {
          "beer_reviews": [
            {
            "href": /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{beer_review_id},
            "image_url": string,
            "username": string,
            "title": string,
            "description": string,
            "rating": int,
            "brewery_id": string,
            "brewery_name": string,
            "beer_id": string,
            "beer_name": string,
            "created_on": date,
          }
          ]
    }
    ```
### Get a list view of Beers reviews by Brewery

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A list view of a Beer reviews by brewery
* Response shape:
    ```json
    {
          "beer_reviews": [
          {
            "href": /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{beer_review_id}/,
            "image_url": string,
            "username": string,
            "title": string,
            "description": string,
            "rating": int,
            "brewery_id": string,
            "brewery_name": string,
            "beer_id": string,
            "beer_name": string,
            "created_on": date,
          }
          ]
    }
    ```


### Get a detailed view of a Beer review by User

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{beer_review_id}/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A detailed view of a Beer review
* Response shape:
    ```json
    {
      "beer_review_id": int,
      "href": /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{beer_review_id}/,
      "image_url": string,
      "username": string,
      "title": string,
      "description": string,
      "rating": int,
      "brewery_id": string,
      "brewery_name": string,
      "beer_id": string,
      "beer_name": string,
      "created_on": date,  
    }
    ```

### Create a Beer review

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{beer_review_id}/
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Create a Beer
* Response shape:
    ```json
    {
      "image_url": string,
      "username": string,
      "title": string,
      "description": string,
      "rating": int,
      "brewery_id": string,
      "brewery_name": string,
      "beer_id": string,
      "beer_name": string,
    }
    ```

### Update a Beer review

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{beer_review_id}/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Update a brewery
* Response shape:
    ```json
   {
      "beer_review_id": int,
      "image_url": string,
      "username": string,
      "title": string,
      "description": string,
      "rating": int,
      "brewery_id": string,
      "brewery_name": string,
      "beer_id": string,
      "beer_name": string,
    }
    ```

### Delete a Beer Review

* Endpoint path: /{city}/breweries/{brewery_id}/beers/{beer_id}/reviews/{beer_review_id}/
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Delete a Beer review
* Response shape:
    ```json
    {
      "deleted": true,
    }
    ```



Example API Data from OpenBreweryDB
    {
        "id": "10-56-brewing-company-knox",
        "name": "10-56 Brewing Company",
        "brewery_type": "micro",
        "street": "400 Brown Cir",
        "address_2": null,
        "address_3": null,
        "city": "Knox",
        "state": "Indiana",
        "county_province": null,
        "postal_code": "46534",
        "country": "United States",
        "longitude": "-86.627954",
        "latitude": "41.289715",
        "phone": "6308165790",
        "website_url": null,
        "updated_at": "2022-08-20T02:56:08.975Z",
        "created_at": "2022-08-20T02:56:08.975Z"
    },

