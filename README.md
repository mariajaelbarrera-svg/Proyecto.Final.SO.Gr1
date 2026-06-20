# Proyecto Final — Arquitecto Cloud
**Sistemas Operativos 750001C | Semestre 1 – 2026**
**Universidad del Valle**

---

## Equipo

| Nombre | Código | Rol |
|--------|--------|-----|
| Duber Alvarez Ruiz | 2260403 | Virtualización |
| Maria Jael Barrera Gómez | 2369181 | Sitio web |
| Gustavo Adolfo Chilito | 202266901| Video + Sitio Web |
| Bradley Suescun Ramírez | 2478054 | Contenedores Docker + Orquestación con Kubernetes |

**Grupo asignado:** Grupo 1  
**Distribución gráfica:** Ubuntu 24.04 LTS  
**Distribución consola:** Debian 13.5
**Imagen Docker base:** Ubuntu:24.04

---

## Componente 1: Virtualización con Linux

**Distribuciones instaladas:** VM Gráfica(Ubuntu 24.04) + VM Consola(Debian 13.5)  
**Herramienta:** VirtualBox / VMware

### Evidencias
- Captura instalación VM gráfica
- Captura particionamiento (lsblk)
- Captura configuración de red
- Captura prueba SSH funcional

### Comandos principales
```bash
ip a                          # Ver interfaces de red
lsblk                         # Ver particiones
ssh usuario@ip_vm_consola     # Conectar por SSH
```

---

## Componente 2: Contenedores Docker

**Servicios implementados:**
- Frontend: Nginx sirviendo HTML estático (puerto 80)
- Backend: Python HTTP (puerto 5000)

### Estructura de archivos
```
docker/
├── frontend/
│   ├── Dockerfile.frontend
│   └── index.html
├── backend/
│   ├── Dockerfile.backend
│   └── server.py
└── docker-compose.yml
```

### Evidencias
- Captura `docker compose up -d`
- Captura navegador accediendo al frontend
- Captura `curl http://localhost:5000`

### Comandos principales
```bash
docker compose up -d
docker ps
docker images
curl http://localhost
curl http://localhost:5000
```

---

## Componente 3: Orquestación con Kubernetes

**Herramienta:** Minikube

### Manifiestos
- `deployment.yaml` — Nginx con 2 réplicas
- `service.yaml` — NodePort en puerto 30080

### Evidencias
- Captura `kubectl get pods`
- Captura `kubectl get svc`
- Captura acceso desde navegador
- Captura escalado a 3 réplicas

### Comandos principales
```bash
minikube start
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl scale deployment nginx --replicas=3
minikube service nginx --url
```

---

## Componente 4: Sitio Web de Documentación

**URL del sitio:https://mariajaelbarrera-svg.github.io/Proyecto.Final.SO.Gr1/  
**Video YouTube:https://www.youtube.com/watch?v=kchrieth3qw

### Secciones del sitio
- Home: introducción y objetivos
- Equipo: integrantes con fotos y roles
- Componentes: descripción, capturas y comandos de cada uno
- Conclusiones: aprendizajes, dificultades y recomendaciones

---

## Diagrama de Arquitectura

> Insertar imagen del diagrama (draw.io / Miro / Lucidchart)

---

## Conclusiones

1. [Aprendizaje principal]
2. [Dificultad encontrada y cómo se resolvió]
3. [Recomendación para futuros proyectos]

---

*Proyecto desarrollado para la asignatura Sistemas Operativos 750001C — Semestre 1, 2026*
