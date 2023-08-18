# ShiftHeroes by Harry JMG

![python](https://img.shields.io/badge/Python-3.11.4-red?logo=Python&label=python&logoColor=white) 

[Challenge Web Site](https://shiftheroes.fr)

---

## Summary
1. [API](https://github.com/lybe-source/shiftheroes#api)
1. [Plannings](https://github.com/lybe-source/shiftheroes#plannings)
1. [Shift](https://github.com/lybe-source/shiftheroes#shifts)
1. [Reservations](https://github.com/lybe-source/shiftheroes#r%C3%A9servations)
1. [Converter](https://github.com/lybe-source/shiftheroes#converter)

---

## API
Toutes les requêtes de l'API doivent être authentifiées à l'aide du token d'API généré via l'interface utilisateur. L'authentification doit être effectuée en incluant le header ```Authorization: Bearer YOUR_API_TOKEN``` dans chaque requête.  

YOUR_API_TOKEN est une clé unique qui te permettra d'accéder à l'API ( [Générer un token](https://shiftheroes.fr/api_tokens) )  

---

## Plannings
Les plannings sont la ressource centrale de l'API. Tu peux lister tous les plannings disponibles et filtrer par type.  
- Lister les plannings ```GET /api/v1/plannings```  

Endpoint : ```GET /api/v1/plannings``` Requête (sans filtre) :  
```bash
curl -X GET "https://shiftheroes.fr/api/v1/plannings" -H "Authorization: Bearer YOUR_API_TOKEN"
```
OR  
```bash
$headers = @{
    "Authorization" = "Bearer YOUR_API_TOKEN"
}
$response = Invoke-WebRequest -Uri "https://shiftheroes.fr/api/v1/plannings" -Headers $headers
```

Requête (avec filtre de type) :  
```bash
curl -X GET "https://shiftheroes.fr/api/v1/plannings?type=TYPE" -H "Authorization: Bearer YOUR_API_TOKEN"
```
OR  
```bash
$headers = @{
    "Authorization" = "Bearer YOUR_API_TOKEN"
}
$response = Invoke-WebRequest -Uri "https://shiftheroes.fr/api/v1/plannings?type=TYPE" -Headers $headers
```

Réponse :  
```bash
[ { "id": "X05fNV", "planning_type": "daily", "state": "available", "published_at": "2023-07-07T08:46:45.215Z" }, { "id": "e6bdK2", "planning_type": "permanent", "state": "available", "published_at": "2023-07-07T08:37:54.353Z" }, { "id": "j9KDf4", "planning_type": "weekly", "state": "available", "published_at": "2023-07-07T08:47:58.611Z" } ]
```

Astuce :  
Utilisez le paramètre ?type=TYPE pour filtrer les plannings selon leur type (permanent, daily, weekly).

---

## Shifts
- Lister les créneaux d'un planning ```GET /api/v1/plannings/:planning_id/shifts```

Endpoint : ```GET /api/v1/plannings/:planning_id/shifts``` Requête :  
```bash
curl -X GET "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts" -H "Authorization: Bearer YOUR_API_TOKEN"
```
OR  
```bash
$headers = @{
    "Authorization" = "Bearer YOUR_API_TOKEN"
}
$response = Invoke-WebRequest -Uri "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts" -Headers $headers
```

Réponse :  
```bash
[ { "id": "lqQFnY", "day": "mardi", "start_hour": "2000-01-01T08:00:00.000Z", "end_hour": "2000-01-01T14:00:00.000Z", "seats": 10, "seats_taken": 1 }, { "id": "x2OFW1", "day": "lundi", "start_hour": "2000-01-01T08:00:00.000Z", "end_hour": "2000-01-01T14:00:00.000Z", "seats": 12, "seats_taken": 0 } // autres shifts... ]
```

Astuce :  
Dans l'exemple j'utilise dans l'url *:planning_id* , ce qu'il faut faire c'est modifier cette valeur par la valeur de l'identifiant du planning souhaité.  

---

## Réservations
- Lister ses réservations sur un planning ```GET /api/v1/plannings/:planning_id/reservations```

Endpoint : ```GET /api/v1/plannings/:planning_id/reservation``` Requête :  
```bash
curl -X GET "https://shiftheroes.fr/api/v1/plannings/:planning_id/reservations" -H "Authorization: Bearer YOUR_API_TOKEN"
```
OR  
```bash
$headers = @{
    "Authorization" = "Bearer YOUR_API_TOKEN"
}
$response = Invoke-WebRequest -Uri "https://shiftheroes.fr/api/v1/plannings/:planning_id/reservations" -Headers $headers
```

Réponse :  
```bash
[ { "id": 103, "user_id": 5, "shift_id": "lqQFnY" // autres attributs de la réservation... }, { "id": 104, "user_id": 5, "shift_id": "x2OFW1" // autres attributs de la réservation... } // autres réservations... ]
```

- Créer une réservation sur un shift ```POST /api/v1/plannings/:planning_id/shifts/:shift_id/reservations```  

Endpoint : ```POST /api/v1/plannings/:planning_id/shifts/:shift_id/reservations``` Requête :  
```bash
curl -X POST "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts/:shift_id/reservations" -H "Authorization: Bearer YOUR_API_TOKEN"
```
OR  
```bash
$headers = @{
    "Authorization" = "Bearer YOUR_API_TOKEN"
}
$response = Invoke-WebRequest -Uri "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts/:shift_id/reservations" -Method Post -Headers $headers
```

Réponse :  
```bash
La réservation est crée avec succès.
```

- Supprimer une réservation ```DELETE /api/v1/plannings/:planning_id/shifts/:shift_id/reservations/:reservation_id```  

Endpoint : ```DELETE /api/v1/plannings/:planning_id/shifts/:shift_id/reservations/:reservation_id``` Requête :  
```bash
curl -X DELETE "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts/:shift_id/reservations/:reservation_id" -H "Authorization: Bearer YOUR_API_TOKEN"
```
OR  
```bash
$headers = @{
    "Authorization" = "Bearer YOUR_API_TOKEN"
}
$response = Invoke-WebRequest -Uri "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts/:shift_id/reservations/:reservation_id" -Method Delete -Headers $headers
```

Réponse :  
```bash
La réservation est supprimée avec succès.
```

---

## Converter

I've used this to convert Curl requests to Python  
[Curl Converter](https://curlconverter.com/python/)

---
