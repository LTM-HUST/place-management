import os

from enum import Enum
import socket
from _thread import *
import threading

from typing import Union, Literal
import json
import datetime
from zoneinfo import ZoneInfo

PLACE_CATEGORY = [
  'accounting',
  'airport',
  'amusement_park',
  'aquarium',
  'art_gallery',
  'atm',
  'bakery',
  'bank',
  'bar',
  'beauty_salon',
  'bicycle_store',
  'book_store',
  'bowling_alley',
  'bus_station',
  'cafe',
  'campground',
  'car_dealer',
  'car_rental',
  'car_repair',
  'car_wash',
  'casino',
  'cemetery',
  'church',
  'city_hall',
  'clothing_store',
  'convenience_store',
  'courthouse',
  'dentist',
  'department_store',
  'doctor',
  'drugstore',
  'electrician',
  'electronics_store',
  'embassy',
  'fire_station',
  'florist',
  'funeral_home',
  'furniture_store',
  'gas_station',
  'gym',
  'hair_care',
  'hardware_store',
  'hindu_temple',
  'home_goods_store',
  'hospital',
  'insurance_agency',
  'jewelry_store',
  'laundry',
  'lawyer',
  'library',
  'light_rail_station',
  'liquor_store',
  'local_government_office',
  'locksmith',
  'lodging',
  'meal_delivery',
  'meal_takeaway',
  'mosque',
  'movie_rental',
  'movie_theater',
  'moving_company',
  'museum',
  'night_club',
  'painter',
  'park',
  'parking',
  'pet_store',
  'pharmacy',
  'physiotherapist',
  'plumber',
  'police',
  'post_office',
  'primary_school',
  'real_estate_agency',
  'restaurant',
  'roofing_contractor',
  'rv_park',
  'school',
  'secondary_school',
  'shoe_store',
  'shopping_mall',
  'spa',
  'stadium',
  'storage',
  'store',
  'subway_station',
  'supermarket',
  'synagogue',
  'taxi_stand',
  'tourist_attraction',
  'train_station',
  'transit_station',
  'travel_agency',
  'university',
  'veterinary_care',
  'zoo'
]

FRIEND_STATUS = [
    "waiting",
    "accepted",
    "rejected"
]

LOG_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.txt')

def recvall_str(sock):
    # Helper function to recv all streaming data using \r\n
    data = ""
    condition = True
    while condition:
        packet = sock.recv(1024)
        if not packet:
            return data
        packet_str = packet.decode('utf8')
        if packet_str.endswith("\r\n"):
            condition = False
        data += packet.decode('utf8')
    return str(data[:-2])

def sendall_str(sock, message: Union[dict, str]):
    if isinstance(message, dict):
        message = json.dumps(message)
    
    if not message.endswith("\r\n"):
        message += "\r\n"
    sock.sendall(message.encode("utf-8"))
    
def write_log(ip_client, port_client, type: Literal["connect", "close", "request", "response"], data: Union[dict, str] = None):
    if data:
        if isinstance(data, dict):
            data = json.dumps(data)
    
    current_time = datetime.datetime.now(tz=ZoneInfo("Asia/Ho_Chi_Minh"))
    
    message = None
    if type == "connect":
        message = f"{current_time}: Server was connected to {ip_client}:{port_client}\n"
    if type == "close":
        message = f"{current_time}: Closed connection to {ip_client}:{port_client}\n"
    if type == "request" and data:
        message = f"{current_time}: Client {ip_client}:{port_client} sent message to server: {data}\n"
    if type == "response" and data:
        message = f"{current_time}: Client {ip_client}:{port_client} received message from server: {data}\n"
        
    if message:
        with open(LOG_PATH, "a+", encoding="utf-8") as f:
            f.write(message)
    
    
    
    
