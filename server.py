import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/ortegalex/api/horse-racing'

mcp = FastMCP('horse-racing')

@mcp.tool()
def racecards(date: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get races list.'''
    url = 'https://horse-racing.p.rapidapi.com/racecards'
    headers = {'x-rapidapi-host': 'horse-racing.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def results(date: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get results by date.'''
    url = 'https://horse-racing.p.rapidapi.com/results'
    headers = {'x-rapidapi-host': 'horse-racing.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def race_detail_info(id_race: Annotated[str, Field(description='')]) -> dict: 
    '''Get racecard detailed info and Odds comparator Horses, Jockeys, Trainers, Form, OR, Owner, Sire, Dam, Age, Weight and more information.'''
    url = 'https://horse-racing.p.rapidapi.com/race/207660'
    headers = {'x-rapidapi-host': 'horse-racing.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id_race': id_race,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_races(course: Annotated[Union[str, None], Field(description='Like Cheltenham, Ascot, Newmarket ....')] = None,
                name: Annotated[Union[str, None], Field(description='Race name or a text on the race name. Like "Novice", "Handicap chase", "Hurdle", ....')] = None,
                distance_from: Annotated[Literal['2f', '4f', '5f', '6f', '7f', '1m', '1m1f', '1m2f', '1m3f', '1m4f', '1m5f', '1m6f', '1m7f', '2m', '2m1f', '2m2f', '2m3f', '2m4f', '2m5f', '2m6f', '2m7f', '3m', '3m1f', '3m2f', '3m3f', '3m4f', '3m5f', '3m6f', '3m7f', '4m', '4m1f', '4m2f', '4m3f', None], Field(description='')] = None,
                distance_to: Annotated[Literal['2f', '4f', '5f', '6f', '7f', '1m', '1m1f', '1m2f', '1m3f', '1m4f', '1m5f', '1m6f', '1m7f', '2m', '2m1f', '2m2f', '2m3f', '2m4f', '2m5f', '2m6f', '2m7f', '3m', '3m1f', '3m2f', '3m3f', '3m4f', '3m5f', '3m6f', '3m7f', '4m', '4m1f', '4m2f', '4m3f', None], Field(description='')] = None,
                class_from: Annotated[Union[int, float, None], Field(description='Minimum race class. Default: 0')] = None,
                class_to: Annotated[Union[int, float, None], Field(description='Maximum race class. Default: 0')] = None,
                id_horse: Annotated[Union[int, float, None], Field(description='Horse id. If you populate this field the query search races where this horse run. Default: 0')] = None,
                date_from: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                date_to: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                order_by_date: Annotated[Literal['ASC', 'DESC', None], Field(description='Results ordered by date race ascending or descending.')] = None) -> dict: 
    '''The best way to search races.'''
    url = 'https://horse-racing.p.rapidapi.com/query-races'
    headers = {'x-rapidapi-host': 'horse-racing.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'course': course,
        'name': name,
        'distance_from': distance_from,
        'distance_to': distance_to,
        'class_from': class_from,
        'class_to': class_to,
        'id_horse': id_horse,
        'date_from': date_from,
        'date_to': date_to,
        'page': page,
        'order_by_date': order_by_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def query_horses(name: Annotated[str, Field(description='Minimum 3 characters')]) -> dict: 
    '''Search horses by name. Once you get "*id_horse*" from this query, you can get horses stats from "**Horse stats**" endpoint.'''
    url = 'https://horse-racing.p.rapidapi.com/query-horses'
    headers = {'x-rapidapi-host': 'horse-racing.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
