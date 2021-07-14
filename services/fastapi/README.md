# API DOC



## Endpoints

**Route:**
`/api/v1/table`

**Type**

`POST`


**Body**

```json
    {
        "page_data": "integer",
        "index": "number"
    }
```


**Response**

```json

{
    "index": "integer"
}
```


**Route:**
`/api/v1/logger`

**Type**

`POST`


**Body**

```json
    {
        "index": "number",
        "kind": "string",
        "text": "string,

    }
```

**Response**

```json

{
    "index": "integer"
}
```


**Route:**
`/api/v1/create_queue`

**Type**

`POST`


**Body**

```json
    {
        "start_index": "number",
        "end_index": "number",
        "batch_size": "number,

    }
```

**Response**

```json

{
    "total_jobs": "integer"
}
```

**Route:**
`/api/v1/params`

**Type**

`GET`


**Response**

```json

{
        "start_index": "number",
        "end_index": "number",
        "batch_size": "number",
}
```



**Route:**
`/api/v1/dequeue`

**Type**

`GET`


**Response**

```json

{
    "job" : [[1,2],[3,4]]
}
```


**Route:**
`/api/v1/queue_size`

**Type**

`GET`


**Response**

```json

{
    "queue_size" : "number"
}
```

