# Operador de Marketing e Inteligencia de Inventario D2C

Agente de IA especializado en automatización de marketing y gestión de inventario para una tienda **Direct-to-Consumer (D2C)** de ropa de golf que opera con **Shopify**, **Whatnot** (ventas en vivo) y **Meta Ads**.

## Objetivo

Reducir tareas manuales del equipo y optimizar la precisión de las operaciones y el marketing mediante un sistema de alertas y borradores automáticos que siempre requieren **revisión humana** antes de ejecutarse.

## Funcionalidades

### 1. Gestión Inteligente de Inventario y Publicidad
- Consulta el stock de Shopify y alerta sobre productos agotados o con bajo inventario.
- Cruza el gasto en anuncios de Meta Ads contra el stock disponible.
- Genera alertas prioritarias cuando se están mostrando anuncios de productos sin stock.
- Detecta productos recién repuestos y genera borradores de marketing (Email, SMS, RRSS).

### 2. Generación de Contenido de Marketing
- Ideación de campañas basada en disponibilidad de inventario.
- Redacción de flujos para Klaviyo y anuncios para Meta.
- Contenido alineado con la identidad de la marca y atractivo para la comunidad del golf.

### 3. Asistente de Soporte al Cliente
- Redacción de borradores de respuesta a consultas de soporte.
- Extracción de información de pedidos de Shopify, políticas de empresa y respuestas anteriores.

### 4. Sincronización de Operaciones
- Mapeo de ventas de Whatnot hacia pedidos de Shopify.
- Preparación de datos de inventario para hojas de stock en shows en vivo.

## Estructura del Proyecto

```
├── .env                          # Credenciales y configuración del agente
├── .agent/                       # Configuración del framework de agente
│   ├── AGENT_FRAMEWORK.md
│   ├── AGENT_INSTRUCTIONS.md
│   └── Dockerfile
├── directives/                   # Directivas YAML para tareas específicas
│   └── check_shopify_inventory.yaml
├── docs/
│   └── OBJETIVO.md               # Prompt principal del agente
├── execution/                    # Scripts de ejecución
│   ├── env_diagnostic.py
│   └── shopify_get_inventory.py  # Consulta stock vía API de Shopify
├── requirements.txt              # psutil, python-dotenv, ShopifyAPI
├── env_diagnostic.py
├── git-update.sh
└── update_repo.sh
```

## Stack Tecnológico

- **Python 3** con `ShopifyAPI` para integración con tienda Shopify.
- **Directivas YAML** para orquestación de tareas automatizadas.
- Compatible con herramientas de automatización como **Zapier** o **Make.com**.

## Uso

```bash
# Consultar inventario de Shopify (threshold: stock mínimo antes de alertar)
python execution/shopify_get_inventory.py --threshold 5
```

El resultado se guarda en `.tmp/inventory_report.json` con listas de productos agotados y con stock bajo.

## Formato de Salida

- **Borradores para revisión humana**: Todo contenido generado se presenta como borrador.
- **Alerta Prioritaria**: Discrepancias entre gasto publicitario y stock se resaltan como alertas críticas.
