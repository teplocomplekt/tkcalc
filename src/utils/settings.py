import tkinter as tk
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

VERSION = '0.9'

APP_TITLE = f'''Калькулятор Теплокомплект v.{VERSION}'''

APP_DESCRIPTION = 'Калькулятор для расчета днищ Теплокомплект'

DEFAULT_WIDTH = 110
DEFAULT_HIGHT = 90
CENTER_POINT = (112.5, 176)

# FONT = 'GOST type A'
FONT = 'GOST2304 Type A'

A4_PORTRAIT_STAMP = {
    'paths': {
        'medium': [
            [
                (20, 292),
                (205, 292),
                (205, 5),
                (20, 5),
                (20, 292)],
            [
                (90, 292),
                (90, 278),
                (20, 278)],
            [
                (20, 292),
                (8, 292),
                (8, 172),
                (20, 172)],
            [
                (13, 292),
                (13, 172)],
            [
                (20, 232),
                (8, 232)],
            [
                (20, 150),
                (8, 150),
                (8, 5),
                (20, 5)],
            [
                (13, 150),
                (13, 5)],
            [
                (20, 115),
                (8, 115)],
            [
                (20, 90),
                (8, 90)],
            [
                (20, 65),
                (8, 65)],
            [
                (20, 30),
                (8, 30)],
            [
                (20, 60),
                (205, 60)],
            [
                (85, 45),
                (205, 45)],
            [
                (85, 20),
                (205, 20)],
            [
                (20, 40),
                (85, 40)],
            [
                (20, 35),
                (85, 35)],
            [
                (155, 40),
                (205, 40)],
            [
                (155, 40),
                (205, 40)],
            [
                (155, 25),
                (205, 25)],
            [
                (27, 35),
                (27, 60)],
            [
                (37, 5),
                (37, 60)],
            [
                (60, 5),
                (60, 60)],
            [
                (75, 5),
                (75, 60)],
            [
                (85, 5),
                (85, 60)],
            [
                (155, 5),
                (155, 45)],
            [
                (170, 25),
                (170, 45)],
            [
                (187, 25),
                (187, 45)],
            [
                (175.575, 20),
                (175.575, 25)]],
        'thin': [
            [
                (20, 55),
                (85, 55)],
            [
                (20, 50),
                (85, 50)],
            [
                (20, 45),
                (85, 45)],
            [
                (20, 30),
                (85, 30)],
            [
                (20, 25),
                (85, 25)],
            [
                (20, 20),
                (85, 20)],
            [
                (20, 15),
                (85, 15)],
            [
                (20, 10),
                (85, 10)],
            [
                (159.965, 25),
                (159.965, 40)],
            [
                (164.982, 25),
                (164.982, 40)]]},
    'static_text': [
        {
            'title': 'Изм.',
            'size': 4.99507,
            'coordinates': (20.5, 35.7267)},
        {
            'title': 'Лист',
            'size': 4.99507,
            'coordinates': (27.6036, 35.7267)},
        {
            'title': '№ докум.',
            'size': 4.99507,
            'coordinates': (40.6749, 35.7267)},
        {
            'title': 'Подп.',
            'size': 4.99507,
            'coordinates': (63.1476, 35.7267)},
        {
            'title': 'Дата',
            'size': 4.99507,
            'coordinates': (75.6036, 35.7267)},
        {
            'title': 'Разраб.',
            'size': 4.99507,
            'coordinates': (20.5, 30.7267)},
        {
            'title': 'Пров.',
            'size': 4.99507,
            'coordinates': (20.5, 25.7267)},
        {
            'title': 'Т.контр.',
            'size': 4.99507,
            'coordinates': (20.5, 20.7267)},
        {
            'title': 'Н.контр.',
            'size': 4.99507,
            'coordinates': (20.5, 10.7267)},
        {
            'title': 'Утв.',
            'size': 4.99507,
            'coordinates': (20.5, 5.72668)},
        {
            'title': 'Лит.',
            'size': 4.99507,
            'coordinates': (158.564, 40.7267)},
        {
            'title': 'Масса',
            'size': 4.99507,
            'coordinates': (172.585, 40.7267)},
        {
            'title': 'Масштаб',
            'size': 4.99507,
            'coordinates': (187.516, 40.7267)},
        {
            'title': 'Лист',
            'size': 4.99507,
            'coordinates': (156.362, 20.7267)},
        {
            'title': 'Листов',
            'size': 4.99507,
            'coordinates': (177.405, 20.7267)},
        {
            'title': '1',
            'size': 4.99507,
            'coordinates': (197.905, 20.7267)},
        {
            'title': 'Копировал',
            'size': 4.99507,
            'coordinates': (95.5, 0.726674)},
        {
            'title': 'Формат',
            'size': 4.99507,
            'coordinates': (165.5, 0.726674)},
        {
            'title': 'A4',
            'size': 4.99507,
            'coordinates': (185.5, 0.726674)}],
    'static_text_title': [
        {
            'title': 'Согласовано',
            'size': 7,
            'coordinates': (130, 280)},
        {
            'title': 'Заказчик_____________________________',
            'size': 7,
            'coordinates': (100, 273)},
        {
            'title': 'Подпись_______________Дата__________',
            'size': 7,
            'coordinates': (100, 266)},
        {
            'title': 'Должность___________________________',
            'size': 7,
            'coordinates': (100, 259)},
        {
            'title': 'ФИО_________________________________',
            'size': 7,
            'coordinates': (100, 252)},
        {
            'title': 'М.П.',
            'size': 7,
            'coordinates': (100, 245)}],
    'static_text_90': [
        {
            'title': 'Инв. № подл.',
            'size': 4.99507,
            'coordinates': (12.2733, 6.66531)},
        {
            'title': 'Подп. и дата.',
            'size': 4.99507,
            'coordinates': (12.2733, 35.7505)},
        {
            'title': 'Взам. инв. №',
            'size': 4.99507,
            'coordinates': (12.2733, 65.9357)},
        {
            'title': 'Инв. № дубл.',
            'size': 4.99507,
            'coordinates': (12.2733, 91.6653)},
        {
            'title': 'Подп. и дата',
            'size': 4.99507,
            'coordinates': (12.2733, 120.751)},
        {
            'title': 'Справ. №',
            'size': 4.99507,
            'coordinates': (12.2733, 193.677)},
        {
            'title': 'Перв. примен.',
            'size': 4.99507,
            'coordinates': (12.2733, 250.61)}]}
