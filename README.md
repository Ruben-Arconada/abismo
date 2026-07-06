# 🎳 ABISMO

Una **bola de bolos se fuga de la bolera** para vivir una aventura. Rueda por plataformas flotantes sobre un abismo sin fin, atravesando distintas zonas —**ciudad**, montaña nevada, cueva y cueva de lava— y llega lo más lejos que puedas sin caer.

Juego web (HTML5 + Canvas) de un archivo, pensado para **móvil**, instalable como app (PWA) y jugable **sin conexión**.

## ▶️ Jugar

**https://ruben-arconada.github.io/abismo/**

## 🎮 Controles

- **Mitad izquierda de la pantalla** → *joystick* para moverte a izquierda/derecha.
- **Mitad derecha** → saltar. **Mantén pulsado = salto más largo.**
- En ordenador: **flechas** para moverte y **espacio / ↑** para saltar.
- Botón 🔊 arriba a la derecha para silenciar.

## 📲 Instalar en el móvil

- **iPhone (Safari):** botón *Compartir* → **Añadir a pantalla de inicio**. Arranca a pantalla completa.
- **Android (Chrome):** menú ⋮ → **Instalar aplicación** / *Añadir a pantalla de inicio*.

## ✨ Características

- Pantalla completa adaptada a cualquier móvil, nítida en pantallas retina y respetando el *notch* / áreas seguras.
- Sonido generado por código (WebAudio) y vibración (Android).
- 4 biomas que se funden entre sí, plataformas con bisel que se desvanecen en el abismo, y una bola de bolos con sombra 3D.
- Instalable (PWA) y offline mediante *service worker*.

## 🛠️ Desarrollo

Es estático: basta con servir la carpeta.

```bash
python3 -m http.server 8123
# abre http://localhost:8123/
```

Los iconos se regeneran con `tools/make_icons.py` (requiere Pillow).
