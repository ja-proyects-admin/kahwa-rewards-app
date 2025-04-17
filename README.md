# Kahwa Rewards App ☕️🎁

Este repositorio contiene el código fuente de una función HTTP desplegada en Google Cloud Functions (2da generación) que forma parte del backend de la app **Kahwa Rewards**.

## 📦 Arquitectura

- **Lenguaje**: Python 3.10
- **Infraestructura**: Google Cloud Platform
- **Deploys automáticos**: Configurados mediante triggers de Cloud Build

## 🚀 Deploy automático

| Rama            | Entorno      | Proyecto GCP               | Bucket                         |
|------------------|---------------|------------------------------|----------------------------------|
| `feat/*`          | Desarrollo  | `apps-backend-dev-01`       | `apps-backend-dev-storage`      |
| `main`            | Producción  | `apps-backend-prod-01`      | `apps-backend-prod-storage`     |

### 🛠 Triggers activos en Cloud Build

- **`feat/*`**: despliega automáticamente a `dev` cuando se hace push
- **`main`**: despliega automáticamente a `prod` cuando se mergea o pushea

## 📂 Estructura del repo

```
.
├── main.py              # Código fuente de la función
├── requirements.txt     # Dependencias Python
└── cloudbuild.yaml      # Configuración CI/CD para deploy automático
```

## ✅ Checklist para nuevas funciones

- [ ] Crear nueva rama desde `main`: `feat/nombre-funcion`
- [ ] Desarrollar la función en `main.py`
- [ ] Probar localmente con `functions-framework`
- [ ] Push a `feat/*` → se deploya automáticamente a `dev`
- [ ] Merge a `main` → se deploya automáticamente a `prod`

---

> ¿Querés agregar integración con Firestore, Pub/Sub o Cloud Storage en el próximo paso?
