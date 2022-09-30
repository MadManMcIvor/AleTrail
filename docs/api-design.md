## Breweries
* Get a list of breweries
* Detailed view of breweries (get information)
* CRUD

## Beers
* List beers by brewery (flavor?)
* Detail page/review page
* 

## Users
* View user details
* Update user information
* List of favorite beers
* List of favorite breweries
* Sign up
* Log in/out (create/delete token)



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
          "id": string,
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

* Endpoint path: /{city}/breweries/{id}/
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
            "href": /{city}/breweries/{id}/beers/{id}/,
            "image_url": string,
            "name": string,
            "id": string,
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
          "id": string,
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

* Endpoint path: /{city}/breweries/{id}/
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

* Endpoint path: /{city}/breweries/{id}/
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
          "id": string,
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

* Endpoint path: /{city}/breweries/{id}/beers/{id}/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A detailed view of a beer
* Response shape:
    ```json
    {
      "beer": [
        {
          "id": string,
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

* Endpoint path: /{city}/breweries/{id}/beers/{id}/
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

* Endpoint path: /{city}/breweries/{id}/beers/{id}/
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