IPAD = {
    'ipadx': 6,
    'ipady': 6}

PAD = {
    'padx': 4,
    'pady': 2
}

POSITION = {'anchor': tk.NW} | PAD

GRID_POSITION = {
                    'row': 0,
                    'column': 0,
                    'columnspan': 1,
                    'sticky': tk.NSEW} | PAD | IPAD

STEEL_3 = 'Ст3'
STEEL_AISI_409 = 'AiSi 409'
STEEL_09G2C = '09Г2С'
STEEL_AISI_304 = 'AiSi 304'
STEEL_BT_1 = 'ВТ-1'
STEEL_AISI_321 = 'AiSi 321'
STEEL_AISI_316 = 'AiSi 316'

Q = {
    STEEL_BT_1: 143,
    STEEL_AISI_409: 159,
    STEEL_AISI_316: 179,
    STEEL_AISI_321: 179,
    STEEL_AISI_304: 170,
    STEEL_09G2C: 195,
    STEEL_3: 154
}

S_MIN = {
    '300': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '350': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '400': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '450': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '500': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 3, 'r_80': 3, 'r_100': 0, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '550': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 3, 'r_80': 3, 'r_100': 0, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '600': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 3, 'r_80': 3, 'r_100': 0, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '650': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 3, 'r_80': 3, 'r_100': 4, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '700': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 3, 'r_80': 3, 'r_100': 4, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '750': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 0, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '800': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '850': {'r_30': 3, 'r_50': 3, 'r_60': 3, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '900': {'r_30': 3, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '950': {'r_30': 3, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 0, 'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1000': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 4, 'r_180': 0,
             'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1100': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 4, 'r_180': 0,
             'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1200': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 5, 'r_180': 5,
             'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1300': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 4, 'r_150': 5, 'r_180': 5,
             'r_200': 5, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1400': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 5, 'r_150': 5, 'r_180': 5,
             'r_200': 5, 'r_220': 6, 'r_250': 6, 'r_300': 6},
    '1500': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 4, 'r_120': 5, 'r_150': 5, 'r_180': 5,
             'r_200': 5, 'r_220': 6, 'r_250': 6, 'r_300': 6},
    '1600': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 5, 'r_120': 5, 'r_150': 5, 'r_180': 5,
             'r_200': 6, 'r_220': 6, 'r_250': 6, 'r_300': 6},
    '1700': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 4, 'r_80': 4, 'r_100': 5, 'r_120': 5, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 6, 'r_300': 6},
    '1800': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 5, 'r_80': 5, 'r_100': 5, 'r_120': 5, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 6, 'r_300': 6},
    '1900': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 5, 'r_80': 5, 'r_100': 5, 'r_120': 5, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 6, 'r_300': 6},
    '2000': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 5, 'r_80': 5, 'r_100': 5, 'r_120': 6, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 6, 'r_300': 6},
    '2100': {'r_30': 4, 'r_50': 4, 'r_60': 4, 'r_75': 5, 'r_80': 5, 'r_100': 5, 'r_120': 6, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 6, 'r_300': 7},
    '2200': {'r_30': 4, 'r_50': 5, 'r_60': 5, 'r_75': 5, 'r_80': 5, 'r_100': 6, 'r_120': 6, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 6, 'r_300': 7},
    '2300': {'r_30': 4, 'r_50': 5, 'r_60': 5, 'r_75': 5, 'r_80': 5, 'r_100': 6, 'r_120': 6, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 7, 'r_300': 7},
    '2400': {'r_30': 4, 'r_50': 5, 'r_60': 5, 'r_75': 6, 'r_80': 6, 'r_100': 6, 'r_120': 6, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 6, 'r_250': 7, 'r_300': 7},
    '2500': {'r_30': 5, 'r_50': 5, 'r_60': 5, 'r_75': 6, 'r_80': 6, 'r_100': 6, 'r_120': 6, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '2600': {'r_30': 5, 'r_50': 5, 'r_60': 5, 'r_75': 6, 'r_80': 6, 'r_100': 6, 'r_120': 6, 'r_150': 6, 'r_180': 6,
             'r_200': 6, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '2700': {'r_30': 5, 'r_50': 5, 'r_60': 5, 'r_75': 6, 'r_80': 6, 'r_100': 6, 'r_120': 6, 'r_150': 6, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '2800': {'r_30': 5, 'r_50': 6, 'r_60': 6, 'r_75': 6, 'r_80': 6, 'r_100': 6, 'r_120': 6, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '2900': {'r_30': 5, 'r_50': 6, 'r_60': 6, 'r_75': 6, 'r_80': 6, 'r_100': 6, 'r_120': 6, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '3000': {'r_30': 5, 'r_50': 6, 'r_60': 6, 'r_75': 6, 'r_80': 6, 'r_100': 6, 'r_120': 7, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '3100': {'r_30': 6, 'r_50': 6, 'r_60': 6, 'r_75': 6, 'r_80': 6, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '3200': {'r_30': 6, 'r_50': 6, 'r_60': 6, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 7, 'r_300': 7},
    '3300': {'r_30': 6, 'r_50': 6, 'r_60': 6, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 8, 'r_300': 8},
    '3400': {'r_30': 6, 'r_50': 7, 'r_60': 7, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 8, 'r_300': 8},
    '3500': {'r_30': 6, 'r_50': 7, 'r_60': 7, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 7,
             'r_200': 7, 'r_220': 7, 'r_250': 8, 'r_300': 8},
    '3600': {'r_30': 7, 'r_50': 7, 'r_60': 7, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 7,
             'r_200': 8, 'r_220': 8, 'r_250': 8, 'r_300': 8},
    '3700': {'r_30': 7, 'r_50': 7, 'r_60': 7, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 8,
             'r_200': 8, 'r_220': 8, 'r_250': 8, 'r_300': 8},
    '3800': {'r_30': 7, 'r_50': 7, 'r_60': 7, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 8,
             'r_200': 8, 'r_220': 8, 'r_250': 8, 'r_300': 8},
    '3900': {'r_30': 7, 'r_50': 7, 'r_60': 7, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 8,
             'r_200': 8, 'r_220': 8, 'r_250': 8, 'r_300': 8},
    '4000': {'r_30': 7, 'r_50': 7, 'r_60': 7, 'r_75': 7, 'r_80': 7, 'r_100': 7, 'r_120': 7, 'r_150': 7, 'r_180': 8,
             'r_200': 8, 'r_220': 8, 'r_250': 8, 'r_300': 8}
}
S_MAX = {
    '300': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0,
            'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '350': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0,
            'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '400': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0,
            'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '450': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 0, 'r_80': 0, 'r_100': 0, 'r_120': 0, 'r_150': 0,
            'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '500': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 0, 'r_120': 0, 'r_150': 0,
            'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '550': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 0, 'r_120': 0, 'r_150': 0,
            'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '600': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 0, 'r_120': 0, 'r_150': 0,
            'r_180': 0,
            'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '650': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 0, 'r_150': 0,
            'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '700': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 0, 'r_150': 0,
            'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '750': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 0, 'r_150': 0,
            'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '800': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 13, 'r_150': 0,
            'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '850': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 13, 'r_150': 0,
            'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '900': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 13, 'r_150': 0,
            'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '950': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 13, 'r_150': 0,
            'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1000': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 12, 'r_120': 13, 'r_150': 13,
             'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1100': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 0, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1200': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 0, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1300': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 0, 'r_250': 0, 'r_300': 0},
    '1400': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '1500': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '1600': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '1700': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '1800': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '1900': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2000': {'r_30': 6, 'r_50': 8, 'r_60': 8, 'r_75': 10, 'r_80': 10, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2100': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2200': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2300': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2400': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2500': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2600': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2700': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2800': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '2900': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3000': {'r_30': 7, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3100': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3200': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3300': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3400': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3500': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3600': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3700': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3800': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '3900': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10},
    '4000': {'r_30': 8, 'r_50': 9, 'r_60': 9, 'r_75': 11, 'r_80': 11, 'r_100': 13, 'r_120': 13, 'r_150': 13,
             'r_180': 12, 'r_200': 12, 'r_220': 11, 'r_250': 10, 'r_300': 10}
}

CONE_VALUES = {
    '60': {
        '219': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '273': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '325': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '377': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '426': {
            '80': {
                '30': ['4', '6', '8'],
            }
        },
        '480': {
            '80': {
                '30': ['4', '6', '8'],
            }
        },
        '530': {
            '80': {
                '30': ['4', '6', '8'],
            }
        },
        '630': {
            '80': {
                '30': ['4', '6', '8'],
            }
        },
        '720': {
            '80': {
                '40': ['6', '8', '10'],
                '50': ['12'],
            }
        },
        '820': {
            '160': {
                '40': ['6', '8', ],
                '50': ['10', '12'],
            }
        },
        '920': {
            '160': {
                '40': ['6', '8'],
                '50': ['10', '12'],
            }
        },
        '1020': {
            '160': {
                '40': ['6', '8'],
                '50': ['10', '12'],
            }
        },
        '1120': {
            '160': {
                '40': ['6', '8'],
                '50': ['10'],
                '60': ['12', '14'],
            }
        },
        '1220': {
            '160': {
                '40': ['6'],
                '50': ['8', '10'],
                '60': ['12', '14'],
            }
        },
        '1320': {
            '160': {
                '50': ['6', '8', '10'],
                '60': ['12'],
                '70': ['14'],
            }
        },
        '1420': {
            '160': {
                '50': ['6', '8'],
                '60': ['10', '12'],
                '70': ['14', '16'],
            }
        },

    },
    '90': {
        '219': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '273': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '325': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '377': {
            '40': {
                '30': ['4', '6', '8'],
            }
        },
        '426': {
            '80': {
                '30': ['4', '6', '8'],
            }
        },
        '480': {
            '80': {
                '30': ['4', '6', '8', '10'],
            }
        },
        '530': {
            '80': {
                '30': ['4', '6', '8'],
                '40': ['10'],
            }
        },
        '630': {
            '80': {
                '30': ['4', '6', '8'],
                '40': ['10'],
            }
        },
        '720': {
            '80': {
                '40': ['6', '8', '10'],
                '50': ['12'],
            }
        },
        '820': {
            '160': {
                '40': ['6', '8'],
                '50': ['10', '12'],
            }
        },
        '920': {
            '160': {
                '40': ['6', '8'],
                '50': ['10', '12'],
                '60': ['14'],
            }
        },
        '1020': {
            '160': {
                '40': ['6', '8'],
                '50': ['10', '12'],
                '60': ['14', '16'],
            }
        },
        '1120': {
            '160': {
                '40': ['6', '8'],
                '50': ['10'],
                '60': ['12', '14'],
                '70': ['16'],
            }
        },
        '1220': {
            '160': {
                '40': ['6', ],
                '50': ['8', '10'],
                '60': ['12', '14'],
                '70': ['16'],
            }
        },
        '1320': {
            '160': {
                '50': ['6', '8', '10'],
                '60': ['12'],
                '70': ['14', '16'],
            }
        },
        '1420': {
            '160': {
                '50': ['6', '8'],
                '60': ['10', '12'],
                '70': ['14', '16'],
            }
        },
    },
}
