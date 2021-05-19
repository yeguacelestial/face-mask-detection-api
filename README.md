# Face Mask Detection API
Face Mask Detection API - v1

This API is a prototype of what can be made with Machine Learning, specifically
how can a trained model be integrated with a REST API environment.

## Base Endpoint

The following URL indicates the main base URL of all the requests.
```url
https://face-mask-detection-api.herokuapp.com/api/v1/mask-detection/
```

## Mask detection

As of now, the API has only one endpoint. It can list the images sent to the API,
and receive new images to be processed by the model.

The model doesn't know whether the image has a human or not.

### Sending images

In order to send an image to the API, you must make a POST request
to the following endpoint.

**Definition**

`POST api/v1/mask-detection`

**Arguments**
- `"image": <ImageObject>`, a file of a static image with a human face on it.

**Response**
- The results of the prediction made by the model.

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "prediction_result": {
        "person_has_mask": false,
        "scalar_result": 1
    }
}
```

- If the file is not an image:

```json
HTTP 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

```

### Retrieving sent images

You can also retrieve the images that users had send to the API.
Since there is no filter yet, this can lead to unexpected results, so
beware. Trolling is quite common these days.

**Definition**

`GET api/v1/mask-detection`


**Response**

- You'll get a collection of resources. Each one has an associated id, the filename
and the whether the person on the photo has a mask or not.

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "image": "Images/test_with_mask_8j1mBKu.jpg",
        "person_has_mask": true
    },
    {
        "id": 2,
        "image": "Images/test_without_mask_zq1Oby3.jpg",
        "person_has_mask": false
    },
    {
        "id": 3,
        "image": "Images/ENGE6RoWwAADw66_V9kLbY4.jpeg",
        "person_has_mask": true
    }
]
```
