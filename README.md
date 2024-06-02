# Weather App
## Description
Simple project build with FastApi that utilize OpenWeatherMap API to retrive data about weather in given city and provide it in parsed format.
## Packages
Python == 3.10  
FastApi == 0.111.0  
Reqests == 2.32.3  
## Scripts
Run app:
`fastapi dev app/main.py`  
Run tests: 
`pytest`

# Documentation
`GET /weather/`

*Get Weather*

This endpoint allows to fetch data about weather in given city

<h3 id="get_weather_weather__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|city|query|string|true|City name must be alphabetical and non-empty (do not use local alphabet letters, all those letters should be replaced with standard alphabet letters).|

> Example responses

> 200 Response

```json
{
  "temperature": 22.5,
  "description": "broken clouds",
  "humidity": 75,
  "wind_speed": 1.5
}
```

<h3 id="get_weather_weather__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Information about weather in given city containing: temperature (celcius), description of the weather, humidity (%) and wind speed (m/s).|[WeatherResponse](#schemaweatherresponse)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|[Error401Response](#schemaerror401response)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|City Not Found.|[Error404Response](#schemaerror404response)|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Response from OpenWeatherMap API can not be parsed correctly, the structure of the API response may have changed.|[Error409Response](#schemaerror409response)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Error401MassageDetail">Error401MassageDetail</h2>
<!-- backwards compatibility -->
<a id="schemaerror401massagedetail"></a>
<a id="schema_Error401MassageDetail"></a>
<a id="tocSerror401massagedetail"></a>
<a id="tocserror401massagedetail"></a>

```json
{
  "cod": "401",
  "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."
}

```

Error401MassageDetail

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cod|string|true|none|none|
|message|string|true|none|none|

<h2 id="tocS_Error401Response">Error401Response</h2>
<!-- backwards compatibility -->
<a id="schemaerror401response"></a>
<a id="schema_Error401Response"></a>
<a id="tocSerror401response"></a>
<a id="tocserror401response"></a>

```json
{
  "message": {
    "cod": "401",
    "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."
  }
}

```

Error401Response

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|[Error401MassageDetail](#schemaerror401massagedetail)|true|none|none|

<h2 id="tocS_Error404MassageDetail">Error404MassageDetail</h2>
<!-- backwards compatibility -->
<a id="schemaerror404massagedetail"></a>
<a id="schema_Error404MassageDetail"></a>
<a id="tocSerror404massagedetail"></a>
<a id="tocserror404massagedetail"></a>

```json
{
  "cod": "404",
  "message": "city not found"
}

```

Error404MassageDetail

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cod|string|true|none|none|
|message|string|true|none|none|

<h2 id="tocS_Error404Response">Error404Response</h2>
<!-- backwards compatibility -->
<a id="schemaerror404response"></a>
<a id="schema_Error404Response"></a>
<a id="tocSerror404response"></a>
<a id="tocserror404response"></a>

```json
{
  "message": {
    "cod": "404",
    "message": "city not found"
  }
}

```

Error404Response

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|[Error404MassageDetail](#schemaerror404massagedetail)|true|none|none|

<h2 id="tocS_Error409Response">Error409Response</h2>
<!-- backwards compatibility -->
<a id="schemaerror409response"></a>
<a id="schema_Error409Response"></a>
<a id="tocSerror409response"></a>
<a id="tocserror409response"></a>

```json
{
  "error": "Response from OpenWeatherMap API is not processable",
  "message": "Missing expected field: 'humidity'"
}

```

Error409Response

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|error|string|true|none|none|
|message|string|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_WeatherResponse">WeatherResponse</h2>
<!-- backwards compatibility -->
<a id="schemaweatherresponse"></a>
<a id="schema_WeatherResponse"></a>
<a id="tocSweatherresponse"></a>
<a id="tocsweatherresponse"></a>

```json
{
  "temperature": 22.5,
  "description": "broken clouds",
  "humidity": 75,
  "wind_speed": 1.5
}

```

WeatherResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|temperature|number|true|none|none|
|description|string|true|none|none|
|humidity|number|true|none|none|
|wind_speed|number|true|none|none|

