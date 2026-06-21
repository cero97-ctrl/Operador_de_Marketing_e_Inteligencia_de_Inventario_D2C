# Registro General de Errores de Compilación LaTeX y Soluciones

Este archivo actúa como una bitácora histórica y base de conocimiento para documentar y resolver cualquier error de compilación LaTeX (`pdflatex`, `xelatex`, etc.) que ocurra en los documentos del proyecto.

---

## 📋 Guía para registrar nuevos errores

Cuando ocurra un nuevo error de compilación, agrégalo al final de este archivo utilizando la siguiente estructura:

```markdown
## [Nombre Corto del Error]

- **Archivo afectado:** `ruta/del/archivo.tex`
- **Fecha:** AAAA-MM-DD

### ❌ Descripción del Error
[Pega aquí el extracto del log del compilador o la descripción del problema]

### 🔍 Causa Raíz
[Explica brevemente por qué ocurre este error en LaTeX]

### 🚀 Solución
[Detalla la corrección aplicada en el código LaTeX]
```

---

## 🗃️ Historial de Errores Registrados

### 1. Error de Lenguaje de Programación No Definido en `listings`

- **Archivo afectado:** [manual.tex](file:///home/cero/MEGA/VS_CODE_WORKSPACE/Operador_de_Marketing_e_Inteligencia_de_Inventario_D2C/manual.tex)
- **Fecha:** 2026-06-21

#### ❌ Descripción del Error
El compilador fallaba al procesar un bloque de código JSON:
```
! Package Listings Error: Couldn't load requested language.
...
l.263 \begin{lstlisting}[language=json]
! Package Listings Error: language json undefined.
```

#### 🔍 Causa Raíz
El paquete `listings` estándar de LaTeX no incluye una definición de sintaxis integrada para `json`. Al configurar `language=json`, el compilador lanza un error al no encontrar la definición correspondiente.

#### 🚀 Solución
Se eliminó el parámetro de lenguaje, dejando el inicio del bloque como:
```latex
\begin{lstlisting}
```
Esto permite renderizar el bloque como texto de ancho fijo simple sin interrumpir la compilación.

---

### 2. Comando No Definido (`\node`) en Entorno `enumerate`

- **Archivo afectado:** [manual.tex](file:///home/cero/MEGA/VS_CODE_WORKSPACE/Operador_de_Marketing_e_Inteligencia_de_Inventario_D2C/manual.tex)
- **Fecha:** 2026-06-21

#### ❌ Descripción del Error
```
! Undefined control sequence.
l.399     \node
                Delega en \texttt{update\_repo.sh}.
```

#### 🔍 Causa Raíz
Dentro del entorno `enumerate` (listas numeradas), se utilizó erróneamente `\node` en lugar de `\item` para definir un elemento de la lista.

#### 🚀 Solución
Se reemplazó `\node` por `\item` en el elemento de la lista afectado:
```latex
    \item Delega en \texttt{update\_repo.sh}.
```
