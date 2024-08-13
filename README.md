# Haier Web API - for Loxone users
---
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---
Haier Web API - for Loxone users using [Haier's mobile app hOn](https://hon-smarthome.com/) based on [pyhOn](https://github.com/Andre0512/pyhon).
---

# uruchomienie na rPI ( aplikacja wystawion na porcie 10000 ) 

```
docker run -d -p 10000:80 -e USERNAME="xxxxxxxx" -e PASSWORD="xxxxxx" zawadzkipiter/haier-loxone-pi:1.0.3
```

obraz zawadzkipiter/haier-loxone-pi:1.0.3 jest skompilowany na armv7

jeżeli chcemy skompilować obraz na rpi 4+ w arm64 to możemy to wykonać albo budując to na raspberry pi albo na maszynie 
lokalnej poleceniami:
```shell
docker buildx build --platform xxxxxx -t [repo]/[obraz] . --push
```



# Instrukcja użytkownika

## Wymagane parametry w każdym callu
username: user aplikacji hOn

password: hasło aplikacji hOn

device: nazwa urządzenia z aplikacji hOn - tutaj jak nie mamy pewności - strzelamy w endpoint devices.

## Api umożliwia komunikację z urządzeniem Haier poprzez api. Poniżej przykładowe wywołania urządzenia:

### START:
```https://HOST:PORT/settings?username=xxx&password=xxx&device=xxx&onOffStatus=1```

### STOP:
```https://HOST:PORT/settings?username=xxx&password=xxx&device=xxx&onOffStatus=0```

### ZMIANA USTAWIEŃ:
wszystkie parametry do zmiany są opcjonalne.

```https://HOST:PORT/settings?username=xxx&password=xxx&device=xxx&tempSel=21&windDirectionHorizontal=7&windDirectionVertical=8&windSpeed=5&ecHOST:PORTatus=1```

api umożliwia zmianę wszystkich parametrów z listy dostępnych parametrów. Aby pobrać listę parametrów dla naszego urządzenia można strzelić w API:

```https://HOST:PORT/commands?username=xxx&password=xxx&device=xxx```

na zwrocie otrzymamy np:

``` json 
{'10degreeHeatingStatus': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'ch2oCleaningStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'cleaningTimeStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'ecHOST:PORTatus': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'electricHeatingStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'energySavePeriod': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '15'}, 'energySavingStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'filterChangeStatusCloud': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'freshAirStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'halfDegreeSettingStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'healthMode': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'heatAccumulationStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'humanSensingStatus': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '3', 'incrementValue': '1'}, 'humidificationStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'humiditySel': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '30'}, 'intelligenceStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'lightStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'lockStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'machMode': {'category': 'command', 'typology': 'enum', 'mandatory': 1, 'defaultValue': '0', 'enumValues': [0, 1, 2, 4, 6]}, 'muteStatus': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'onOffStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '1'}, 'operationName': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': 'grSetDAC'}, 'pm2p5CleaningStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'pmvStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'rapidMode': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'screenDisplayStatus': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '1', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'selfCleaning56Status': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'selfCleaningStatus': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'silentSleepStatus': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '0', 'minimumValue': '0', 'maximumValue': '1', 'incrementValue': '1'}, 'specialMode': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'tempSel': {'category': 'command', 'typology': 'range', 'mandatory': 1, 'defaultValue': '22', 'minimumValue': '16', 'maximumValue': '30', 'incrementValue': '1'}, 'tempUnit': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'voiceSignStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'voiceStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'windDirectionHorizontal': {'category': 'command', 'typology': 'enum', 'mandatory': 1, 'defaultValue': '0', 'enumValues': [0, 3, 4, 5, 6, 7]}, 'windDirectionVertical': {'category': 'command', 'typology': 'enum', 'mandatory': 1, 'defaultValue': '5', 'enumValues': [2, 4, 5, 6, 7, 8]}, 'windSensingStatus': {'category': 'command', 'typology': 'fixed', 'mandatory': 1, 'fixedValue': '0'}, 'windSpeed': {'category': 'command', 'typology': 'enum', 'mandatory': 1, 'defaultValue': '5', 'enumValues': [1, 2, 3, 5]}}
```

Widać tam jaki parametr jakie może przyjmować wartości. Opis niektórych parametrów znajdziemy tutaj:


<https://github.com/Andre0512/hon/blob/6906e751b1a7af5411d3ab5ce761174b48752077/custom_components/hon/const.py>

lub po prostu przeszukując to repozytorium.


### ZMIANA NIESTANDARDOWEGO PARAMETRU:
 - np. zmiana trybu pracy AC na grzanie ( machMode=4):

```https://HOST:PORT/settings?username=xxx&password=xxx&device=xxx&machMode=4```


### STATUS:
```https://HOST:PORT/status?username=xxx&password=xxx&device=xxx```


### WYCISZENIE “BEEP” - DŹWIĘKU PRZY KAŻDEJ ZMIANIE:
zalecam dodanie tej opcji dopiero jak przetestujemy i siebie wszystkie komendy i będą one działały. W celu wyciszenie dźwięku wystarczy do każdej komendy “start/stop/settings” dodać parametr: &ecHOST:PORTatus=1 np start:

```https://HOST:PORT/settings?username=xxx&password=xxx&device=xxx&onOffStatus=1&echoStatus=1```


### Wyłączenie wyświetlacza:
```https://HOST:PORT/settings?username=xxx&password=xxx&device=xxx&onOffStatus=1&screenDisplayStatus=0&echoStatus=1```
