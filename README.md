# Rebus Test

Para los modelos Player y Team usé vistas ModelViewSet, mientras que para CouchingStaffView usé APIView en la cual implementé manualmente los metodos GET, POST, PATCH y DELETE.

Para la gestion de los archivos usé la API de Google Storage.

Los endpoints y sus respectivos bodies que conforman el CRUD son los suguientes:

GET, POST:


* http://localhost:8000/api/teams/

      {

      "name": "PSG",

      "flag": (Imagen en base 64),

      "shield": (Imagen en base 64)
      }

* http://localhost:8000/api/players/ 

      {
      "name": "ROberto",

      "last_name": "k",

      "birthday": "2001-05-20",

      "position": "ss",

      "shirt_number": 2,

      "is_titular": false,

      "team": 1,

      "photo": (Imagen en base 64)
      }
    
Validaciones: Birthday no puede ser pasado, shirt number debe estar entre 1 y 99


* http://localhost:8000/api/couching_staff/

        {
        "name": "Sebsatian",

        "last_name": "ROmero",

        "birthday": "1980-01-01",

        "birth_country": "Brasil",

        "rol": "tecnico",

        "team": 1
        }
        
Validaciones: Birthday no puede ser pasado, rol solo puede ser: Tecnico, asistente, medico, preparador


PATCH, DELETE:


* http://localhost:8000/api/teams/id
* http://localhost:8000/api/players/id
* http://localhost:8000/api/couching_staff/id

* Cuánto equipos hay registrados

localhost:8000/services/count_teams

* Total de jugadores que participarán en el campeonato

localhost:8000/services/count_players

* Quién es el jugador más joven

localhost:8000/services/youngest_player

* Quien es el jugador mas viejo

localhost:8000/services/oldest_player

* Cuantos jugadores suplentes hay

localhost:8000/services/substitute_players_count

* Promedio de número jugadores suplentes en cada equipo

localhost:8000/services/substitute_players_mean

* Cuál de los equipo fue el que mas registró jugadores?

localhost:8000/services/biggest_team

* Cuál es la edad promedio de los jugadores?

localhost:8000/services/players_age_mean

* Cuál es el promedio de número de jugadores en cada equipo?

localhost:8000/services/team_players_mean

* Quien es el técnico más viejo

localhost:8000/services/oldest_technician





