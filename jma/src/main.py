import flet as ft
import requests
import json

# 気象庁APIのエンドポイントURL
AREA_URL = "http://www.jma.go.jp/bosai/common/const/area.json"
FORECAST_URL_TEMPLATE = "https://www.jma.go.jp/bosai/forecast/data/forecast/{}.json"

def main(page: ft.Page):
    page.spacing = 0
    page.padding = 0


ft.app(main)
